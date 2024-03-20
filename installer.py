import zipfile
import os
import subprocess

def extract_zip_with_password(zip_file_to_extract, extract_dir):
    zip_password = input("Enter the password: ")
    try:
        with zipfile.ZipFile(zip_file_to_extract, 'r') as zip_ref:
            zip_ref.extractall(extract_dir, pwd=zip_password.encode())
        print(f"Extracted '{zip_file_to_extract}' successfully.")
        file_path = os.path.join(extract_dir, "r.txt")
        try:
            subprocess.run(['pip', 'install', '-r', file_path], check=True)
            print("Requirements installed successfully.")
            print("\n Run python main.py to start the toolkit")
            input("\n Press Any key To continue")
            os.remove(file_path)
            os.remove(zip_file_to_extract)
            
        except subprocess.CalledProcessError as e:
            print(f"Error installing requirements: {e}")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nPlease purchase a genuine copy from @n7oue...")
        input("\nPress any key to continue...")

# Example usage
zip_file_to_extract = os.path.join(os.getcwd(), 'data.zip')
extract_directory = os.getcwd()

extract_zip_with_password(zip_file_to_extract, extract_directory)
