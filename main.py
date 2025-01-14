import turtle
import math

root = turtle.Screen()

mouse_cord = None

def mouse_pos(x,y):
    global mouse_cord 
    mouse_cord = (x,y)

    dir_x = mouse_cord[0] - turtle.xcor()
    dir_y = mouse_cord[1] - turtle.ycor()

    dist = math.sqrt(dir_x*dir_x + dir_y*dir_y)

    angle = math.degrees(math.atan2(dir_y,dir_x))

    turtle.setheading(angle)
    turtle.forward(dist)
    print( turtle.position())    
    print(mouse_cord)



root.onscreenclick(mouse_pos)




turtle.mainloop()