from coalescer.models.criteria import Criteria

from coalescer.utils.math_util import get_average_value


class Average(Criteria):
    def calculate(self) -> float:
        return get_average_value(self.data)
