import sys

def reverse_cipher(input_text):
  return input_text[::-1]

def load_file(input_filename,output_filename):
  try:
        # Read the original file
        with open(input_filename, 'r') as file:
            original_data = file.read()

        reversed_data = reverse_cipher(original_data)
        with open(output_filename, 'w') as file:
            file.write(reversed_data)
        print(f"File '{output_filename}' created successfully with reversed content.")
  except FileNotFounError:
        print(f'Error: File {input_filename} not found')
  except Exception as e:
        print(f'Error: {e}')
  

