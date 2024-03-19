from turtle import *

#we want to paint a house

#step 1 draw a square

speed(2)

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of a square

#drawing a door


forward(95)

color("yellow")
begin_fill()
left(90)

forward(120)
right(90)

forward(50)
right(90)

forward(120)
left(90)

end_fill()


penup()
goto(200, 200)
pendown()


#drawing a roof

color("red")
begin_fill()
left(140)
forward(150)
left(90)
forward(135)
end_fill()

penup()
goto(45, 165)
pendown()


#making windows
color("brown")
left(40)
forward(35)

left(90)
forward(35)

left(90)
forward(35)

left(90)
forward(35)

penup()
goto(165, 165)
pendown()

forward(35)
left(90)

forward(35)
left(90)

forward(35)
left(90)

forward(35)
left(90)

penup()
goto(-25, -50)
pendown()

#making grass

color("green")
begin_fill()
left(180)
forward(400)

right(90)
forward(50)

right(90)
forward(400)

right(90)
forward(50)
end_fill()

exitonclick()