import random


class Elevator:
    # Only supports single destination
    directions = ["up", "down", "idle"]

    # Dunder methods
    def __init__(self, floors):
        self.floors = floors
        cur_floor = random.randint(floors[0], floors[-1])
        self.origin = cur_floor
        self.location = cur_floor
        self.destination = cur_floor
        self.direction = self.directions[-1]

    def __repr__(self):
        # A fun __repr__ of elevator loc:   1   2   3   4   #   6   7   8   9   10
        return "\t".join(
            ["#" if floor == self.location else str(floor) for floor in self.floors]
        )

    """

    Public methods used by Controller

    """

    def pickup(self, floor):
        # Called by controller to set new pickup loc
        self._dispatch(floor)

    def dropoff(self, floor):
        # Called by controller when user inputs desired dropoff loc
        self._dispatch(floor)

    def is_idle(self):
        # Used by controller to find all idle elevators
        return self.direction == "idle"

    def distance(self, floor):
        # Calculates distance between self and floor
        return abs(floor - self.location) + self._penalty(floor)

    """

    Private methods used within class only

    """

    def _dispatch(self, floor):
        # Sets internal state on elevator
        if floor < self.location:
            desired_direction = "down"
        elif floor > self.location:
            desired_direction = "up"
        else:
            desired_direction = "idle"

        self.direction = desired_direction
        self.destination = floor
        # TODO dispatch elevator on different thread perhaps

    def _arrived(self, floor):
        # Called after each evolution to check if location == destination, if so set internal state
        pass

    def _penalty(self, floor):
        # Calculate penalty for travelling in wrong direction as pickup loc
        delta = floor - self.location
        return (
            2
            if ((delta < 0) and self.direction == "up")
            or ((delta > 0) and self.direction == "down")
            else 0
        )
