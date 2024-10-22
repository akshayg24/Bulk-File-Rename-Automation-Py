
import os
import csv

# Function to rename files according to the rules
def rename_files(directory, report_file):
    # List to hold the old and new names for reporting
    renamed_files = []
    
    # Loop through all the files in the directory
    for filename in os.listdir(directory):
        # Create full path for each file
        old_file_path = os.path.join(directory, filename)
        
        # Check if it is a file
        if os.path.isfile(old_file_path):
            # Create new filename
            new_filename = filename.lower().replace(' ', '-')
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            
            # Append old and new filenames to the list
            renamed_files.append([filename, new_filename])
    
    # Write the report to a CSV file
    with open(report_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Original Filename", "New Filename"])
        writer.writerows(renamed_files)
    
    print(f"Renaming completed! Report saved as '{report_file}'.")

# Usage Example
if __name__ == "__main__":
    directory = input("Enter the directory where the files are located: ")
    report_file = 'renaming_report.csv'
    
    rename_files(directory, report_file)
