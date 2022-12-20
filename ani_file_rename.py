import os
from pathlib import Path
import re
import shutil

BASE_DIR = Path(__file__).resolve().parent

# BASE_DIR = "W:\HDD1\Ani"

print(BASE_DIR)


def main():
    for root, dirs, files in os.walk(BASE_DIR):
        # print("root" + str(root))
        # print("dirs🥎" + str(dirs))
        # print("files🧧" + str(files))
        if len(files) > 0:
            # print("🎇")
            for file in files:  # [ 3 , ani_file_rename ]
                # print(file + "🎁")
                origin_name = file
                ext = os.path.splitext(file)[1]
                # print(origin_name.split(" ", 1)[0])
                if (
                    origin_name.split(" ", 1)[0] == "[Ohys-Raws]"
                    or origin_name.split(" ", 1)[0] == "[SubsPlease]"
                ):
                    new_name = origin_name.split(" ", 1)[1]
                    new_name = remove_dash(new_name)
                    try:
                        new_name = (
                            re.search(r".+?\s\-\s[0-9\sOVAEND\.]+", new_name)
                            .group(0)
                            .strip()
                        ) + ext
                        rename_file(root, origin_name, new_name)
                        # print(new_name)
                    except Exception:
                        print("🧧" + origin_name)
                        pass
                # print((new_name))


def rename_file(root, origin_name, new_name):
    old_file_name = os.path.join(root, origin_name)
    new_file_name = os.path.join(root, new_name)
    print(f"💥{origin_name}\n → 🌟{new_name}")
    shutil.move(old_file_name, new_file_name)


def count_dash(name):
    dash_count = len(re.findall(" - ", name))
    return dash_count


def remove_dash(name):
    if count_dash(name) > 1:
        result = re.sub(" - ", "-", name, 1)
        # print(result)
        return remove_dash(result)
    else:
        # print("===========" + name)
        return name


def close_window():
    input("종료하려면 엔터를 입력하세요")


if __name__ == "__main__":
    main()
    close_window()
