# vscode-black-isort
Pseudo-daemon for Python Formatting using Black and ISort

### What this is:
- A script that automatically runs the python formatter Black, as well as ISort for import sorting, on file-save.

### Why I made it:
- I hate setting-up formatting in VsCode and wanted a simpler way to do so that just works out-of-the-box.

### How to use:
- Set up your python environment however you want (i personally recommend using a virtual environment.)
- Run `pip install black isort watchdog` to install the necessary dependencies.
- Download the script to your project directory, add it to your .gitignore, and run it `python dev_formatter.py`.
- Happy coding :)
