#################################################
# TP0 Code.py
#
# Your name: Yi Sijun Cathy
# Your andrew id: sijuncay
#################################################

import cs112_f20_week7_linter
import math, copy, random

from cmu_112_graphics import *

from cmu_112_graphics import *

def appStarted(app):
    app.counter = 0

def keyPressed(app, event):
    app.counter += 1

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text=f'{app.counter} keypresses', font='Arial 30 bold')

runApp(width=400, height=400)