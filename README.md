# Pyanimation

Math and Physics Animation Tool inspired by the Manim Math Animation Tool created by 3Blue1Brown. This is a personal passion project to develop my personal understanding and familiarity with python, coding structure and logic.

## Update : August 26, 2026
Currently working on double-slit diffraction animation, keeping tkinter elements on screen past next render, adding move and size functions for all elements (minus a few).

---
## Setup
Python 3.11 or newer required. You can use a official installer or a package manager.
```
# For macOS with Homebrew
brew install python 

# For Linux with Ubuntu, Debian
sudo apt update
sudo apt install python

# For Linux with Fedora or RHEL
sudo dnf install python
```
If you have python already, check version by running:
```
# For windows
python --version

# For macOS
python3 --version

# For Linux
python3.11 --version

# Expected output
Python 3.11._
```
Download the Pyanimation folder. Inside is a test.py file to demonstrate what Pyanimation can do, and a playground.py file

# Functions

Most objects have the render and animate functions. ```.move``` and ```.size``` are in the process of being added.

```.render``` : draws the object
```.animate``` : animates the drawing of the object
```.move``` : moves or transforms the object to a new coordinate
```.size``` : resizes the object according to its shape
