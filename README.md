# Nirvana Take Home Python

Gets patient data from multiple APIs and coalesces the responses according to a configurable strategy.

Receives two query parameters:

- member_id
- criteria

Request example: `GET http://localhost:8000/patient?member_id=1&criteria=min`

The possible criterias are 'average', 'min', and 'max'.

It allows adding a new one.

## Requirements

### Python

- Python 3.6 or higher

## Installation

Create the `.env` file on the `project root`: please verify required environment variables at [.env.example](.env.example).

Run the following commands to enable the virtual env and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Running

Start server watching for file changes and reloading automatically using `uvicorn`:

```bash
uvicorn coalescer.main:api --reload
```

_Note:_ APIs should return correct JSON data

## Tests

Running test suite with [pytest](https://pytest.org/):

```bash
pytest
```

## Adding a new Criteria

If you want to add new Criteria, you should follow these instructions:

- Create a new criteria class in `coalescer/models/criterias` folder. It must extend the Criteria class and override the calculate method.
- Add a key in `coalescer/models/enums/criteria_types.py` file.
- Add a rule in `coalescer/services/criteria_service.py` file.
- Send it as "criteria" query parameter.

## License

[MIT](https://choosealicense.com/licenses/mit/)
