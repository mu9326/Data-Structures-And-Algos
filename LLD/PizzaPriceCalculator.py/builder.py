from abc import ABC, abstractmethod
from typing import List, Set


# ----- Ingredient Abstraction -----
class Ingredient(ABC):
    """Base class for all pizza ingredients."""

    @abstractmethod
    def get_name(self) -> str: ...

    @abstractmethod
    def get_cost(self) -> float: ...


# ----- Concrete Ingredients -----
class Size(Ingredient):
    def __init__(self, name: str, cost: float):
        self._name = name
        self._cost = cost

    def get_name(self) -> str:
        return self._name

    def get_cost(self) -> float:
        return self._cost


class Crust(Ingredient):
    def __init__(self, name: str, cost: float):
        self._name = name
        self._cost = cost

    def get_name(self) -> str:
        return self._name

    def get_cost(self) -> float:
        return self._cost


class Topping(Ingredient):
    def __init__(self, name: str, cost: float):
        self._name = name
        self._cost = cost

    def get_name(self) -> str:
        return self._name

    def get_cost(self) -> float:
        return self._cost


# ----- Pizza Class with Builder -----
class Pizza:
    def __init__(self, builder: "Pizza.Builder"):
        self.size: Size = builder.size
        self.crust: Crust = builder.crust
        self.toppings: Set[Topping] = builder.toppings

    def calculate_price(self) -> float:
        return round(
            self.size.get_cost()
            + self.crust.get_cost()
            + sum(t.get_cost() for t in self.toppings),
            2,
        )

    def __str__(self) -> str:
        toppings_list = ", ".join(t.get_name() for t in self.toppings) or "No Toppings"
        return f"{self.size.get_name()} {self.crust.get_name()} Pizza with {toppings_list} (${self.calculate_price():.2f})"

    # --- Fluent Builder (Nested Class) ---
    class Builder:
        def __init__(self):
            self.size: Size = None
            self.crust: Crust = None
            self.toppings: Set[Topping] = set()

        def with_size(self, size: Size):
            self.size = size
            return self

        def with_crust(self, crust: Crust):
            self.crust = crust
            return self

        def add_topping(self, topping: Topping):
            self.toppings.add(topping)
            return self

        def build(self) -> "Pizza":
            if not self.size or not self.crust:
                raise ValueError("Pizza must have both size and crust.")
            return Pizza(self)


# ----- Order Class -----
class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.items: List[Pizza] = []

    def add_item(self, pizza: Pizza):
        self.items.append(pizza)

    def calculate_total(self) -> float:
        return round(sum(p.calculate_price() for p in self.items), 2)


# ----- Receipt Formatter (UI Layer) -----
class ReceiptPrinter:
    @staticmethod
    def print(order: Order):
        print(f"--- Order #{order.order_id} ---")
        if not order.items:
            print("No items in order.")
        else:
            for item in order.items:
                print(str(item))
        print("---------------------")
        print(f"Total: ${order.calculate_total():.2f}")
        print("---------------------")


# ----- Example Usage -----
def main():
    # Define possible ingredients (could come from config or DB in real system)
    small = Size("Small", 8.0)
    large = Size("Large", 12.0)
    deep_dish = Crust("Deep Dish", 3.5)
    thin = Crust("Thin Crust", 2.0)
    pepperoni = Topping("Pepperoni", 1.5)
    mushrooms = Topping("Mushrooms", 1.0)
    onions = Topping("Onions", 0.75)

    # Build pizzas using Builder
    pizza1 = (
        Pizza.Builder()
        .with_size(large)
        .with_crust(deep_dish)
        .add_topping(pepperoni)
        .add_topping(mushrooms)
        .add_topping(onions)
        .build()
    )

    pizza2 = (
        Pizza.Builder().with_size(small).with_crust(thin).add_topping(mushrooms).build()
    )

    # Place order
    order = Order(order_id=202)
    order.add_item(pizza1)
    order.add_item(pizza2)

    # Print receipt
    ReceiptPrinter.print(order)


if __name__ == "__main__":
    main()
