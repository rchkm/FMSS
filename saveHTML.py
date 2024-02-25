import os

def save_html(html, directory_output, custom_filename):
    # generates file path for write-out of html file
    file_output_path = os.path.join(directory_output, custom_filename + ".html")
    # write HTML to file
    with open(file_output_path, "w", encoding="utf-8") as file:
        file.write(html)
    print(f"HTML file generated at: {file_output_path}")