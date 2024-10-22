Python File Renaming Script

This script renames files in a specified directory by:
1. Replacing spaces with hyphens (`-`).
2. Converting filenames to lowercase.
3. Creating a report with the original and new filenames in CSV format.

Prerequisites
1. Install Python

Make sure you have Python 3.x installed on your system. You can download Python from the official website: 
https://www.python.org/downloads/.

Windows Installation Instructions:

- Download the Python installer for Windows from the link above.
- Run the installer and make sure to check the box that says "Add Python to PATH" during installation.
- After installation, open Command Prompt and type:

python --version
This should display the installed Python version.
2. Verify pip (Python Package Manager)

pip should be installed automatically with Python. Verify its installation by typing:

pip --version

If pip is not installed, you can manually install it by following the instructions 
here: https://pip.pypa.io/en/stable/installation/.

How to Use the Script
1. Clone or Download the Script

Download the rename_files_script.py file or clone this repository if you are working from a version control system.

2. Place the Script in Your Working Directory
Place the rename_files_script.py file in the directory where your files are located, or place it in any convenient location on your system.
3. Modify the Script (Optional)

By default, the script will prompt you to input the directory path where your files are located. If you want to automate this further, you can modify the following line to hard-code your directory path:

directory = "C:/path/to/your/folder"

4. Running the Script

On Windows:
1. Open Command Prompt.
2. Navigate to the folder where the script is saved using the cd command. For example:

cd C:\path\to\your\script
3. Run the script by typing:
python rename_files_script.py
4. When prompted, enter the directory where your files are located. For example:

Enter the directory where the files are located: C:\Users\yourusername\Documents\files

On macOS/Linux:

1. Open Terminal.
2. Navigate to the folder where the script is saved using the cd command.
3. Run the script:
python3 rename_files_script.py

5. Output

- The script will rename all files in the specified directory by:
  - Converting filenames to lowercase.
  - Replacing spaces with hyphens.
- It will generate a report called renaming_report.csv in the same directory, detailing the old and new filenames.

Troubleshooting
Issue: Python was not found Error

If you receive the error Python was not found, ensure that Python is correctly installed and added to the system PATH.

To Check Python Installation:

1. Open Command Prompt.
2. Run:
python --version

If you get an error, try the following:
- Verify that Python is installed in C:\Users\YourUsername\AppData\Local\Programs\Python\PythonXX\.
- Add the Python path to your system PATH manually by following these steps:
  - Press Windows + X → Select System → Advanced system settings → Environment Variables → Edit Path.
  - Add the Python folder path and the Scripts folder.

Issue: Execution Policy Error (Windows PowerShell)

If you get an execution policy error when running the script via PowerShell, you can temporarily allow script execution by running the following command:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


