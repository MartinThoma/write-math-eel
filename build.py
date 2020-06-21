# The following script was originally created by Samuel Williams:
#     https://github.com/samuelhwilliams/Eel/issues/331#issuecomment-647177832
# Thank you very much, you're awesome!

# Core Library modules
import os
from argparse import ArgumentParser

# Third party modules
import pkg_resources as pkg
import PyInstaller.__main__ as pyi

eel_js_file = pkg.resource_filename("eel", "eel.js")
js_file_arg = f"{eel_js_file}{os.pathsep}eel"
web_folder_arg = f"web{os.pathsep}web"

model_tar_file = pkg.resource_filename("hwrt", os.path.join("misc", "model.tar"))
model_file_arg = f"{model_tar_file}{os.pathsep}{os.path.join('hwrt', 'misc')}"

pyinstaller_args = [
    "--hidden-import",
    "bottle_websocket",
    "--add-data",
    js_file_arg,
    "--add-data",
    web_folder_arg,
    "--add-data",
    model_file_arg,
    "main.py",
    "--onefile",
]

print("Running:\npyinstaller", " ".join(pyinstaller_args), "\n")

pyi.run(pyinstaller_args)
