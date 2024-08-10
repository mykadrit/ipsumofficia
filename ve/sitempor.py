# Assuming you have an object 'self' with an 'age' attribute
class Person:
    def __init__(self, age):
        self.age = age

    def get_age_string(self):
        return f"Age: {round(self.age)}"

# Example usage
person = Person(25.6)
print(person.get_age_string())  # Output: Age: 26
