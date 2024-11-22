import csv
import random
import string
import hashlib
from datetime import datetime, timedelta

def generate_secure_password(min_length, max_length):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_key(password):
    key = hashlib.sha256(password.encode()).hexdigest()  # 64-character hex representation of 32 bytes
    expanded_key = (key * 2)[:60]  # Expand and trim to 60 bytes
    return expanded_key

def generate_passwords_csv(min_length, max_length, start_date, num_days, output_file):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    data = []

    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        password = generate_secure_password(min_length, max_length)
        key = generate_password_key(password)
        data.append([current_date.strftime("%Y-%m-%d"), password, key])

    with open("./gen_keys/" + output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["date", "password", "key"])
        writer.writerows(data)

# Prompt the user for input
min_password_length = int(input("Enter minimum password length: "))
max_password_length = int(input("Enter maximum password length: "))
start_date = input("Enter start date (YYYY-MM-DD): ")
number_of_days = int(input("Enter number of days: "))
output_file = input("Enter output file name (e.g., keys.csv): ")

# Generate the CSV file
generate_passwords_csv(min_password_length, max_password_length, start_date, number_of_days, output_file)

print(f"File '{output_file}' generated successfully.")
