from ..models.criteria import Criteria

from ..models.criterias.average import Average
from ..models.criterias.min import Min
from ..models.criterias.max import Max

from ..models.enums.criteria_types import CriteriaTypes


def get_criteria(criteria: CriteriaTypes, values: list) -> Criteria:
    if criteria == CriteriaTypes.AVERAGE:
        return Average(values)
    elif criteria == CriteriaTypes.MIN:
        return Min(values)
    elif criteria == CriteriaTypes.MAX:
        return Max(values)
    else:
        raise Exception("CRITERIA_NOT_VALID")
