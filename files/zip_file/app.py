from pathlib import Path
from zipfile import ZipFile

#with ZipFile("file.zip" , "w") as zip:
#    for path in Path("zip_file\ecommerce").rglob("*.*"):
#       zip.write(path)


#with ZipFile("file.zip") as zip:
#   info =   zip.getinfo(zip.namelist()[0])
#   print(info.compress_size)


with ZipFile("file.zip") as zip:
    zip.extractall("Extract")