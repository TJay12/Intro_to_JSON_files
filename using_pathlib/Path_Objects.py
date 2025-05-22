import json
from pathlib import Path
# Common Things You Can Do with Path Objects

pathdir = Path("data")
pathfile = Path("data") / "examplefile.json"

pathfile.exists() # True if the file or directory exists
pathfile.is_file() # True if it's a file
pathfile.is_dir() # True if it's a directory
pathfile.name # full filename of file
pathfile.stem # file name
pathfile.suffix # file type
pathfile.parent # parent folder

print(f"\n{'-' * 34}")
print(f"{'.json file in data folder':^34}")
print(f"{'-' * 34}")
print(f"{'Name:':<17} {pathfile.name}")
print(f"{'File/Dir Exists:':<17} {pathfile.exists()}")
print(f"{'Is File:':<17} {pathfile.is_file()}")
print(f"{'Is Directory:':<17} {pathfile.is_dir()}")
print(f"{'Stem:':<17} {pathfile.stem}")
print(f"{'Suffix:':<17} {pathfile.suffix}")
print(f"{'Parent(folder):':<17} {pathfile.parent}")

print(f"\n{'-' * 23}")
print(f"{'data folder':^23}")
print(f"{'-' * 23}")
print(f"{'Name:':<17} {pathdir.name}")
print(f"{'File/Dir Exists:':<17} {pathdir.exists()}")
print(f"{'Is File:':<17} {pathdir.is_file()}")
print(f"{'Is Directory:':<17} {pathdir.is_dir()}")
print(f"{'Stem:':<17} {pathdir.stem}")
print(f"{'Suffix:':<17} {pathdir.suffix}")
print(f"{'Parent(folder):':<17} {pathdir.parent}")