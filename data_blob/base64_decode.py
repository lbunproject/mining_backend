import base64

def decode_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            decoded_line = base64.b64decode(line.strip()).decode()
            outfile.write(decoded_line + '\n')

# Usage
input_file = 'data_blob/data_blob.txt'  # Replace with your input file name
output_file = 'data_blob/decoded_output.txt'
decode_file(input_file, output_file)
