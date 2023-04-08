from dataclasses import dataclass
from math import cos, tan, exp, cosh, sin, pow as mpow

import numpy as np


@dataclass
class InputParameters:
    n: int
    step: float
    x = np.arange(-3.5, 3.5, 0.0003)

    def __post_init__(self):
        self.range = list(np.arange(0, self.n+self.step, self.step)) + \
                     list(np.arange(-self.n, self.n, self.step))[::-1] + \
                     list(np.arange(self.step-self.n, self.step, self.step))
        self.y = [f(x, 100) for x in self.x]


def f(x: float, n: float):
    try:
        return mpow(abs(x), 2/3) + mpow(10 - x**2, 1/2) * sin(n * x)
        # return sin(x+n)
    except (ZeroDivisionError, ValueError):
        return
