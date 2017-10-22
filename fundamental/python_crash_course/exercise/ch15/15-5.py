# 15-5
# 重构 ：
# 方法fill_walk() 很长。
# 请新建一个名为get_step() 的方法，用于确定每次漫步的距离和方向，并计算这次漫步将如何移动。
# 然后，在fill_walk() 中调用get_step() 两次：
# x_step = get_step()
# y_step = get_step()
# 通过这样的重构，可缩小fill_walk() 的规模，让这个方法阅读和理解起来更容易。

from random import choice


class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, and how far to go in that direction.

            x_step = self.get_step(self, [1, -1], [0, 1, 2, 3, 4])
            y_step = self.get_step(self, [1], [0, 1, 2, 3, 4,5])

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self, direction_range, distance_range):
        return choice(direction_range) * choice(distance_range)
