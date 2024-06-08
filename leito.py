import csv

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Use a função
read_csv_file('movies.csv')
