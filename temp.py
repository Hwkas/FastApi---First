from enum import Enum


class Choices(Enum):
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"
    FOURTH = "fourth"


choices = Choices().value

print(choices)


from functools import wraps
