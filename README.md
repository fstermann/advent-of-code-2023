# advent-of-code

[adventofcode](https://adventofcode.com/2023)

## Setup
```bash
pip install poetry
poetry install
pre-commit install
```

For each day, copy the template folder [`day00`](day00) and rename it to the given day.
Copy the input data from each challenge into the `input.txt` file.
For each part, copy the test data into the predefined variables:
```python
INPUT = """\

"""
EXPECTED = 0
```

Implement your solution in the `run` function:
```python
def run(input_: str) -> int:
    return 0
```

## Usage

Run the tests:
```bash
poetry run pytest day00/part1.py
poetry run pytest day00/part2.py
```

Run solutions for the input data:
```bash
poetry run python day00/part1.py
poetry run python day00/part2.py
```
