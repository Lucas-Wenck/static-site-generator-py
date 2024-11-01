import os
import shutil
from copying import content_copy

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    print("Copying files from static to public")
    content_copy("./static", "./public")

main()