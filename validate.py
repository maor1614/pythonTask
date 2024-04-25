import json
from jsonschema import validate, ValidationError


def load_json(filename):
    """ Load the JSON data from a file """
    with open(filename, 'r') as file:
        return json.load(file)


def validate_json(data, schema):
    """ Validate JSON data against the schema """
    try:
        validate(instance=data, schema=schema)
        return True, "No validation errors found."
    except ValidationError as ve:
        return False, ve


def main():
    # Load the schema
    schema = load_json('schema.json')

    # Load the JSON data file you want to validate
    data = load_json('data.json')

    # Validate the data
    is_valid, message = validate_json(data, schema)
    if is_valid:
        print("Validation successful.")
    else:
        print("Validation failed with errors:")
        print(message)


if __name__ == "__main__":
    main()
