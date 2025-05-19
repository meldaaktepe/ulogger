import os
try:
    with open("./VERSION", "r", encoding="utf-8") as version_file:
        __version__ = version_file.read().strip()
        print(__version__)
except FileNotFoundError as ex:
    print("File VERSION does not exist.")
