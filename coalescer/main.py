from dotenv import load_dotenv
from fastapi import FastAPI

from coalescer.constants import endpoints

from .models.enums.criteria_types import CriteriaTypes

from .services import patient_service

load_dotenv()

api = FastAPI()


@api.get(endpoints.PATIENT)
async def patient(member_id: int, criteria: CriteriaTypes):
    patient = await patient_service.get_coalesced_info(member_id, criteria)
    return patient
