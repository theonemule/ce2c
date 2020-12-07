from graphics import *

def main():
    win = GraphWin('Face', 500, 500) 

    head = Circle(Point(250,250), 200) 
    head.setFill(color_rgb(255, 255, 0))
    head.draw(win)

    eye1 = Circle(Point(175, 170), 15)
    eye1.setFill(color_rgb(0, 0, 255))
    eye1.draw(win)
    
    eye2 = Circle(Point(325, 175), 15)
    eye2.setFill(color_rgb(0, 0, 255))
    eye2.draw(win)
    
    nose = Circle(Point(250, 225), 15)
    nose.setFill(color_rgb(255, 0, 0))
    nose.draw(win)    

    mouth = Oval(Point(150, 300), Point(350, 400)) 
    mouth.setFill(color_rgb(0, 0, 0))
    mouth.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()