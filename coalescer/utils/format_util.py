from ..models.enums.patient_fields import PatientFields


def get_formatted_response(values: dict, strategy):
    response = dict()
    for field in PatientFields:
        data = []
        for value in values:
            data = [*data, value[field.value]]

        response[field.value] = strategy(data)

    return response
