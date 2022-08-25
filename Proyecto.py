import turtle

def ventana():
    """Esta función ejecuta la ventana para donde se va a jugar PONG(Ancho, Largo,Color de fondo)."""
    window = turtle.Screen()
    window.title("PONG, Felipe y Pablo")
    window.bgcolor("black")
    window.setup(width=800, height=600)
    window.tracer(0)
    return window

def playA():
    """Esta función se encarga de crear y personalizar la barra del jugador A(Forma,Posicionamiento,Dimensiones)."""
    a=input("ingrese el color que desea el jugadorA(ingles):")
    jugadorA = turtle.Turtle()
    jugadorA.speed(0)
    jugadorA.shape("square")
    jugadorA.color(a)
    jugadorA.penup()
    jugadorA.goto(-350,0)
    jugadorA.shapesize(stretch_wid=5, stretch_len=1)
    return jugadorA

def playB():
    """Esta función se encarga de crear y personalizar la barra del jugador B(Forma,Posicionamiento,Dimensiones)."""
    b=input("ingrese el color que desea el jugadorB(ingles):")
    jugadorB=turtle.Turtle()
    jugadorB.speed(0)
    jugadorB.shape("square")
    jugadorB.color(b)
    jugadorB.penup()
    jugadorB.goto(350,0)
    jugadorB.shapesize(stretch_wid=5, stretch_len=1)
    return jugadorB

def ball():
    """Esta función se encarga de crear la pelota y la velocidad de la misma(Forma,Posicionamiento,Dimensiones,color)."""
    pelota=turtle.Turtle()
    pelota.speed(0)
    pelota.shape("square")
    pelota.color("white")
    pelota.penup()
    pelota.goto(0,0)
    pelota.dx=0.6
    pelota.dy=0.6
    return pelota

def line():
    """Se utiliza para que aparezca la linea que divide el mapa de juego."""
    division = turtle.Turtle()
    division.color("white")
    division.goto(0,400)
    division.goto(0,-400)

def pen():
    """Creación del Marcador inicial."""
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup() 
    """Funciona para borrar el recorrido que dejan los objetos."""
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("jugadorA: 0       jugadorB: 0", align = "center",font = ("Courier",24,"normal" ))
    return pen

jA = playA()
jB = playB()

def jugadorA_up():
    """Sirve para que el jugador A se pueda mover hacia arriba"""
    y=jA.ycor()
    y += 20
    jA.sety(y)

def jugadorA_down():
    """Sirve para que el jugador A se pueda mover hacia abajo"""
    y=jA.ycor()
    y -= 20
    jA.sety(y)

def jugadorB_up():
    """Sirve para que el jugador B se pueda mover hacia arriba"""
    y=jB.ycor()
    y += 20
    jB.sety(y)

def jugadorB_down():
    """Sirve para que el jugador B se pueda mover hacia abajo"""
    y=jB.ycor()
    y -= 20
    jB.sety(y)

def main():
    answer=input("hay dos jugadores presentes?(si/no)")
    if answer == "si":
        one=input("ingrese el nombre del primer jugador:")
        two=input("ingrese el nombre del segundo jugador:")
        marcadorA=0
        marcadorB=0
        
        b = ball()
        line()
        p = pen()
        
        w = ventana()
        w.listen() 
        """ Dispone al programa a prestar atención a la interaccion del usuario con el teclado."""
        w.onkeypress(jugadorA_up,"w")
        w.onkeypress(jugadorA_down,"s")
        w.onkeypress(jugadorB_up,"Up")
        w.onkeypress(jugadorB_down,"Down")

        while True:
            """Es el que genera que el juego esté ejecutandose constantemente."""
            if ((marcadorA==7) or (marcadorB==7)):
                """Muestra el nombre del ganador de la partida."""
                if ((marcadorA==7) and (marcadorB<7)):
                    print("gano el jugador A:", one)
                    print("marcador A:",marcadorA,"marcadorB:",marcadorB)
                    print("El juego finalizo")
                    break

                if ((marcadorB==7) and (marcadorA<7)):
                    print("gano el jugador B:", two)
                    print("marcador A:",marcadorA,"marcadorB:",marcadorB)
                    print("El juego finalizo")
                    break
            elif (marcadorA<7) or (marcadorB<7):
                """Ejecución durante la partida cuando aún no hay ganador."""
                w.update()
                """Permite el reinicio del juego anotado un punto."""
                b.setx(b.xcor() + b.dx)
                b.sety(b.ycor()+ b.dy)
                """Movimientos de la pelota"""

                if b.ycor()>290:
                    """Borde Superior."""
                    b.dy *=-1
                if b.ycor()<-290:
                    """Borde Inferior."""
                    b.dy *=-1

                if b.xcor()>390:
                    """Anotación en  la cancha del jugador B"""
                    b.goto(0,0)
                    b.dx *=-1
                    marcadorA +=1
                    p.clear()
                    p.write("jugadorA: {}      jugadorB: {}".format(marcadorA,marcadorB), align = "center",font=("Courier",24,"normal" ))

                if b.xcor()<-390:
                    """Anotación la cancha del jugador A"""
                    b.goto(0,0)
                    b.dx *=-1
                    marcadorB+=1
                    p.clear()
                    p.write("jugadorA: {}       jugadorB: {}".format(marcadorA,marcadorB), align = "center",font=("Courier",24,"normal" ))

                if ((b.xcor() > 340 and b.xcor() < 350)
                        and (b.ycor() < jB.ycor()+50
                        and b.ycor()>jB.ycor()-50)): 
                    """Anotación la cancha del jugador A"""
                    b.dx*=-1
                        
                if ((b.xcor()<-340 and b.xcor()>-350)
                        and (b.ycor()<jA.ycor()+50
                        and b.ycor()>jA.ycor()-50)): 
                    """Demarcación de la cancha del jugador A"""
                    b.dx*=-1
    else:
        print("NO PUEDE JUGAR")

main()