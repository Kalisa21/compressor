import os
import shutil
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    try:
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_filename = f"{folder_name}_{current_date}.{compress_type}"

        if compress_type == "zip":
            with zipfile.ZipFile(compressed_filename, "w") as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))
        elif compress_type == "tar":
            with tarfile.open(compressed_filename, "w") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        elif compress_type == "tgz":
            with tarfile.open(f"{compressed_filename}.tar.gz", "w:gz") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        else:
            print("Unsupported compression type.")
            return False

        print(f"Compression successful. Compressed file saved as {compressed_filename}")
        return True
    except Exception as e:
        print(f"Compression failed: {e}")
        return False

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    compress_types = ["zip", "tar", "tgz"]
    print("Available compress types:")
    for i, compress_type in enumerate(compress_types, 1):
        print(f"{i}. {compress_type}")

    compress_choice = int(input("Enter the number corresponding to the desired compress type: "))
    if compress_choice < 1 or compress_choice > len(compress_types):
        print("Invalid choice.")
        return

    selected_compress_type = compress_types[compress_choice - 1]
    compress_folder(folder_path, selected_compress_type)

if __name__ == "__main__":
    main()
