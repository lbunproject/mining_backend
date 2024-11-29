import csv
import random
import string
import hashlib
from datetime import datetime, timedelta

def generate_secure_key(min_length, max_length):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

def convert_to_hex(key):
    hex_representation = key.encode('utf-8').hex()  # Convert key to hexadecimal
    return hex_representation

def generate_keys_csv(min_length, max_length, start_date, num_days, output_file):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    data = []

    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        key = generate_secure_key(min_length, max_length)
        hex_key = convert_to_hex(key)  # Convert the key to hex
        data.append([current_date.strftime("%Y-%m-%d"), key, hex_key])

    with open("./gen_keys/" + output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["date", "key", "hex_key"])  # Added "hex_key" to header
        writer.writerows(data)

# Prompt the user for input
min_key_length = int(input("Enter minimum key length: "))
max_key_length = int(input("Enter maximum key length: "))
start_date = input("Enter start date (YYYY-MM-DD): ")
number_of_days = int(input("Enter number of days: "))
output_file = input("Enter output file name (e.g., keys_hex.csv): ")

# Generate the CSV file
generate_keys_csv(min_key_length, max_key_length, start_date, number_of_days, output_file)

print(f"File '{output_file}' generated successfully.")
