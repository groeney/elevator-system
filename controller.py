from elevator import Elevator
from collections import namedtuple


class Controller:

    # Dunder methods
    def __init__(self, num_floors=10, num_elevators=4):
        self.floors = [i for i in range(1, num_floors + 1)]
        self.elevators = []
        for _ in range(num_elevators):
            self.add_elevator()

    def __repr__(self):
        # A fun __repr__ of elevator locs:  1   2   3   4   #   6   7   8   9   10
        #                                   1   2   3   4   5   6   7   8   #   10
        #                                   1   2   #   4   5   6   7   8   9   10
        #                                   1   #   3   4   5   6   7   8   9   10
        return "\n".join([str(elevator) for elevator in self.elevators])

    """

    Public methods used by God

    """

    def add_elevator(self):
        # Add new elevator worker to elevators list
        elevator = Elevator(self.floors)
        self.elevators.append(elevator)

    def request_pickup(self, floor):
        # When a user presses the button on their floor to request an elevator
        elevator = self._find_pickup_elevator(floor)
        elevator.pickup(floor)

    def request_dropoff(self, elevator, floor):
        # When a user presses the destination button in the elevator
        elevator.dropoff(floor)

    """

    Private methods used within class only

    """

    def _find_pickup_elevator(self, floor):
        # Iterates through the list of elevator instances and calculates the optimal elevator for the job
        Pick = namedtuple("Pick", "distance elevator")
        best_pick = Pick(len(self.floors) + 1, None)
        for elevator in self._idle_elevators():
            dist = elevator.distance(floor)
            if dist < best_pick.distance:
                best_pick = Pick(dist, elevator)
        return best_pick.elevator

    def _idle_elevators(self):
        return [elevator for elevator in self.elevators if elevator.is_idle()]
