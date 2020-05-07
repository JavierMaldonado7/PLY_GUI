
from src.lexer import tokens
import ply.yacc as yacc
import src.U_GUI as gui
from colorama import init
from termcolor import colored

def p_init_frame(p):
    'expression : START CURL_L NUMBER COMMA NUMBER CURL_R'

    if len(gui.framesArray) > 0:

        p[0] = "You've already started!"

    else:

        gui.windowWidth = p[3]

        gui.windowHeight = p[5]

        gui.createFrame()

        p[0] = colored("Welcome to U-GUI! Window initialized.", 'yellow')

def p_stunWarning(p):
    'expression : IDENTIFIER PERIOD LABEL'
    return 0


#function to create an initial window or add a new one to the collection
def p_make_window(p):
    'expression : MAKEWINDOW'
    gui.createFrame(gui.App,gui.App.getTop())
    p[0] = "Window created", gui.currentFrame

#function to check the current status of the Window being made
def p_check(p):
    'expression : CHECK'
    if checkInit(p):
        print("Showing current Window configuration", gui.currentFrame)
        print("Close Window to continue.")
        gui.makeCanvas()
        p[0] = colored("Continuing...",'red')

# BUTTONS------------------------------------------------------
def p_CreateButton(p):
    'expression : BUTTON  CURL_L NUMBER COMMA NUMBER COMMA NUMBER COMMA NUMBER CURL_R'
    if checkInit(p):
        name = input("Enter Button name: ")
        gui.App.createButton(gui.App,p[3],p[5],p[7],p[9], name,gui.App.getTop())
        p[0] = colored('Button was made! Named'+' '+name,'red')

#SHAPES FOR GUI--------------------------------------------------
def p_CreateCircle(p):
    'expression : OVAL CURL_L NUMBER COMMA NUMBER COMMA NUMBER COMMA NUMBER CURL_R'
    if checkInit(p):
        name = input(colored("Give your oval a name: ", "red"))
        color = input(colored("What color should it be(red,blue,green or yellow)?: ","red"))
        while( (color != 'yellow') and (color != 'red') and (color !='blue') and (color !='green')):
            color = input(colored("Not a valid color!(red,blue,green or yellow)?: ", "red"))
        gui.App.addOval(gui.App,p[3],p[5],p[7],p[9],name,color)
        p[0] = colored('Oval has been made!', 'red')


def p_CreateSquare(p):
    'expression : SQUARE CURL_L NUMBER COMMA NUMBER COMMA NUMBER COMMA NUMBER CURL_R'
    if checkInit(p):
        name = input(colored("Give your square a name: ", "red"))
        color = input(colored("What color should it be(red,blue,green or yellow)?: ","red"))
        while ((color != 'yellow') and (color != 'red') and (color != 'blue') and (color != 'green')):
            color = input(colored("Not a valid color!(red,blue,green or yellow)?: ", "red"))
        gui.App.addSquare(gui.App,p[3],p[5],p[7],p[9],name,color)
        p[0] = colored('Square has been made!', 'red')

def p_ResetShapes(p):
    'expression : RESET'
    if checkInit(p):
        shape = input(colored("Reset which shape(square, oval or all)?: ","red"))
        while ((shape != 'square') and (shape != 'oval') and (shape != 'all')):
            shape = input(colored("Not a valid shape!(square, oval or all)?: ", "red"))
        if(shape == "square"):
            gui.resetS
        if (shape == "oval"):
            gui.resetOvals()
        if (shape == "all"):
            gui.resetAll()

def p_CreateLine(p):
    'expression : LINE CURL_L NUMBER COMMA NUMBER COMMA NUMBER COMMA NUMBER CURL_R'
    if checkInit(p):
        name = input(colored("Give your line a name: ", "red"))
        color = input(colored("What color should it be(black,red,blue,green or yellow)?: ","red"))
        while ((color != 'yellow') and (color != 'red') and (color != 'blue') and (color != 'green') and (color!= 'black')):
            color = input(colored("Not a valid color!(black, red,blue,green or yellow)?: ", "red"))
        gui.App.addLine(gui.App,p[3],p[5],p[7],p[9],name,color)
        p[0] = colored('Line has been made!', 'red')

def p_LoadImage(p):
    #'expression : IMAGE CURL_L IDENTIFIER COMMA IDENTIFIER PERIOD IDENTIFIER COMMA NUMBER COMMA NUMBER COMMA NUMBER COMMA NUMBER CURL_R'
    'expression : IMAGE CURL_L IDENTIFIER PERIOD IDENTIFIER CURL_R'
    gui.App.addImage(gui.App,p[3]+p[4]+p[5])
    p[0] = colored('Image Loaded!','red')


def p_error(p):
    print("Syntax error in input", p)


def checkInit(p):
    if len(gui.framesArray) > 0:
        return True
    else:
        p[0] = "Not initialized yet"
        return False


parser = yacc.yacc()


while True:
    try:
        s = input(colored('U-GUI::= ', 'blue'))
        s.lower()
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)