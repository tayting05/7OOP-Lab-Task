Main.py

from carClass import Car
def main():
 car1 = Car("red", 19999.85, "M")
 car2 = Car("blue", 50000.00, "L")
 car3 = Car("green", 12345.67, "S")
 print("Action: Invoking the Car class constructor using
Car('red', 19999.85, 'M').")
 print("Output:")
 print(car1)
 print("\nAction: Invoking the Car class constructor using
Car('blue', 50000.00, 'L').")
 print("Output:")
 print(car2)
 print("\nAction: Invoking the Car class constructor using
Car('green', 12345.67, 'S').")
 print("Output:")
 print(car3)
if __name__ == "__main__":
 main()

==========================================================================
carClass.py

class Car:
 def __init__(self, color: str, price: float, size: str):
 self.__color = color
 self.__price = price
 self.__size = size.upper()
 # set
 def set_color(self, color: str) -> None:
 self.__color = color
 def set_price(self, price: float) -> None:
 self.__price = price
 def set_size(self, size: str) -> None:
 self.__size = size.upper()
 # get
 def get_color(self) -> str:
   return self.__color
 def get_price(self) -> float:
 return self.__price
 def get_size(self) -> str:
 return self.__size
 # string
 def __str__(self) -> str:
 size_desc = {
 'S': 'small',
 'M': 'medium',
 'L': 'large'
 }.get(self.__size, 'unknown')
 return f"Car ({self.__color}) - P{self.__price:.2f} -
{size_desc}"
