# The system should support multiple elevators, each with its own capacity and ability to serve requests independently.
# The system should allow users to request an elevator by specifying a source floor and destination floor.
# The system should have a mechanism to assign the most optimal elevator to a request, based on proximity or other criteria.
# Elevators should be able to process requests sequentially, simulating movement between floors in a chosen direction.
# The system should handle concurrent requests safely and ensure no request is lost or starved.


class Floor:
    def __init__(self, id):
        pass

    def get_id(self):
        pass


class Elevator:
    def __init__(self, capacity):
        self.capacity = capacity
        pass

    def request_elevator(source: Floor, destination: Floor):
        pass


class ElevatorController:
    def __init__(self):
        self.elevators = []
        pass

    def assign_elevator(self, user):
        pass

    def process_request(self):
        pass


class User:
    def __init__(self, id, name):
        pass

    def make_request(self):
        pass


def main():
    User()
