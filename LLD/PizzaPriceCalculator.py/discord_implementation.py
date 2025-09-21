# PIZZA PRICE CALCULATOR
from enum import Enum


# CHANGE THE SIZE AND TOPPINGS AND PRICES BASED ON YOUR RUBRIC
class Size(Enum):
    # use enums to help make things easier, just pass in word and
    # you already know the price

    SMALL = ("Small", 5.00)
    MEDIUM = ("Medium", 7.00)
    LARGE = ("Large", 10.00)

    def __init__(self, name: str, baseprice: float):
        self.name = name
        self.baseprice = baseprice


class Topping:
    def __init__(self, name: str, cost: float):
        self.name = name
        self.cost = cost


class Crust(Enum):
    Cheesy = ("cheesy", 5.00)
    random = ("random", 7.00)
    thin = ("thin", 10.00)

    def __init__(self, crusttype: str, crustprice: float):
        self.crusttype = crusttype
        self.crustprice = crustprice


class Pizza:
    def __init__(self, size: Size, crust):
        self.size = size
        self.toppings = []

    def addtopping(self, topping):
        self.toppings.append(topping)

    def calculateprice(self):
        totalprice = self.size.baseprice
        totalprice += self.Crust.crustprice
        for topping in self.toppings:
            totalprice += topping.cost
        totalprice = totalprice * self.size.baseprice
        return totalprice


class PizzaOrder:
    def __init__(self):
        self.pizzas = []

    def addpizza(self, pizza):
        self.pizzas.append(pizza)

    def calculatetotal(self):
        return sum(pizza.calculateprice() for pizza in self.pizzas)
