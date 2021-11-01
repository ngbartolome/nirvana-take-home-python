from coalescer.models.criteria import Criteria

from coalescer.utils.math_util import get_max_value


class Max(Criteria):
    def calculate(self) -> float:
        return get_max_value(self.data)
