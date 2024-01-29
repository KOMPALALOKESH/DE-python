import json
import jsonschema
from jsonschema import validate

transaction_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "InvoiceNo": {"type": "integer"},
        "StockCode": {"type": "integer"},
        "Description": {"type": "string"},
        "Quantity": {"type": "integer"},
        "InvoiceDate": {"type": "string"},
        "UnitPrice": {"type": "number"},
        "CustomerID": {"type": "integer"},
        "Country": {"type": "string"},
    },
    "required": [
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "CustomerID",
        "InvoiceDate",
        "UnitPrice",
    ],
}

def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True

def validate_json_schema(json_data, schema=transaction_schema):
    """REF: https://json-schema.org/ """
    try:
        validate(json.loads(json_data), schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given json data is not valid."
        return False, err
    msg = "Given json data is valid."
    return True, msg


if __name__ == "__main__":
    
    with open('json working/data_subset.json', 'r') as json_file:
        data = json.load(json_file)
    valid_data = data[0]
    CustomerID_missing_dict = { 
        "InvoiceNo": 536370,
        "StockCode": 22492,
        "Description": "MINI PAINT SET VINTAGE",
        "Quantity": 36,
        "InvoiceDate": "12/1/2010 8:45",
        "UnitPrice": 0.65,
        "Country": "France"
    }

    ########### testing with inbuilt functions ###########
    ######################################################
    is_valid = validate(instance=valid_data, schema=transaction_schema)
    print(is_valid)
    is_valid = validate(instance=CustomerID_missing_dict, schema=transaction_schema)
    print(is_valid) # throws error as CustomerID is missing in CustomerID_missing_dict

    ########### testing with defined functions ###########
    ######################################################
    is_valid = validate_json(json.dumps(valid_data)) # checks the json format only
    print(is_valid)
    is_valid = validate_json(json.dumps(CustomerID_missing_dict)) # checks the json format only
    print(is_valid)
    is_valid, msg = validate_json_schema(json.dumps(valid_data)) # checks the json format and schema
    print(f'{is_valid} \n {msg}')
    is_valid, msg = validate_json_schema(json.dumps(CustomerID_missing_dict)) # checks the json format and schema
    print(f'{is_valid} \n {msg}')