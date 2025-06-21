import tkinter as tk
import random

symbols = ["♾", "☺", "☢", "☯", "☂", "☠"]
raresymbol = ["Ⓐ", "☭", "☮"]

class BanditGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Einarmiger Bandit")
        self.geometry("400x250")
        self.configure(bg="#222")

        self.money = 10000

        self.label = tk.Label(self, text="Willkommen zum Einarmigen Banditen!", font=("Arial", 14), bg="#222", fg="white")
        self.label.pack(pady=10)

        self.money_label = tk.Label(self, text=f"Geld: {self.money} Euro", font=("Arial", 12), bg="#222", fg="lime")
        self.money_label.pack(pady=5)

        self.symbols_label = tk.Label(self, text="", font=("Arial", 40), bg="#222", fg="yellow")
        self.symbols_label.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 12), bg="#222", fg="white")
        self.result_label.pack(pady=10)

        self.spin_button = tk.Button(self, text="Drehen", command=self.spin, font=("Arial", 12))
        self.spin_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Beenden", command=self.destroy, font=("Arial", 12))
        self.quit_button.pack(pady=5)

    def spin(self):
        x = random.randint(1, 7)
        y = random.randint(1, 7)
        z = random.randint(1, 7)

        symbol1 = random.choice(raresymbol) if x == 1 else random.choice(symbols)
        symbol2 = random.choice(raresymbol) if y == 1 else random.choice(symbols)
        symbol3 = random.choice(raresymbol) if z == 1 else random.choice(symbols)

        self.symbols_label.config(text=f"{symbol1} {symbol2} {symbol3}")
        if symbol1 == "Ⓐ" and symbol2 == "Ⓐ" and symbol3 == "Ⓐ":
            self.result_label.config(text="ANARCHY! Hauptgewinn!")
            self.money += 10000
        elif symbol1 == "☭" and symbol2 == "☭" and symbol3 == "☭":
            self.result_label.config(text="KOMMUNISMUS!")
            self.money += 5000
        elif symbol1 == "☮" and symbol2 == "☮" and symbol3 == "☮":
            self.result_label.config(text="FRIEDEN!!!")
            self.money += 10000
        elif symbol1 == symbol2 == symbol3:
            self.result_label.config(text="Jackpot! Du hast gewonnen!")
            self.money += 1000
        elif symbol1 in raresymbol and symbol2 in raresymbol and symbol3 in raresymbol:
            self.result_label.config(text="SELTEN!")
            self.money += 1000
        else:
            self.result_label.config(text="Leider kein Gewinn, versuche es erneut.")
            self.money -= 10

        self.money_label.config(text=f"Geld: {self.money} Euro")

if __name__ == "__main__":
    app = BanditGame()
    app.mainloop()