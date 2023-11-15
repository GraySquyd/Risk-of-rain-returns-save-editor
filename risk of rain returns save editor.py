import tkinter as tk
from tkinter import filedialog

def read_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None

data = read_file_content("all flags.txt")

def insert_after_keyword(source_file, destination_file, keyword, new_string):
    try:
        # Create the source file if it doesn't exist yet
        with open(source_file, 'a') as file:
            file.write("")  # Write an empty string to create the file

        # Read the content of the source file
        with open(source_file, 'r') as file:
            source_content = file.read()

        # Find the location of the keyword
        keyword_index = source_content.find(keyword)

        if keyword_index != -1:
            # Insert the new string after the keyword
            modified_content = (
                source_content[:keyword_index + len(keyword)] +
                new_string +
                source_content[keyword_index + len(keyword):]
            )

            # Write the modified content to the destination file
            with open(destination_file, 'w') as file:
                file.write(modified_content)
            print("Operation successful: The new string has been inserted after the keyword.")
        else:
            print("Keyword not found in the source file.")
    except FileNotFoundError:
        print(f"The file {source_file} could not be created or found.")

def choose_source_file():
    file_source = filedialog.askopenfilename(title="Choose the source file", filetypes=[("JSON files", "*.json")])
    entry_source.delete(0, tk.END)
    entry_source.insert(0, file_source)

def choose_destination_folder():
    folder_destination = filedialog.askdirectory(title="Choose the destination folder")
    entry_destination.delete(0, tk.END)
    entry_destination.insert(0, folder_destination)

def execute_program():
    file_source = entry_source.get()
    folder_destination = entry_destination.get()
    keyword = '"flags":['

    file_content = read_file_content(file_source)

    if file_content is not None:
        file_destination = f"{folder_destination}/save.json"
        new_string = data

        insert_after_keyword(file_source, file_destination, keyword, new_string)

# Creating the graphical interface
window = tk.Tk()
window.title("Risk of Rain Returns Save Editor")

# Widgets
label_source = tk.Label(window, text="Save file:")
entry_source = tk.Entry(window, width=40)
button_choose_source = tk.Button(window, text="Choose", command=choose_source_file)

label_destination = tk.Label(window, text="Output:")
entry_destination = tk.Entry(window, width=40)
button_choose_destination = tk.Button(window, text="Choose", command=choose_destination_folder)

button_execute = tk.Button(window, text="Execute", command=execute_program)

# Placing the widgets
label_source.grid(row=0, column=0, padx=5, pady=5)
entry_source.grid(row=0, column=1, padx=5, pady=5)
button_choose_source.grid(row=0, column=2, padx=5, pady=5)

label_destination.grid(row=1, column=0, padx=5, pady=5)
entry_destination.grid(row=1, column=1, padx=5, pady=5)
button_choose_destination.grid(row=1, column=2, padx=5, pady=5)

button_execute.grid(row=3, column=0, columnspan=3, pady=10)

# Launching the main loop
window.mainloop()
