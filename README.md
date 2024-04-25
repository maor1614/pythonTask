JSON Validation Project
This project is a Python script designed to validate JSON files against a predefined schema. It ensures that JSON data used in applications adheres to expected formats, enhancing data integrity and reliability in development environments.

Features
Schema Validation: Uses the jsonschema library to validate JSON files against a user-defined schema.
Error Reporting: Provides detailed reports of validation errors, helping developers quickly identify and correct data issues.
Flexibility: Allows validation of any JSON file against any schema, specified via command-line arguments or hardcoded paths.
Prerequisites
Before running the script, you need to have Python installed on your machine. The script has been tested with Python 3.7 and above. Additionally, you need to install the jsonschema library, which can be done via pip:

bash
Copy code
pip install jsonschema
Installation
Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/yourusername/json-validation-project.git
cd json-validation-project
Usage
The script can be run from the command line, and it takes two arguments: the path to the schema JSON file and the path to the data JSON file.

Running the Script
To validate a JSON file against a schema, run:

bash
Copy code
python validate.py <path_to_schema.json> <path_to_data.json>
For example:

bash
Copy code
python validate.py C:\Users\maors\PycharmProjects\AppiumSandbox\pythonProject\pythonTask\pythonTask\schema.json C:\Users\maors\PycharmProjects\AppiumSandbox\pythonProject\pythonTask\pythonTask\data.json
Example Schema and Data Files
Ensure your schema and data JSON files are properly set up. Refer to the example schema and JSON data provided in the examples folder.
