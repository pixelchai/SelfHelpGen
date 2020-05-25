import os
import zipfile
from bs4 import BeautifulSoup

def process_epub(epub_path):
    out_path = os.path.join("data", "out", os.path.splitext(os.path.split(epub_path)[1])[0] + ".txt")
    epub = zipfile.ZipFile(epub_path, "r")

    with open(out_path, "w") as f:
        for epub_file in epub.filelist:
            file_name = epub_file.filename
            if os.path.splitext(file_name)[1] == ".html":
                soup = BeautifulSoup(epub.open(file_name))
                for elem in soup.select("p"):
                    f.write(elem.text)
                    f.write("\n")

if __name__ == '__main__':
    input("Press enter to begin processing epubs -- will overwrite txt files in data/out/")
    os.makedirs(os.path.join("data", "out"), exist_ok=True)

    raw_dir = os.path.join("data", "raw")
    for raw_file in os.listdir(raw_dir):
        raw_file_full = os.path.join(raw_dir, raw_file)
        if os.path.splitext(raw_file)[1] == ".epub":
            print("Doing {}".format(raw_file))
            process_epub(raw_file_full)
