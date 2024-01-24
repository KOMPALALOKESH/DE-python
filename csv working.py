import csv
import os

# reading csv file with normal version
with open('BPI-Sep2020.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f"""\t
                  Series reference: {row[0]}
                  Description: {row[1]}
                  Period: {row[2]}
                  Previously published: {row[3]}
                  revised: {row[4]}""")
            line_count += 1
            if line_count > 1:
                break
    print(f'Processed {line_count} lines.')

# reading csv file with dict version
with open('BPI-Sep2020.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f"""\t
                  Series reference: {row["Series reference"]}
                  Description: {row["Description"]}
                  Period: {row["Period"]}
                  Previously published: {row["Previously published"]}
                  revised: {row["Revised"]}""")
            line_count += 1
            if line_count > 1:
                break
    print(f'Processed {line_count} lines.')

# creating a employee csv file 
with open('emp_file1.csv', 'w') as csvfile:
    emp_writer = csv.writer(csvfile, delimiter=',') # csv writer
    emp_writer.writerow(['emp_id', 'name', 'dept'])
    emp_writer.writerow(['1', 'John', 'IT'])
    emp_writer.writerow(['2', 'Jane', 'HR'])

with open('emp_file2.csv', 'w') as csvfile:
    columns = ['emp_id', 'name', 'dept']
    emp_writer = csv.DictWriter(csvfile, fieldnames=columns) # csv Dict writer
    emp_writer.writeheader()
    emp_writer.writerow({'emp_id': 3, 'name': 'james', 'dept': 'IT'})
    emp_writer.writerow({'emp_id': 4, 'name': 'jane john', 'dept': 'HR talent'})