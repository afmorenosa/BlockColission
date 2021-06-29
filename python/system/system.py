"""This file contain a tow boxes system."""
from box import box


class base_system(object):
    """A system of two boxes."""

    def __init__(self,
                 mass_1, mass_2,
                 width_1, width_2,
                 x0_1, x0_2,
                 v0_1=0, v0_2=0,
                 h=0.1):
        """
        Create the system of two boxes.

        Args:
        ----
            mass_1: Mass of the first box [Kg].
            mass_2: Mass of the second box [Kg].
            width_1: Width of the first box [m].
            width_2: Width of the second box [m].
            x0_1: Initial position of the first box [m].
            x0_2: Initial position of the second box [m].
            v0_1: Initial velocity of the first box [m/s].
            v0_2: Initial velocity of the second box [m/s].
            h: Time step [s].

        """
        self.box_1 = box.box(mass_1, width_1, x0_1, v0_1)
        self.box_2 = box.box(mass_2, width_2, x0_2, v0_2)
        self.h = h
        self.coll_counter = 0

    def box_collision(self):
        """Test if the bloxes had collied."""
        border_box_pos_1 = self.box_1.x + self.box_1.width/2
        border_box_pos_2 = self.box_2.x - self.box_2.width/2

        if (border_box_pos_2 - border_box_pos_1) <= 0:
            return True
        else:
            return False

    def wall_collision(self):
        """Test if the bloxes had collied."""
        border_box_pos_1 = self.box_1.x - self.box_1.width/2

        if (border_box_pos_1) <= 0:
            return True
        else:
            return False

    def time_step_evolution(self):
        """Make a step in time."""
        self.box_1.x += self.h * self.box_1.v
        self.box_2.x += self.h * self.box_2.v

        if self.box_collision():

            aux_v_1 = self.box_1.v
            aux_v_2 = self.box_2.v
            self.box_1.v =\
                (aux_v_1 * (self.box_1.mass - self.box_2.mass) +
                 2*aux_v_2*self.box_2.mass)/(self.box_1.mass + self.box_2.mass)
            self.box_2.v =\
                (aux_v_2 * (self.box_2.mass - self.box_1.mass) +
                 2*aux_v_1*self.box_1.mass)/(self.box_2.mass + self.box_1.mass)
            self.coll_counter += 1

        elif self.wall_collision():

            self.box_1.v = -self.box_1.v
            self.coll_counter += 1


class sm_system(base_system):
    """System with two boxes of the same mass."""

    def __init__(self,
                 mass,
                 width_1, width_2,
                 x0_1, x0_2,
                 v0_1=0, v0_2=0,
                 h=0.01):
        """
        Create the system of two boxes with same mass.

        Args:
        ----
            mass: Mass of the boxes [Kg].
            width_1: Width of the first box [m].
            width_2: Width of the second box [m].
            x0_1: Initial position of the first box [m].
            x0_2: Initial position of the second box [m].
            v0_1: Initial velocity of the first box [m/s].
            v0_2: Initial velocity of the second box [m/s].
            h: Time step [s].

        """
        super().__init__(mass, mass,
                         width_1, width_2,
                         x0_1, x0_2,
                         v0_1, v0_2, h)


class sb_system(base_system):
    """System with two boxes of the same mass and width (same boxes)."""

    def __init__(self,
                 mass,
                 width,
                 x0_1, x0_2,
                 v0_1=0, v0_2=0,
                 h=0.01):
        """
        Create the system of two identical boxes.

        Args:
        ----
            mass: Mass of the boxes [Kg].
            width: Width of the boxes [m].
            x0_1: Initial position of the first box [m].
            x0_2: Initial position of the second box [m].
            v0_1: Initial velocity of the first box [m/s].
            v0_2: Initial velocity of the second box [m/s].
            h: Time step [s].

        """
        super().__init__(mass, mass,
                         width, width,
                         x0_1, x0_2,
                         v0_1, v0_2, h)


class simple_system(base_system):
    """
    Simplest system.

    System with two boxes of the same mass, width and default initial
    conditions.
    """

    def __init__(self,
                 h=0.01):
        """
        Create the system of two identical boxes and default conditions.

        Args:
        ----
            h: Time step [s].

        """
        super().__init__(1, 100000000,
                         1, 1,
                         5, 10,
                         0, -1, h)
