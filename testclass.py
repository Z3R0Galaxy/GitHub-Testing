class Me:
    def __init__(self, name: str, favColor: str, favNum: int, sport: str):
        self.name = name
        self.favColor = favColor
        self.favNum = favNum
        self.sport = sport

    def describe(self):
        print(f"{self.name}'s favorite color is {self.favColor}, favorite number is {self.favNum}, and sport is {self.sport}.")

Orlando = Me("Orlando", "green", 2, "volleyball")
Alex = Me("Alex", "red", 6, "F1")
Avalon = Me("Avalon", "purple", 4, "equestrian")

Orlando.describe()
Alex.describe()
Avalon.describe()