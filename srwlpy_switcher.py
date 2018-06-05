import os, sys, shutil
from orangecanvas import resources

if "darwin" in sys.platform:
    platform = "darwin"
    file     = "srwlpy.so"
elif "linux" in sys.platform:
    platform = "linux"
    file     = "srwlpy.so"
elif "win" in sys.platform:
    platform = "windows"
    file     = "srwlpy.pyd"

lib_path = os.path.join(resources.package_dirname("srwlpy_aux"), platform, file)
srw_path = os.path.join(lib_path.split("srwlpy_aux")[0], file)

shutil.copyfile(lib_path, srw_path)

print("File: ", lib_path, "copied to: ", srw_path)
