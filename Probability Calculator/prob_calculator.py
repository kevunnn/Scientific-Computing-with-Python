import copy
import random


class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for k, v in kwargs.items():
            while v != 0:
                self.contents.append(k)
                v = v - 1   

    def draw(self, draws: int):
        colors = random.choices(self.contents,k=draws)
        for color in colors:
            self.contents.remove(color)
        return colors
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0
    for i in range(num_experiments):
        expected = dict(expected_balls)
        colors = random.sample(hat.contents, k=min(num_balls_drawn, len(hat.contents)))
        for color in colors:
            if color in expected:
                expected[color] -= 1
        if all(value < 1 for value in expected.values()):
            match += 1

    probability = match / num_experiments
    return probability