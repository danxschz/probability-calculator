# Probability Calculator -- Scientific Computing with Python Project #5

## Imports
import copy
import random

## Main object
class Hat:

    # Functions
    def __init__(self, **kwargs):
        self.contents = list()
        for color, number in kwargs.items():
            while number > 0:
                self.contents.append(color)
                number -= 1

    def draw(self, numberofballs):
        if numberofballs > len(self.contents):
            return self.contents
        drawnballs = list()
        while numberofballs > 0:
            rnumber = random.randrange(len(self.contents))
            drawnballs.append(self.contents[rnumber])
            self.contents.pop(rnumber)
            numberofballs -= 1
        return drawnballs

## Experiment function
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    timesweget = 0
    n = num_experiments
    while n > 0:
        copyhat = copy.deepcopy(hat)
        balls = copyhat.draw(num_balls_drawn)
        for color, number in expected_balls.items():
            if balls.count(color) < number:
                weget = False
                break
            else:
                weget = True
        if weget is True:
            timesweget += 1
        n -= 1
    probability = timesweget / num_experiments
    return probability
