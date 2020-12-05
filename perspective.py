from TP2Code import *

def mouseDragged(app, event):
    print('drag')
    app.dragging = True
    if event.x >= app.getX:
        app.cxSun += 30
    else:
        app.cxSun -= 30

def mouseReleased(app,event):
    print('release')
    if app.dragging == False:
        return
    app.dragging = False



