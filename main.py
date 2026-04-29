#7-misol
class Kitob:
    def __init__(self, nomi):
        self.nomi = nomi

    def info(self):
        print(f" Kitob: {self.nomi}")

class Darslik(Kitob):
    def __init__(self, nomi, fan):
        super().__init__(nomi)
        self.fan = fan

    def info(self):
        super().info()
        print(f"Fan: {self.fan}")

d = Darslik("Algebra", "Matematika")
d.info()
