class Person:
    age=0
    def __init__(self,initialAge):
        self.initialAge=initialAge
        if self.initialAge<0:
            print("Age is not valid, setting age to 0")
        else:
            age=self.initialAge
    def yearPasses(self):
            age = self.initialAge + 1
            return age #increase the age by 1
    def amIOld(self):
            if self.initialAge < 13:
                return "You are young."
            elif self.initialAge >= 13 and self.initialAge < 18:
                return "You are a teenager."
            else:
                return "You are old."

for i in range(-5,30):
    Oreoluwa=Person (i)
    print(Oreoluwa.initialAge)
    print(Oreoluwa.amIOld())
    print("")
# print(Meleyotan.amIOld())
# print(Meleyotan.yearPasses())
# print(Oreoluwa.amIOld())
# print(Oreoluwa.yearPasses())
# print(Olubukola.amIOld())
# print(Olubukola.yearPasses())
# print(Dad.amIOld())
# print(Dad.yearPasses())
# print(Mum.amIOld())
# print(Mum.yearPasses())