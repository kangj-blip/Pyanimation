# Pyanimation

<img width="1064" height="683" alt="Screenshot 2026-08-27 at 10 05 15 AM" src="https://github.com/user-attachments/assets/7991fa96-2128-41f3-9ae0-2c662beee171" />

Pyanimation is a Math and Physics Animation Tool inspired by the Manim Math Animation Tool created by 3Blue1Brown. This is a personal passion project to develop my personal understanding and familiarity with python, coding structure and logic.

---

### Update : August 26, 2026
Currently working on keeping tkinter elements on screen past next render, adding move and size functions for all elements (minus a few). Also working on adding fill / outline options, like hatching, fill, dotted, etc.

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

Most objects have the render and animate functions. ```.move```, ```.size```, and ```.particleAnimate``` are in the process of being added.

```.render``` : draws the object
```.animate``` : animates the drawing of the object
```.move``` : moves or transforms the object to a new coordinate
```.size``` : resizes the object according to its shape
```.particleAnimate``` : draws a steady stream of particles along the shape
