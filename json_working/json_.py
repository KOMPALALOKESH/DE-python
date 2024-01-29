import json
from pprint import pprint 

with open('json working/data_subset.json', 'r') as json_file:
    data = json.load(json_file)  # json file to python object
pprint(data) # prints pettely with proper indents when working with json files
# print(data)

json_formatted_str = json.dumps(data, indent=4)  # python object to json string
print(f'{json_formatted_str} \n {type(json_formatted_str)}')

transaction_list_of_dicts = json.loads(json_formatted_str)  # json string to python object
pprint(transaction_list_of_dicts[0].keys())  # prints the keys of the first dictionary in the list
print(transaction.get['InvoiceNo'] 
      for transaction in transaction_list_of_dicts)  # prints the InvoiceNo of each transaction in the list

update_dict = {
    'Country': 'India',
    'CustomerID': 11111,
    'Description': 'MINI PAINT SET VINTAGE',
    'InvoiceDate': '12/1/2010 8:45',
    'InvoiceNo': 111111,
    'Quantity': 36,
    'StockCode': 22492,
    'UnitPrice': 0.65
}
for transaction in transaction_list_of_dicts:
    if transaction.get('CustomerID') == 12583:
        transaction.update(update_dict)
        break
pprint(transaction_list_of_dicts)

with open('json working/data_dumped.json', 'w') as json_file:
    json.dump(transaction_list_of_dicts, json_file, indent=4)  # python object to json file