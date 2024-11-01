import os
import shutil

def content_copy(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for file in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            content_copy(from_path, dest_path)
            