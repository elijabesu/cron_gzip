import gzip
import os
import datetime

def main():
    path = "/var/log"
    for file in os.listdir(path):
        if not file.endswith(".log"):
            continue

        file_name = split_file_name(file)
        paths = get_paths(path, file_name)

        with open(paths[0], "r") as f:
            with gzip.open(paths[1], "wt+") as fgz:
                fgz.writelines(f)

        clear_file(paths[0])

def clear_file(path):
    open(path, "w").close()

def split_file_name(file):
    file_name = list()
    file_name = file.split(".")
    return file_name

def get_paths(path, file_name):
    paths = list()
    path_file_name = [path + "/" + file_name[0], "." + file_name[1]]
    paths.append(path_file_name[0] + path_file_name[1])
    paths.append(path_file_name[0] + "_" + str(datetime.date.today()) + path_file_name[1] + ".gz")
    return paths

if __name__ == "__main__":
    main()