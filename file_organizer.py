import os
import shutil

# Jis folder ko organize karna hai
SOURCE_FOLDER = "Test_Files"

# File extensions ke hisaab se folders
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "ZIP_Files": [".zip", ".rar", ".7z"]
}

for file_name in os.listdir(SOURCE_FOLDER):

    file_path = os.path.join(SOURCE_FOLDER, file_name)

    # Sirf files ko process karo
    if not os.path.isfile(file_path):
        continue

    extension = os.path.splitext(file_name)[1].lower()

    category = None

    for folder, extensions in file_categories.items():
        if extension in extensions:
            category = folder
            break

    # Unknown file type
    if category is None:
        category = "Others"

    # Destination folder
    destination_folder = os.path.join(SOURCE_FOLDER, category)

    # Folder nahi hai to create karo
    os.makedirs(destination_folder, exist_ok=True)

    # File ko move karo
    destination = os.path.join(destination_folder, file_name)

    shutil.move(file_path, destination)

    print(f"Moved: {file_name} → {category}")

print("\nFile organization complete!")