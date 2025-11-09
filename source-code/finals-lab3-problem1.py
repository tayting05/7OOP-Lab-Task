bird.py

from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, color, age, sound=""):
        self.color = color
        self.age = age
        self.sound = sound

    @abstractmethod
    def make_sound(self):
        print("Generic Bird Sound")
====================================================
sparrow.py

from bird import Bird

class Sparrow(Bird):
    def make_sound(self):
        print("Chirp Chirp!")
====================================================
parrot.py

from bird import Bird

class Parrot(Bird):
    def make_sound(self):
        print("Tweet Tweet!")
====================================================
birdCage.py

class BirdCage:
    def make_bird_sounds(self, birds: list):
        for bird in birds:
            bird.make_sound()
====================================================
main.py

from sparrow import Sparrow
from parrot import Parrot
from birdCage import BirdCage

def main():
    birds = []
    num = int(input("How many birds do you want to add? "))

    for i in range(num):
        print(f"\nBird {i+1}:")
        btype = input("Enter bird type (sparrow/parrot): ").strip().lower()
        color = input("Enter color: ")
        age = int(input("Enter age: "))

        if btype == "sparrow":
            birds.append(Sparrow(color, age))
        elif btype == "parrot":
            birds.append(Parrot(color, age))
        else:
            print("Unknown bird type, skipping this one.")

    if birds:
        cage = BirdCage()
        print("\nBird sounds:")
        cage.make_bird_sounds(birds)
    else:
        print("No birds to display.")

if __name__ == "__main__":
    main()
