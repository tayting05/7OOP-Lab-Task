performer.py

class Performer:
   def __init__(self, name: str, age: int):
       self._name = name
       self._age = age


   def get_name(self) -> str:
       return self._name


   def get_age(self) -> int:
       return self._age


   def display_info(self) -> None:
       print(f"{self.get_name()}  {self.get_age()} ")
=======================================================
singer.py

from performer import Performer


class Singer(Performer):
   def __init__(self, name: str, age: int, vocal_range: str):
       super().__init__(name, age)
       self._vocal_range = vocal_range


   def get_vocal_range(self) -> str:
       return self._vocal_range


   def sing(self) -> None:
       print(f"{self.get_name()} is singing with a {self.get_vocal_range()} range.")
=======================================================
dancer.py

from performer import Performer


class Dancer(Performer):
   def __init__(self, name: str, age: int, dance_style: str):
       super().__init__(name, age)
       self._dance_style = dance_style


   def get_dance_style(self) -> str:
       return self._dance_style


   def dance(self) -> None:
       print(f"{self.get_name()} is performing {self.get_dance_style()} dance.")
=======================================================
test_class.py

from performer import Performer
from singer import Singer
from dancer import Dancer


def test_performer():
   performer = Performer("John", 25)
   performer.display_info()


def test_dancer():
   dancer = Dancer("Emily", 28, "Ballet")
   print(f"{dancer.get_name()} {dancer.get_age()} {dancer.get_dance_style()}")
   dancer.dance()


def test_singer():
   singer = Singer("Linda", 35, "Soprano")
   print(f"{singer.get_name()} {singer.get_age()} {singer.get_vocal_range()}")  
   singer.sing()
if __name__ == "__main__":
   test_performer()
   test_dancer()
   test_singer()
