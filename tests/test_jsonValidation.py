import json
import pytest

from jsonschema import validate
from json_working.json_validation import validate_json, validate_json_schema


class Test_JSONValidation:
    # def __init__(self): # should not be declared __init__ method in class in a package already __init__.py file is declared in package
    #     pass

    def test_validate_json_should_return_true_when_valid_json_string(self):
        # Arrange
        json_string = """[
            {
                "InvoiceNo": 536370, 
                "StockCode": 22492, 
                "Description": "MINI PAINT SET VINTAGE", 
                "Quantity": 36, 
                "InvoiceDate": "12/1/2010 8:45", 
                "UnitPrice": 0.65, 
                "CustomerID": 12583, 
                "Country": "France"
            }, 
            {
                "InvoiceNo": 536372, 
                "StockCode": 22632, 
                "Description": "HAND WARMER RED POLKA DOT", 
                "Quantity": 6, 
                "InvoiceDate": "12/1/2010 9:01", 
                "UnitPrice": 1.85, 
                "CustomerID": 17850, 
                "Country": "United Kingdom"
            }, 
            {
                "InvoiceNo": 536389, 
                "StockCode": 22727, 
                "Description": "ALARM CLOCK BAKELIKE RED", 
                "Quantity": 4, 
                "InvoiceDate": "12/1/2010 10:03", 
                "UnitPrice": 3.75, 
                "CustomerID": 12431, 
                "Country": "Australia"
            }, 
            {
                "InvoiceNo": 562106, 
                "StockCode": 22993, 
                "Description":"SET OF 4 PANTRY JELLY MOULDS", 
                "Quantity": 1, 
                "InvoiceDate": "8/2/2011 15:19", 
                "UnitPrice": 1.25, 
                "CustomerID": 14076, 
                "Country": "United Kingdom"
            }
        ]"""
        # Act
        is_valid_json = validate_json(json_string)
        # Assert
        assert is_valid_json is True

    def test_validate_json_should_return_false_when_invalid_json_string(self):
        # Arrange
        invalid_json_string = """{
            "InvoiceNo": 536370 
            "StockCode": 22492, 
            "Description":  "MINI PAINT SET VINTAGE", 
            "Quantity": 36, 
            "InvoiceDate": "12/1/2010 8:45", 
            "UnitPrice": 0.65, 
            "CustomerID": 12583, 
            "Country": "France"
        }"""
        # Act
        is_valid_json = validate_json(invalid_json_string)
        # Assert
        assert is_valid_json is False

    def test_validate_json_schema_should_return_true_when_valid_json_string(self):
        # Arrange
        valid_json_schema = {
            "InvoiceNo": 536370,
            "StockCode": 22492,
            "Description": "MINI PAINT SET VINTAGE",
            "Quantity": 36,
            "InvoiceDate": "12/1/2010 8:45",
            "UnitPrice": 0.65,
            "CustomerID": 12583,
            "Country": "France"
        }

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
                "Country": {"type": "string"}
            },
            "required": [
                "InvoiceNo",
                "StockCode",
                "Quantity",
                "CustomerID",
                "InvoiceDate",
                "UnitPrice"
            ]
        }
        # Act
        is_valid_json_schema, message = validate_json_schema(json.dumps(valid_json_schema), transaction_schema)
        # Assert
        assert is_valid_json_schema is True
        assert message == "Given json data is valid."

    def test_validate_json_schema_should_return_false_when_invalid_json_string(self):
        # Arrange
        #InvoiceNo is string instead of int
        InvoiceNo_is_a_string = {
            "InvoiceNo": "536370",
            "StockCode": 22492,
            "Description": "MINI PAINT SET VINTAGE",
            "Quantity": 36,
            "InvoiceDate": "12/1/2010 8:45",
            "UnitPrice": 0.65,
            "CustomerID": 12583,
            "Country": "France"
        }

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
                "Country": {"type": "string"}
            },
            "required": [
                "InvoiceNo",
                "StockCode",
                "Quantity",
                "CustomerID",
                "InvoiceDate",
                "UnitPrice"
            ]
        }
        # Act
        is_valid_json_schema, message = validate_json_schema(json.dumps(InvoiceNo_is_a_string), transaction_schema)
        # Assert
        assert is_valid_json_schema == False
        assert message == "Given json data is not valid."

        # this test only runs if the pytest.ini has the *_test set
    
    def run_validate_json_schema_Should_return_True_when_valid_json_schema_test(self):
        # Arrange
        valid_json_schema = {
            "InvoiceNo": 536370,
            "StockCode": 22492,
            "Description": "MINI PAINT SET VINTAGE",
            "Quantity": 36,
            "InvoiceDate": "12/1/2010 8:45",
            "UnitPrice": 0.65,
            "CustomerID": 12583,
            "Country": "France"
        }

        transaction_schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "InvoiceNo": {
                    "type": "integer"
                },
                "StockCode": {
                    "type": "integer"
                },
                "Description": {
                    "type": "string"
                },
                "Quantity": {
                    "type": "integer",
                },
                "InvoiceDate": {
                    "type": "string"
                },
                "UnitPrice": {
                    "type": "number"
                },
                "CustomerID": {
                    "type": "integer"
                },
                "Country": {
                    "type": "string"
                }
            },
            "required": [
                "InvoiceNo",
                "StockCode",
                "Quantity",
                "CustomerID",
                "InvoiceDate",
                "UnitPrice"

            ]
        }

        # Act
        is_valid_json_schema, message = validate_json_schema(json.dumps(valid_json_schema), transaction_schema)
        # Assert
        assert is_valid_json_schema == True
        assert message == "Given json data is valid."