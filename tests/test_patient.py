import faker
import os
import pytest
import responses
from http import HTTPStatus

from fastapi.testclient import TestClient

from coalescer.constants import endpoints
from coalescer.main import api

from coalescer.models.enums.criteria_types import CriteriaTypes

from coalescer.utils.format_util import get_formatted_response
from coalescer.utils.math_util import get_average_value, get_min_value, get_max_value

from tests.factories.patient_factory import get_mock_data

client = TestClient(api)
fake = faker.Faker()


class TestPatient():
    @pytest.fixture
    def dataset(self):
        return [get_mock_data(), get_mock_data(),
                get_mock_data()]

    @pytest.fixture
    def mocked_responses(self, dataset):
        with responses.RequestsMock() as mock:
            for index, data in enumerate(dataset, start=1):
                mock.add(
                    responses.GET, os.getenv(f'API_{index}_URL'),
                    json=data, status=HTTPStatus.OK)

            yield mock

    def test_missing_fields(self):
        response = client.get(endpoints.PATIENT)
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    def test_missing_criteria_field(self):
        response = client.get(
            endpoints.PATIENT, params={"member_id": fake.unique.random_int()})
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    def test_missing_member_id_field(self):
        response = client.get(
            endpoints.PATIENT, params={"criteria": CriteriaTypes.AVERAGE.value})
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    def test_patient_info_according_to_average_criteria(self, dataset, mocked_responses):
        response = client.get(
            endpoints.PATIENT, params={"member_id": fake.unique.random_int(), "criteria": CriteriaTypes.AVERAGE.value})

        assert response.status_code == HTTPStatus.OK
        assert response.json() == get_formatted_response(
            dataset, get_average_value)

    def test_patient_info_according_to_min_criteria(self, dataset, mocked_responses):
        response = client.get(
            endpoints.PATIENT, params={"member_id": fake.unique.random_int(), "criteria": CriteriaTypes.MIN.value})

        assert response.status_code == HTTPStatus.OK
        assert response.json() == get_formatted_response(
            dataset, get_min_value)

    def test_patient_info_according_to_max_criteria(self, dataset, mocked_responses):
        response = client.get(
            endpoints.PATIENT, params={"member_id": fake.unique.random_int(), "criteria": CriteriaTypes.MAX.value})

        assert response.status_code == HTTPStatus.OK
        assert response.json() == get_formatted_response(
            dataset, get_max_value)
