def convert_from_hex(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            text_representation = bytes.fromhex(line.strip()).decode('utf-8')
            outfile.write(text_representation + '\n')

# Usage
input_file = 'data_blob/data_blob_hex.txt'  # Replace with your hex file name
output_file = 'data_blob/data_blob_text.txt'
convert_from_hex(input_file, output_file)
