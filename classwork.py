class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self, sound):
        return f"{self.name} says {sound}"

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."
    
cat = Pet(
    name="Catty",
    species="Cat",
    age=4
)
print(cat.make_sound("Meow"))
print(cat.celebrate_birthday())
    
