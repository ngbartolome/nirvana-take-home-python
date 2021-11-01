import asyncio

from ..models.enums.criteria_types import CriteriaTypes
from ..models.enums.patient_fields import PatientFields

from .criteria_service import get_criteria
from .third_party.api_1_service import API1Service
from .third_party.api_2_service import API2Service
from .third_party.api_3_service import API3Service


async def get_info_from_APIs(member_id: int) -> dict:
    results = await asyncio.gather(API1Service().get_patient(member_id), API2Service().get_patient(member_id), API3Service().get_patient(member_id))

    values = dict()
    for field in PatientFields:
        values[field.value] = []

    for result in results:
        for field in PatientFields:
            values[field.value] = [
                *values[field.value], result[field.value]]

    return values


async def get_coalesced_info(member_id: int, criteria_type: CriteriaTypes) -> dict:
    try:
        data = await get_info_from_APIs(member_id)

        response = {}
        for field in PatientFields:
            response = {
                **response,
                field: get_criteria(
                    criteria_type, data[field.value]).calculate()
            }

        return response
    except Exception as e:
        raise Exception(f'GET_COALESCED_INFO: {e}')
