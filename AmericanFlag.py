import turtle

def draw_rectangle(height,length,color):
	length = height*1.9
	t.color("white")
    	t.begin_fill()
        for i in range(2):
        	t.forward(length)
        	t.left(90)
        	t.forward(height)
        	t.left(90)
    	t.end_fill()

def draw_strips(height,length):
	height_of_strip = height/13
	t.penup()
	t.color("red","red")
	t.pendown()
	for i in range(7):
		t.begin_fill()
		t.forward(length)
                t.left(90)
                t.forward(height_of_strip)
                t.left(90)
                t.forward(length)
                t.right(90)
                if i <6:
                    t.forward(height_of_strip)
                    t.right(90)
                t.end_fill()
	t.right(90)
	

def draw_canton(height_of_canton,length_of_canton,height):
         t.color("blue","blue")
         t.begin_fill()
	 t.penup()
         t.goto(0,height)
	 t.right(90)
	 t.pendown()
         for i in range(2):
		t.forward(height_of_canton)
		t.left(90)
		t.forward(length_of_canton)
		t.left(90)
         t.end_fill()

def draw_star(size,color):
        t.color("blue","white")
        t.begin_fill()
        for i in range(5):
                t.forward(size/2)
                t.right(144)
                t.forward(size/2)
                t.left(72)
        t.end_fill()

def draw_star_row(G,height,star_location):
	t.goto(G,height-star_location)
	t.left(90)
        height_of_strip = height/13
        size = (height_of_strip*4)/5
	for i in range(6):
		draw_star(size,"white")
		if i<5:
			t.forward(2*G)
	t.penup()
	t.goto(G,height-star_location*3)
	t.pendown()
	for i in range(6):
		draw_star(size,"white")
                if i<5:
                        t.forward(2*G)
	t.penup()
        t.goto(G,height-star_location*5)
        t.pendown()
        for i in range(6):
                draw_star(size,"white")
                if i<5:
                        t.forward(2*G)
	t.penup()
        t.goto(G,height-star_location*7)
        t.pendown()
        for i in range(6):
                draw_star(size,"white")
                if i<5:
                        t.forward(2*G)
	t.penup()
        t.goto(G,height-star_location*9)
        t.pendown()
        for i in range(6):
                draw_star(size,"white")
                if i<5:
                        t.forward(2*G)
	
	t.penup()
        t.goto(2*G,height-star_location*2)
        t.pendown()
        for i in range(5):
                draw_star(size,"white")
                if i<4:
                        t.forward(2*G)
	t.penup()
        t.goto(2*G,height-star_location*4)
        t.pendown()
        for i in range(5):
                draw_star(size,"white")
                if i<4:
                        t.forward(2*G)
	t.penup()
        t.goto(2*G,height-star_location*6)
        t.pendown()
        for i in range(5):
                draw_star(size,"white")
                if i<4:
                        t.forward(2*G)
	t.penup()
        t.goto(2*G,height-star_location*8)
        t.pendown()
        for i in range(5):
                draw_star(size,"white")
                if i<4:
                        t.forward(2*G)	

def get_color(color):
	if color == "red":
		red = (255,0,0)
		return(red)
	if color == "blue":
		blue = (0,0,255)
		return(blue)
	if color == "white":
		white = (255,255,255) 
		return(white)
	else:
		print "choose either red, blue or white colors"

def draw_flag(height):
    length = height*1.9
    height_of_canton = (height*7)/13 
    length_of_canton = (length*2)/5
    height_of_strip = height/13
    size = (height_of_strip*4)/5
    star_location = height_of_canton/10
    G = length_of_canton/12
    color = "white"
    draw_rectangle(height,length,color)
    draw_strips(height,length)
    draw_canton(height_of_canton,length_of_canton,height)
    draw_star_row(G,height,star_location)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color("black")
    t.forward(length)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(height)
    t.left(90)






t = turtle.Turtle()
t.speed(1000)
t.ht()
height = float(raw_input("height of the flag : "))
draw_flag(height)
turtle.getscreen()._root.mainloop()

