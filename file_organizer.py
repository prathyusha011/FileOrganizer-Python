import os
import shutil

def organize_files(source_folder):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.txt', '.docx', '.doc'],
        'PDFs': ['.pdf'],
        'Music': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Code': ['.py', '.js', '.cpp', '.java'],
    }

    files = os.listdir(source_folder)

    for file in files:
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            moved = False

            for folder_name, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(source_folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(source_folder, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))

    print("✅ All files organized successfully!")

if __name__ == "__main__":
    folder_input = input("Enter full path of folder to organize: ").strip()
    if os.path.exists(folder_input):
        organize_files(folder_input)
    else:
        print("❌ Folder not found. Please check the path again.")
