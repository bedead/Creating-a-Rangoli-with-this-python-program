import turtle

# taking users input to deside the size of Rangoli

print("The value should be between 1 to 5,\nelse the Design which will be created will be greater then monitor.\n(Preferred size is 1 or 2)")
l = int(input("what should be length of side of Rangoli : "))


    

def main_window():
    window = turtle.Screen()

    turtle.getscreen().bgcolor("black") # changing the background color
    turtle.pensize(5) # setting pen siz eto 5
    turtle.speed("fastest") # settinf speed of animation to slowest

    # setting the cursor pos to home
    turtle.home()

    # drawing center large circles with red shades
    turtle.dot(700*l,"darkred");turtle.dot(600*l,"firebrick")
    turtle.dot(500*l,"crimson");turtle.dot(400*l,"red")
    turtle.dot(300*l,"indianred");turtle.dot(200*l,'lightcoral')
    turtle.dot(200*l,"salmon");turtle.dot(100*l,"darksalmon")
    turtle.dot(150*l,"lightsalmon")
    
    
    turtle.home()
    turtle.dot(250*l,"darkgreen");turtle.dot(225*l,"green");turtle.dot(200*l,"forestgreen")
    turtle.dot(175*l,"yellowgreen");turtle.dot(150*l,"lightgreen")
    turtle.fd(125*1);turtle.seth(180);turtle.fd(250*1);turtle.seth(0) # drawing a line from center to right anf back to left with total diameter of circle

    turtle.home()
    turtle.begin_fill() # starting filling
    turtle.color("white", "navy")
    turtle.circle(50*l) # drawing center top center with filling blue

    turtle.seth(180) # setting angle
    turtle.circle(50*l) # drawing center bottom circle with filling blue

    turtle.end_fill() # ending filling

    turtle.begin_fill() # starting filling
    turtle.color("white", "navy")


    # drawing different color circle in left,right,up,and down
    turtle.seth(270)
    turtle.circle(50*l)

    turtle.seth(90)
    turtle.circle(50*l)

    turtle.end_fill() # ending filling
    turtle.home()

    turtle.seth(270);turtle.fd(125*l);turtle.seth(90);turtle.fd(250*l)
    turtle.home()

    turtle.setx(0);turtle.sety(62.5*l);turtle.dot(70*l,"mediumblue")
    turtle.setx(0);turtle.sety(62.5*l);turtle.dot(45*l,"blue")
    turtle.setx(0);turtle.sety(62.5*l);turtle.dot(30*l,"royalblue")
    turtle.setx(0);turtle.sety(62.5*l);turtle.dot(15*l,"cornflowerblue")
    turtle.pu()

    turtle.setx(62.5*l);turtle.sety(0)
    turtle.pd();turtle.dot(70*l,"mediumblue")
    turtle.setx(62.5*l);turtle.sety(0);turtle.dot(45*l,"blue")
    turtle.setx(62.5*l);turtle.sety(0);turtle.dot(30*l,"royalblue")
    turtle.setx(62.5*l);turtle.sety(0);turtle.dot(15*l,"cornflowerblue")
    turtle.pu()

    turtle.setx(0);turtle.sety(-62.5*l)
    turtle.pd();turtle.dot(70*l,"mediumblue")
    turtle.setx(0);turtle.sety(-62.5*l);turtle.dot(45*l,"blue")
    turtle.setx(0);turtle.sety(-62.5*l);turtle.dot(30*l,"royalblue")
    turtle.setx(0);turtle.sety(-62.5*l);turtle.dot(15*l,"cornflowerblue")
    turtle.pu()

    turtle.setx(-62.5*l);turtle.sety(0)
    turtle.pd();turtle.dot(70*l,"mediumblue")
    turtle.setx(-62.5*l);turtle.sety(0);turtle.dot(45*l,"blue")
    turtle.setx(-62.5*l);turtle.sety(0);turtle.dot(30*l,"royalblue")
    turtle.setx(-62.5*l);turtle.sety(0);turtle.dot(15*l,"cornflowerblue")
    turtle.pu()

    turtle.home()
    
    turtle.begin_fill()
    turtle.color("black");turtle.setx(0);turtle.sety(62.5*l);turtle.color("white","orangered")
    turtle.circle(100*l)

    turtle.seth(180)
    turtle.color("white");turtle.setx(0);turtle.sety(-62.5*l);turtle.color("white","orangered")
    turtle.circle(100*l)

    turtle.end_fill()


    # drawing four outter circles with different colors
    turtle.pd()
    turtle.pen(pencolor="black")
    turtle.goto(0.0,162.5*l)
    turtle.dot(175*l,"darkorange");turtle.dot(150*l,"orange")
    turtle.dot(100*l,"gold");turtle.dot(60*l,"yellow");turtle.dot(25*l,"white")

    turtle.goto(0.0,-162.5*l)
    turtle.dot(175*l,"darkorange");turtle.dot(150*l,"orange")
    turtle.dot(100*l,"gold");turtle.dot(60*l,"yellow");turtle.dot(25*l,"white")

    turtle.goto(0.0,162.5*l)
    turtle.goto(0.0,-162.5*l)

    turtle.pen(pencolor="white")
    turtle.goto(162.5*l,0.0)
    turtle.dot(175*l,"darkorange");turtle.dot(150*l,"orange")
    turtle.dot(100*l,"gold");turtle.dot(60*l,"yellow");turtle.dot(25*l,"white")

    turtle.goto(0.0,-162.5*l)
    turtle.goto(162.5*l,0.0*l)
    turtle.goto(0.0,162.5*l)

    turtle.goto(-162.5*l,0.0)
    turtle.dot(175*l,"darkorange");turtle.dot(150*l,"orange")
    turtle.dot(100*l,"gold");turtle.dot(60*l,"yellow");turtle.dot(25*l,"white")
    turtle.goto(0.0,162.5*l)
    turtle.goto(-162.5*l,0.0)
    turtle.goto(0.0,-162.5*l)

    # checking if size defined is 1 or 2 or greater
    if l ==1 or l ==2:

        # writting happy
        turtle.pu();turtle.goto(-200.0,200.0);turtle.pen(pencolor='gold')
        turtle.pd();turtle.goto(-200,100);turtle.goto(-200,150)
        turtle.goto(-150,150);turtle.goto(-150,200);turtle.goto(-150,100)

        turtle.pu();turtle.goto(-125,100);turtle.pd()
        turtle.goto(-125,200);turtle.goto(-100,200);turtle.goto(-100,100)
        turtle.goto(-100,150);turtle.goto(-125,150)

        turtle.pu();turtle.goto(-75,100);turtle.pd();turtle.pen(pencolor='navy')
        turtle.goto(-75,200);turtle.goto(-25,200);turtle.goto(-25,150)
        turtle.goto(-75,150)

        turtle.pu();turtle.goto(0,100);turtle.pd();turtle.pen(pencolor='navy')
        turtle.goto(0,200);turtle.goto(50,200);turtle.goto(50,150)
        turtle.goto(0,150)


        turtle.pu();turtle.goto(100,100);turtle.pd();turtle.pen(pencolor='gold')
        turtle.goto(125,200);turtle.pu();turtle.goto(85,200);turtle.pd()
        turtle.goto(112.5,150)


        # writting diwali
        turtle.pu();turtle.goto(-200,-100);turtle.pd()
        turtle.goto(-200,-200);turtle.goto(-150,-175);turtle.goto(-150,-125)
        turtle.goto(-200,-100)

        turtle.pu();turtle.goto(-125,-100);turtle.pd()
        turtle.goto(-100,-100);turtle.goto(-112.5,-100);turtle.goto(-112.5,-200)
        turtle.goto(-125,-200);turtle.goto(-100,-200)

        turtle.pu();turtle.goto(-75,-100);turtle.pd();turtle.pen(pencolor='navy')
        turtle.goto(-75,-200);turtle.goto(-50,-150);turtle.goto(-25,-200)
        turtle.goto(-25,-100)

        turtle.pu();turtle.goto(0,-200);turtle.pd();turtle.pen(pencolor='navy')
        turtle.goto(0,-100);turtle.goto(50,-100);turtle.goto(50,-150)
        turtle.goto(0,-150);turtle.goto(50,-150);turtle.goto(50,-200)

        turtle.pu();turtle.goto(75,-100);turtle.pd();turtle.pen(pencolor='gold')
        turtle.goto(75,-200);turtle.goto(100,-200)

        turtle.pu();turtle.goto(125,-100);turtle.pd()
        turtle.goto(175,-100);turtle.goto(150,-100);turtle.goto(150,-200)
        turtle.goto(125,-200);turtle.goto(175,-200)
        
        # if size defined greater then 1 or 2 there will be no printing of happy diwali in graphics
    else:
        turtle.pu();turtle.home()

if l>5:
    print("Value should be less then 5")
    print("Kindly Re-run the program ")

else:
    # runnung the main method
    main_window()



