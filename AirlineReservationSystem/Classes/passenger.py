# passenger.py

class Passenger:
    def __init__(self, name, passport_number, age):
        self.name = name
        self.passport_number = passport_number
        self.age = age
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data['name'],
            passport_number = data['passport_number'],
            age = data['age']
        )
    
    def to_dict(self):
        return {
            'name': self.name,
            'passport_number': self.passport_number,
            'age': self.age
        }
    
    def display(self):
        print(f'\n{"-" * 25}')
        print("Name:", self.name)
        print("Age:", self.age)
        print("Passport Number:", self.passport_number)
        print("-" * 25)