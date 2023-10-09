from pathlib import Path

path = Path("path_basic\ecommerce\__init__.py")
#path2 = path.with_name("tex_number.txt")
path2 = path.with_suffix(".txt")

#print(path.exists())
#print(path.is_file())
#print(path.is_dir())
#print(path.absolute())
#print(path.name)
#print(path.parent)

print(path2)