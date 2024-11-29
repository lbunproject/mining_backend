import base64

def encode_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            encoded_line = base64.b64encode(line.strip().encode()).decode()
            outfile.write(encoded_line + '\n')

# Usage
input_file = 'data_blob/kjv.csv'  # Replace with your input file name
output_file = 'data_blob/data_blob.txt'
encode_file(input_file, output_file)