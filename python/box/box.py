"""This file conaint the box class."""


class box:
    """A cubic box with mass and width."""

    def __init__(self, mass, width, x0, v0=0):
        """
        Create a squared box.

        Args:
        ----
        mass: The mass of the box [Kg].
        width: The width of the box [m].
        x0: The initial position [m].
        v0: The initial velocity [m/s].

        """
        self.mass = mass
        self.width = width
        self.v = v0
        self.x = x0
