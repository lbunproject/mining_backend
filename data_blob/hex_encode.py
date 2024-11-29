def convert_to_hex(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            hex_representation = line.strip().encode('utf-8').hex()
            outfile.write(hex_representation + '\n')

# Usage
input_file = 'data_blob/kjv.csv'  # Replace with your input file name
output_file = 'data_blob/data_blob_hex.txt'
convert_to_hex(input_file, output_file)
