import csv
import random
import string
import binascii
from datetime import datetime, timedelta
import os

def generate_secure_key(length=60):
    """
    Generates a secure random key of a specified byte length.

    Parameters:
        length (int): The exact byte length of the key to generate. Default is 60 bytes.

    Returns:
        str: A securely generated random key consisting of ASCII letters, digits, and punctuation.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    # Ensure that each character is one byte in UTF-8
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

def convert_to_hex(key):
    """
    Converts a string key to its hexadecimal representation.

    Parameters:
        key (str): The key string to convert.

    Returns:
        str: The hexadecimal representation of the key.
    """
    hex_representation = key.encode('utf-8').hex()  # Convert key to hexadecimal
    return hex_representation

def generate_keys_csv(start_date, num_days, output_file, key_length=60):
    """
    Generates a CSV file containing dates, keys, and their hexadecimal representations.

    Parameters:
        start_date (str): The start date in "YYYY-MM-DD" format.
        num_days (int): The number of consecutive days to generate keys for.
        output_file (str): The name of the output CSV file.
        key_length (int): The exact byte length of each key. Default is 60 bytes.
    """
    # Parse the start date
    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        print("Error: Start date must be in YYYY-MM-DD format.")
        return

    data = []

    for i in range(num_days):
        current_date = start_date_obj + timedelta(days=i)
        key = generate_secure_key(length=key_length)
        hex_key = convert_to_hex(key)  # Convert the key to hex
        data.append([current_date.strftime("%Y-%m-%d"), key, hex_key])

    # Ensure the output directory exists
    output_dir = "./gen_keys/"
    os.makedirs(output_dir, exist_ok=True)

    # Write to the CSV file
    with open(os.path.join(output_dir, output_file), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["date", "key", "hex_key"])  # Header
        writer.writerows(data)

    print(f"File '{output_file}' generated successfully in '{output_dir}' directory.")

def main():
    """
    Main function to execute the key generation process.
    """
    print("=== Secure Key Generation ===")
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()

    # Number of days to generate keys for
    while True:
        try:
            number_of_days = int(input("Enter number of days: ").strip())
            if number_of_days <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer for the number of days.")

    output_file = input("Enter output file name (e.g., keys_hex.csv): ").strip()

    # Generate the CSV file with exactly 60-byte keys
    generate_keys_csv(start_date, number_of_days, output_file, key_length=60)

if __name__ == '__main__':
    main()