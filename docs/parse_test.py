# Exploring the file system

from processhtml import *
import os

if __name__ == "__main__":
        for root, dirs, files in os.walk("../pages/www.imdb.com/title/"):
                for name in files:
                        if name.endswith((".html", ".htm")):
                                print html_to_data(os.path.join(root, name))

