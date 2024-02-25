from turtle import *

width (7)

speed (5)

#I want to build a house

begin_fill()

color ("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#Door

begin_fill()
forward(70)
left(90)
color ("green")
forward(80)
right(90)

forward(60)
right(90)

forward(80)
end_fill()

#Ceiling

penup()

goto(200, 200)

pendown()
color ("black")
right(150)
begin_fill()
forward(200)

left(120)
forward(200)
end_fill()    

penup()

goto(20, 160)

pendown()

#Windows

begin_fill()

color ("cyan")
left(30)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

penup()

goto(140, 160)

pendown()

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill()

exitonclick()