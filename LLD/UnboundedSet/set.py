"""
unbounded set refers to set without a limit on number of elements it can hold.
no maximum size.

in this unbounded set
1. insert elements with TTL (time to live) and it won't reject new entries due to size limitations.
2. expiration logic: each element has a TTL so even though set is unbounded in size, expired elements are automatically cleaned up.
3. set is not unbounded by time. becuase element is removed based on its TTL

unbounded set is dictionary backed set that can grow indefinitely but elements don't live forever - they expire at a specified time.


"""

from abc import ABC, abstractmethod
import time


class IsSet(ABC):
    # interface for set related function which should be implemented by any set
    @abstractmethod
    def insert(self, element, ttl):
        pass

    @abstractmethod
    def contains(self, element):
        pass

    @abstractmethod
    def remove(self, element):
        pass

    @abstractmethod
    def __iter__(self):
        # iterator on set for non expired elements
        pass

    @abstractmethod
    def length(self):
        # return length of set
        pass


class Unbounded_Set(IsSet):
    def __init__(self):
        self.setobj = {}

    def insert(self, element, ttl):
        # if element in self.setobj:
        #     self.setobj[element] = ttl

        # else:
        #     self.setobj[element] == ttl

        # expiration time in seconds
        expiration_time = time.time() + ttl
        self.setobj[element] = expiration_time

    def cleanup(self):
        current_time = time.time()
        # for i in range(self.length()):
        #     if self.setobj[i] > current_time:
        #         del self.setobj[i]
        keys = [key for key, value in list(self.setobj.items()) if value < current_time]
        for key in keys:
            del self.setobj[key]

    def contains(self, element):
        # if element in self.setobj:
        #     if self.setobj[element] < time.time():
        #         return True

        # return False
        self.cleanup()
        return element in self.setobj

    def length(self):
        return len(self.setobj)

    def remove(self, element):
        self.cleanup()
        if element in self.setobj:
            del self.setobj[element]
            return True

        return False

    def __iter__(self):
        self.cleanup()
        return iter(self.setobj)


def main():
    s = Unbounded_Set()
    s.insert("one", 10)
    s.insert(2, 10)
    s.insert("third", 10)
    # s.c

    print(s.contains(2))

    for element in s:
        print(element)
    # time.sleep(2)

    for element in s:
        print(element)

    print(s.remove("one"))

    for element in s:
        print(element)


if __name__ == "__main__":
    main()
