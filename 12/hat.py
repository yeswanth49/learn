import random
class Hat:
    houses = ["Griffindor","Slytherin","Ravelclaw"]

    @classmethod
    def sort(cls,name):
        return f"{name}'s house is {random.choice(cls.houses)}"
    
print(Hat.sort("Harry"))