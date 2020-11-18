import zipfile
import re
import os

class TextLoader:
    def __init__(self, path):
        if os.path.exists(path):
            os.path.normcase(path)
            self.__folder_name = os.path.split(path)[1].rsplit(".", 1)[0]

            zip_file = zipfile.ZipFile(path)
            zip_file.extractall("./extracted")
            zip_file.close()

            self.__files_path = os.path.join("./extracted", self.__folder_name)
            self.__files = [file for file in os.listdir(self.__files_path)
                            if os.path.isfile(os.path.join(self.__files_path, file))]
            self.__iterable_files = iter(self.__files)

        else:
            raise IOError("non-existent path")

    def __len__(self):
        return len(self.__files)

    def ration(txt):
        return re.sub(r"[.,!?;:-]", " ", txt).lower()

    def __iter__(self):
        return self

    def __next__(self):
        file = next(self.__iterable_files)
        current_path = os.path.join(self.__files_path, file)

        with open(current_path, "r", encoding = "utf-8") as file:
            text = TextLoader.ration(file.read())

        with open(current_path, "w", encoding = "utf-8") as file:
            file.write(text)

        return open(current_path, "r", encoding = "utf-8")
"""
if __name__ == "__main__":
    text = TextLoader("D:\Программы\MIPT_advanced_python_fall\w9\sample.zip")
    for file in text:
        print(file.read())
"""
