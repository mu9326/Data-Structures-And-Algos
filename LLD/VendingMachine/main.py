# The vending machine should allow customers to select an item from the available stock.
# Customers must insert money, and the machine should validate if enough funds have been provided to purchase the selected item.
# The machine should dispense the selected item if it is in stock and return any change if excess money was inserted.
# If the item is out of stock or the transaction cannot be completed, the machine should cancel the transaction and return the inserted money.
# The system should support loading and managing inventory for different items.

# Item: Enum
# name
# cost

# Inventory: ABC
# for a given item, it stores the stock of that item
# add_item()
# remove_item()
# get_item()
# is_out_of_stock()
# is_in_stock()

# Machine: ABC
# loads the inventory (for each item and its number)
# add_to_inventory(item, number):
# create the inventory object with item and number
# display the inventory alongwith the cost of each item in the inventory
# let customers select an item -
# selectItem(itemId) - if validateTransaction(funds) is 0 and the item is in stock --> processTransaction() --> change is zero --> return change + item
# - if validateTransaction(funds) is 1 and the item is in stock --> processTransaction() --> returnChange() --> return change + item
# - if validateTransaction(funds) is 2 --> return funds + None
# validateTransaction(funds) --> if funds are enough, return 0. if funds are more than enough, return 1. if funds are less than enough, return 2
# returnChange(funds) --> subtracts the funds from cost
# processTransaction(item)

from enum import Enum
from abc import ABC, abstractmethod


class Transaction:
    pass


class Item(ABC):
    @abstractmethod
    def __init__(self, id, name, cost):
        self.id = id
        self.name = name
        self.cost

    @abstractmethod
    def getCost(self):
        pass


class Inventory:
    def __init__(self, item: Item, number: int):
        for _ in range(number):
            self.stock.append(item)

    def isOutOfStock(self):
        pass

    def isAvailable(self):
        pass

    pass


class Machine:
    # load the stock
    # display the available stock

    pass
