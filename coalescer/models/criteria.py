from abc import ABC, abstractmethod


class Criteria(ABC):
    def __init__(self, data: list):
        self.data = data

    """Returns a value according to the data and criteria"""
    @abstractmethod
    def calculate(self) -> float:
        raise NotImplementedError(
            "You have to implement the method calculate!")
