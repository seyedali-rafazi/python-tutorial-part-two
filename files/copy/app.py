from pathlib import Path
import shutil

source = Path("copy\ecommerce\__init__.py")
target = Path() / "__init__.py"


shutil.copy(source , target)