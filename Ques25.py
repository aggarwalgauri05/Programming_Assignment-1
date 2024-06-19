def copy_file(source_file, destination_file):
    try:
        with open('source_file.txt', 'r') as f_source:
            with open('destination_file.txt', 'w') as f_dest:
                for line in f_source:
                    f_dest.write(line)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage:
source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)
