from abc import ABC, abstractmethod
from typing import List


# ----- Base Ingredient Abstraction -----
class Ingredient(ABC):
    @abstractmethod
    def get_name(self) -> str: ...

    @abstractmethod
    def get_cost(self) -> int: ...


# ----- Concrete Ingredients -----
class Crust(Ingredient):
    def __init__(self, name: str, cost: int):
        self._name = name
        self._cost = cost

    def get_name(self) -> str:
        return self._name

    def get_cost(self) -> int:
        return self._cost


class PizzaSize(Ingredient):
    def __init__(self, name: str, cost: int):
        self._name = name
        self._cost = cost

    def get_name(self) -> str:
        return self._name

    def get_cost(self) -> int:
        return self._cost


class Topping(Ingredient):
    def __init__(self, name: str, cost: int):
        self._name = name
        self._cost = cost

    def get_name(self) -> str:
        return self._name

    def get_cost(self) -> int:
        return self._cost


# ----- Pizza Abstraction -----
class Pizza(ABC):
    def __init__(self, size: PizzaSize, crust: Crust, toppings: List[Topping]):
        self.size = size
        self.crust = crust
        self.toppings = toppings

    @abstractmethod
    def get_name(self) -> str: ...

    def get_price(self) -> int:
        return (
            self.size.get_cost()
            + self.crust.get_cost()
            + sum(t.get_cost() for t in self.toppings)
        )


# ----- Concrete Pizzas -----
class CustomPizza(Pizza):
    def get_name(self) -> str:
        return f"{self.size.get_name()} {self.crust.get_name()} Pizza"


# ----- Order -----
class Order:
    def __init__(self):
        self.pizzas: List[Pizza] = []

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def get_total_cost(self) -> int:
        return sum(p.get_price() for p in self.pizzas)


# ----- Factory (Optional for extensibility) -----
class PizzaFactory:
    @staticmethod
    def create_custom_pizza(size: str, crust: str, toppings: List[str]) -> Pizza:
        size_map = {"Small": 5, "Medium": 7, "Large": 10}
        crust_map = {"Regular": 2, "Cheese": 3, "HandTossed": 4}
        topping_map = {"Chicken": 3, "Pepperoni": 4, "Steak": 5}

        size_obj = PizzaSize(size, size_map[size])
        crust_obj = Crust(crust, crust_map[crust])
        topping_objs = [Topping(t, topping_map[t]) for t in toppings]

        return CustomPizza(size_obj, crust_obj, topping_objs)


# ----- Usage -----
def main():
    order = Order()

    pizza1 = PizzaFactory.create_custom_pizza("Small", "Cheese", ["Chicken", "Steak"])
    pizza2 = PizzaFactory.create_custom_pizza("Large", "HandTossed", ["Pepperoni"])

    order.add_pizza(pizza1)
    order.add_pizza(pizza2)

    print("Total Order Cost:", order.get_total_cost())


if __name__ == "__main__":
    main()
