import gzip
import os
import datetime

def main():
    path = "/var/log"
    for file in os.listdir(path):
        if not file.endswith(".log"):
            continue

        paths = get_paths(path, file)

        with open(paths[0], "r") as f:
            with gzip.open(paths[1], "wt") as fgz:
                fgz.writelines(f)

        clear_file(paths[0])

def clear_file(path):
    open(path, "w").close()

def get_paths(path, file):
    paths = list()
    paths.append(path + "/" + file)
    paths.append(path + "/" + file + ".gz")
    return paths

if __name__ == "__main__":
    main()