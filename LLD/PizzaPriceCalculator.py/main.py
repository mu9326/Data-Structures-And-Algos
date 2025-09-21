from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class CrustType(Enum):
    Regular = 2
    Cheese = 3
    HandTossed = 4


class Crust:
    def __init__(self, name):
        self.type = CrustType[name]  # Lookup enum member by string
        self.cost = self.type.value  # Cost comes from enum value

    def getName(self):
        return self.type.name  # "Regular", "Cheese", etc.

    def getCost(self):
        return self.cost  # 2, 3, or 4


class PizzaSizeType(Enum):
    Small = 5
    Medium = 7
    Large = 10


class PizzaSize:
    def __init__(self, name):
        self.type = PizzaSizeType[name]  # Lookup enum member by string
        self.cost = self.type.value

    def getName(self):
        return self.type.name

    def getCost(self):
        return self.cost


class ToppingType(Enum):
    Chicken = 3
    Pepperoni = 4
    Steak = 5


class Topping:
    def __init__(self, name):
        self.type = ToppingType[name]
        self.cost = self.type.value

    def getName(self):
        return self.type.name

    def getCost(self):
        return self.cost


class Pizza:
    def __init__(self, size: str, crust: str, toppings: List[Topping]):
        self.size = size
        self.crust = crust
        self.toppings = toppings

    def getSizeCost(self):
        return PizzaSize(self.size).getCost()

    def getCrustCost(self):
        return Crust(self.crust).getCost()

    def getToppingsCost(self):
        total_toppings = 0
        for topping in self.toppings:
            total_toppings += Topping(topping).getCost()
        return total_toppings

    def getPrice(self):
        total = self.getSizeCost() + self.getCrustCost() + self.getToppingsCost()
        return total


class Order:
    def __init__(self):
        self.pizzas = []

    def getTotalOrderCost(self):
        totalOrderCost = 0
        for pizza in self.pizzas:
            # print(pizza.getPrice())
            totalOrderCost += pizza.getPrice()
        return totalOrderCost

    def placeOrder(self, pizzas):
        for pizza in pizzas:
            self.pizzas.append(pizza)

        return self.getTotalOrderCost()


def main():
    # get the input from the user for the pizza_size, crust_type, toppings

    # make a pizza object
    # add the pizza object to the list

    pizzas = [
        Pizza("Small", "Cheese", ["Chicken", "Steak"]),
        Pizza("Large", "HandTossed", ["Pepperoni"]),
    ]

    # user places the order using the above list
    print(Order().placeOrder(pizzas))

    # order returns the total cost


if __name__ == "__main__":
    main()
