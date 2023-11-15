ef read_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None

# Example of usage
file_name = 'all flags.txt'
file_content = read_file_content(file_name)


def insert_after_keyword(source_file, destination_file, keyword, new_string):
    try:
        # Create the source file if it doesn't exist yet
        with open(source_file, 'a') as file:
            file.write("")  # Write an empty string to create the file

        # Read the content of the source file
        with open(source_file, 'r') as file:
            source_content = file.read()

        # Find the location of the keyword
        index_keyword = source_content.find(keyword)

        if index_keyword != -1:
            # Insert the new string after the keyword
            modified_content = (
                source_content[:index_keyword + len(keyword)] +
                new_string +
                source_content[index_keyword + len(keyword):]
            )
            
            # Write the modified content to the destination file
            with open(destination_file, 'w') as file:
                file.write(modified_content)
            print("Operation successful: The new string has been inserted after the keyword.")
        else:
            print("Keyword not found in the source file.")
    except FileNotFoundError:
        print(f"The file {source_file} could not be created or found.")

# Example of usage
source_file = 'source.json'
destination_file = 'save.json'
keyword = '"flags":['
new_string = file_content

insert_after_keyword(source_file, destination_file, keyword, new_string)
