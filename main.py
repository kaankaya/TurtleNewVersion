import turtle
import random


screen = turtle.Screen() # ekran yaz
score_turtle = turtle.Turtle()  # turtle oluşturduk
countdown_turtle = turtle.Turtle() #countdown
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ("Arial",30,"normal") #BÜYÜK HARF İLE OLUNCA SABİT GİBİ,BİRDEN FAZLA FONT KULLANICAĞIMIZ İÇİN TANIMLADIK
grid_size = 15
#turtle list
turtle_list = []
score = 0
game_over = False

#score turtle
def setup_score_turtle():
    score_turtle.hideturtle() #turtle gizle
    score_turtle.color("dark blue") #rengi ayarladık
    score_turtle.penup()
    top_height = screen.window_height() / 2 # ekranın ortasından başladığı için screen boyutunun yarısını istedik
    y = top_height * 0.9 #alıdıgmız değerin yüzde doksanını alıp y koordinatına atadık
    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score: 0",move=False,align="center",font=FONT) # yazıyı yazdık



def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear() #önce yazdıklarını temizle
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)  # yazıyı yazdık


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x * grid_size,y * grid_size) #çarpı 10 yaptım.aşağıda x,y verirken daha küçük sayılar vermek için
    turtle_list.append(t)



def setup_turtles():
    x_coordinates = [-20,-10,0,10,20]
    y_coordinates = [20,10,0,-10]

    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function , bir fonksiyon içerisinde kendisini çağırmak
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle() # turtle listen biri rsatgele seç
        screen.ontimer(show_turtles_randomly,500)



def countdown(time):
    global  game_over
    countdown_turtle.hideturtle()  # turtle gizle
    countdown_turtle.color("dark blue")  # rengi ayarladık
    countdown_turtle.penup()
    top_height = screen.window_height() / 2  # ekranın ortasından başladığı için screen boyutunun yarısını istedik
    y = top_height * 0.9  # alıdıgmız değerin yüzde doksanını alıp y koordinatına atadık
    countdown_turtle.setpos(0, y - 40)
    countdown_turtle.clear()
    if time > 0 :
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)  # yazıyı yazdık
        screen.ontimer(lambda : countdown(time - 1),1000) #lamda ile parametre fonksiyon verdik her seferinde 1 düşsün diye
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="GAME OVER!", move=False, align="center", font=FONT)  # yazıyı yazdık


def start_game_up():
    turtle.tracer(0)  # takip edici animasyon sıfırla
    setup_score_turtle()
    countdown(10)
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)  # takibi başlat



start_game_up()
turtle.mainloop()