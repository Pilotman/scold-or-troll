# Scold Or Troll

This app is a simple wrap of the twitter API for python. Provided with a blacklist file, in which twitter usernames are entered without the @ sign and in separate lines, the program is able to find whether or not a particular person follows anyone in that particular list, allowing to somewhat automate the process of finding out if a person might be acting in bad faith.

## Running the source

To run from the source, you need the `python-twitter` and `PyQt5` modules installed in python, use `pip` to install those, then simply run `python3 main.py` to run the program.

## Running in Windows

To run in Windows you need to download the .zip file (or clone the reposotory), then go into `dist/main` and double-click the `main.exe` file.

If you want to run it from somewhere else **make a shortcut**. If you only move the executable, things **will** break

## Blacklist files

The default blacklist file is `defaultList.txt`, feel free to edit it or add another one to suit your needs, but it has to be in the same directory as the executable/main.py script
