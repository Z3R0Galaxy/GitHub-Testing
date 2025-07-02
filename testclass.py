class Me:
    def __init__(self, favColor: str, favNum: int, sport: str):
        self.favColor = favColor
        self.favNum = favNum
        self.sport = sport

    def describe(self):
        print(f"my fav color is {self.favColor}")

person = Me("blue", 2, "volleyball")
person.describe()