# Pyanimation

<img width="1064" height="683" alt="Screenshot 2026-08-27 at 10 05 15 AM" src="https://github.com/user-attachments/assets/7991fa96-2128-41f3-9ae0-2c662beee171" />

Pyanimation is a Math and Physics Animation Tool inspired by the Manim Math Animation Tool created by 3Blue1Brown. This is a personal passion project to develop my personal understanding and familiarity with python, coding structure and logic.

---

### Update : August 29, 2026
Currently working on keeping tkinter elements on screen past next render, adding move and size functions for all elements (minus a few). Also working on adding fill / outline options, like hatching, fill, dotted, etc. and recording canvas on run.

## Requirements
Python 3.11 or newer is required. 
### 1. Clone the repository
```
git clone https://github.com/kangj-blip/Pyanimation
```
### 2. Install dependencies
```
cd Pyanimation
pip install -r requirements.txt
```
### 3. Open test.py
```
python test.py
```
Do download Python, run ```install python``` or your OS equivalent. If you have Python already, check version by running ```python --version```.

# Functions

Most objects have the render and animate functions. ```.move```, ```.size```, and ```.particleAnimate``` are in the process of being added. Check the current **engine.py** file for more info.

```.render``` : draws the object
```.animate``` : animates the drawing of the object
```.move``` : moves or transforms the object to a new coordinate
```.size``` : resizes the object according to its shape
```.particleAnimate``` : draws a steady stream of particles along the shape
