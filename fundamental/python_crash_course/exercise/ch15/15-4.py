# 15-4
# 改进的随机漫步 ：
# 在类RandomWalk 中，x_step 和y_step 是根据相同的条件生成的：
# 从列表[1, -1] 中随机地选择方向，并从列表[0, 1, 2, 3, 4]中随机地选择距离。
# 请修改这些列表中的值，看看对随机漫步路径有何影响。尝试使用更长的距离选择列表，如0~8；
# 或者将-1从 x 或 y 方向列表中删除。
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
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6])
            x_step = x_direction * x_distance

            y_direction = choice([-1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
