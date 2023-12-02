#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self):
        self._name = None  # Initializing _name as None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

# Example usage:
my_dog = Dog()
my_dog.name = "Buddy"  # Setting a valid name
print(my_dog.name)  # Output: Buddy

my_dog.name = "ThisIsAReallyLongNameForADog"  # Setting an invalid name
# Output: Name must be a string between 1 and 25 characters.

class Dog:
    approved_breeds = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]  # List of approved breeds

    def __init__(self):
        self._breed = None  # Initializing _breed as None

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

# Example usage:
my_dog = Dog()
my_dog.breed = "Mastiff"  # Setting a valid breed
print(my_dog.breed)  # Output: Labrador

my_dog.breed = "Terrier"  # Setting an invalid breed
# Output: Breed must be in list of approved breeds.

