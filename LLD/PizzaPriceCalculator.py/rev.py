# main_pizzashop.py

from enum import Enum
from typing import List, Set

# Step 1: Define Enums for fixed choices to make the code robust and readable.
# Each enum member holds its base price.


class Size(Enum):
    SMALL = (8.00, "Small")
    MEDIUM = (10.00, "Medium")
    LARGE = (12.00, "Large")

    def __init__(self, price, description):
        self.price = price
        self.description = description


class Crust(Enum):
    THIN = (2.00, "Thin Crust")
    HAND_TOSSED = (2.50, "Hand-Tossed")
    DEEP_DISH = (3.50, "Deep Dish")

    def __init__(self, price, description):
        self.price = price
        self.description = description


class Topping(Enum):
    PEPPERONI = (1.50, "Pepperoni")
    MUSHROOMS = (1.00, "Mushrooms")
    ONIONS = (0.75, "Onions")
    EXTRA_CHEESE = (2.00, "Extra Cheese")
    TOMATO_SAUCE = (0.50, "Tomato Sauce")
    BASIL = (0.75, "Basil")

    def __init__(self, price, description):
        self.price = price
        self.description = description


class Pizza:
    def __init__(self):
        pass

    class Builder:
        def __init__(self):
            self.size = None
            self.crust = None
            self.toppings = set()

        def with_size(self, size):
            self.size = size
            return self

        def with_crust(self, crust):
            self.crust = crust
            return self

        def add_topping(self, topping):
            self.toppings.add(topping)
            return self

        def build(self):
            if not self.size or not self.crust:
                raise ValueError("A pizza must have a size and a crust.")
            return Pizza(self)
