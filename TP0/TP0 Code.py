#################################################
# TP0 Code.py
#
# Your name: Yi Sijun Cathy
# Your andrew id: sijuncay
#################################################



import cs112_f20_week7_linter
import math, copy, random

from cmu_112_graphics import *

# “Life moves pretty fast. If you don’t stop and look around 
#  once in a while, you could miss it.”
#                                             Ferris Bueller

def appStarted(app):
    app.mode = 'week'

def keyPressed(app, event):
    if event.key == 'w':
        app.mode = 'week'
    elif event.key == 'm':
        app.mode = 'month'
    elif event.key == 'y':
        app.mode = 'year'


#cited from email from Prof Kosbie about making a button


def mousePressed(app, event):
    cx, cy = app.width/2, app.height/2
    if ((cx-100 <= event.x <= cx+100) and
        (cy+100 <= event.y <= cy+120)):
        app.mode = 'month'

def redrawAll(app, canvas):
    if app.mode == 'week':
        cx1, cy1, r1 = app.width/2, app.height + 100, (app.height - 300) 
        cx2, cy2, r2 = app.width/2, app.height + 100, (app.height - 350) 
        canvas.create_oval(cx1-r1, cy1-r1, cx1+r1, cy1+r1, fill='white')
        canvas.create_oval(cx2-r2, cy2-r2, cx2+r2, cy2+r2, fill='white')
        canvas.create_arc(cx1-r1, cy1-r1, cx1+r1, cy1+r1, start=90, 
                                    extent=45, fill=None)
        canvas.create_arc(cx1-r1, cy1-r1, cx1+r1, cy1+r1, start=45, 
                                    extent=45, fill=None)
        canvas.create_text(200, 100, text = 'today\'s date', 
                                    font = 'Arial 40 bold')
        canvas.create_text(cx1, cy2 - 300, text = 'Review of the week', 
                                        font = 'Arial 40 bold')
        #cited from email from Prof Kosbie about making a button
        cx, cy = app.width/2, app.height/2
        canvas.create_rectangle(cx-100, cy+100, cx+100, cy+120, fill='cyan')
        canvas.create_text(cx, cy+110, text='Click me to go to Month')
        canvas.create_text(cx, cy+100)
    elif app.mode == 'month':
        cx, cy, r = app.width/2, app.height/2, (app.height/2 - 50)
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='yellow')
    elif app.mode == 'year':
        cx, cy, r = app.width/2, app.height/2, (app.height/2 - 150)
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='cyan')
    #canvas.create_line(200, app.height, cx-50, cy-50)
    #canvas.create_line(app.width-200, app.height, cx+50, cy+50)
    #canvas.create_rectangle(200, 500, 1200, 1000, fill='white')

    

runApp(width=1400, height=800)


