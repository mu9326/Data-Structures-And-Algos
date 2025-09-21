# UnboundedSet():
class UnboundedSet:
    def __init__(self):
        self.set = set()

    # set = ()
    # fetch_element()
    def fetch_element(self, element: int):
        if element in self.set:
            return element

    def add_element(self, element: int):
        self.set.add(element)
        print("Element added!")

    def remove_element(self, element: int):
        self.set.remove(element)
        print("Element removed!")
