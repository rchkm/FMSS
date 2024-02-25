import loadStaffData
import calculateMetrics
import generateHTML
import saveHTML

def main():
    # directory paths
    directory_input = '/Users/weare/Documents/Sports Interactive/Football Manager 2024/fm data python/data input'
    directory_output = '/Users/weare/Documents/Sports Interactive/Football Manager 2024/fm data python/output'

    # get user input for output name
    custom_filename = input("Enter the desired output filename (without extension): ").strip()
       
    # load staff data
    try:     
        file_name = input("Enter the input filename (without extension): ").strip()
        staff_rawdata = loadStaffData.load_staff_data(directory_input, file_name)
        
        # calculate metrics
        staff = calculateMetrics.calculate_metrics(staff_rawdata)

        # generate html
        html = generateHTML.generate_html(staff)

        # save html
        saveHTML.save_html(html, directory_output, custom_filename)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()