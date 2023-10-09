from pathlib import Path

#path = Path("WORK_WITH_Directory.py\ecommerce2")
#print(path.mkdir())
#print(path.rmdir())

#path = Path("WORK_WITH_Directory.py\ecommerce")
#paths = [p for p in path.iterdir() if p.is_dir]

#print(paths)


#path = Path("WORK_WITH_Directory.py\ecommerce")
#py_files = [p for p in path.glob("**/*.py")]

#print(py_files)

path = Path("WORK_WITH_Directory.py\ecommerce")
py_files = [p for p in path.rglob("*.py")]

print(py_files)