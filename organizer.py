import os
import shutil

# Define where your files are located
source_folder = '/path/to/your/folder'  # Update this path

# List of file extensions and corresponding folders
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'Code': ['.py', '.js', '.html', '.css']
}

def organize_files():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)

            moved = False
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    folder_path = os.path.join(source_folder, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(source_folder, 'Others')
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, filename))

if __name__ == "__main__":
    organize_files()
    print("Files organized successfully!")
