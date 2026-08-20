# 22. Rename files in a directory.

# Problem: Add a specific prefix to all .txt files in a directory.

import os

def rename_txt_files(directory, prefix):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, f"{prefix}_{filename}")
            os.rename(old_path, new_path)


print("Renamed .txt files in current directory with prefix 'new_'")