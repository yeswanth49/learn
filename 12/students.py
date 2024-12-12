class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"An Student {self.name} having {self.roll}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        roll = input("Roll: ")
        return Student(name,roll)
    
    def get_name(self):
        return self.name
    
    def get_roll(self):
        return self.roll
    
    @property
    def roll(self):
        return self.roll
    
    @roll.setter
    def roll(self,roll):
        if len(roll) !=2:
            raise ValueError("Invalid roll")
        
        self._roll = roll
    

def main():
    student = Student.get()
    print(f"{student.name} having {student.roll}")
    print(student.get_name())

if __name__ == "__main__" :
    main()