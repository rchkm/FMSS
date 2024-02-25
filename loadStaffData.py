import pandas as pd
import glob
import os

def load_staff_data(directory_input, file_name):
    # Get a list of HTML files in the specified directory
    list_of_files = glob.glob(os.path.join(directory_input, '*.html'))

    # Extract only the filenames without the directory path and extension
    file_names = [os.path.basename(file)[:-5] for file in list_of_files]

    # Check if the entered filename exists in the list of file names
    if file_name in file_names:
        file_input_path = os.path.join(directory_input, file_name + '.html')  # Construct the full path of the HTML file
        staff_rawdata_list = pd.read_html(file_input_path, header=0, encoding="utf-8", keep_default_na=False)  # Read HTML data into a list of DataFrame objects
        print("File found and data loaded successfully.")
        return staff_rawdata_list[0]
    else:
        raise FileNotFoundError("File not found.")