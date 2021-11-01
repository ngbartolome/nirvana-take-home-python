import faker

from coalescer.models.enums.patient_fields import PatientFields

fake = faker.Faker()


def get_mock_data() -> dict:
    values = dict()
    for field in PatientFields:
        values[field.value] = fake.unique.random_int()

    return values
