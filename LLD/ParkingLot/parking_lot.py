from typing import List
from level import Level
from vehicle import Vehicle


class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot._instance = self
            self.levels: List[Level] = []

    # get_instance needs to be callable without an instance because it's the method that creates or returns the singleton instance.
    # Using @staticmethod allows calling it like ParkingLot.get_instance() right from the class.
    # If it were a normal method, you'd need an instance first, which defeats the purpose of the singlet
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance

    def add_level(self, level: Level) -> None:
        self.levels.append(level)

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False

    def display_availability(self):
        for level in self.levels:
            level.display_availability()
