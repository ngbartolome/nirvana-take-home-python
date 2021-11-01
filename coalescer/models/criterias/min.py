from coalescer.models.criteria import Criteria

from coalescer.utils.math_util import get_min_value


class Min(Criteria):
    def calculate(self) -> float:
        return get_min_value(self.data)
