import tkinter as tk

currentFrame = -1
windowWidth = 500
windowHeight = 500
frameImages = []
buttons = []
buttonsX = []
buttonsY = []
#--------OVAL DICTIONARY--------------------
ovals = {}

#-------SQUARE DICTIONARY-------------------
squrs = {}

#-------LINE DICTIONARY---------------------
lines = {}

#-------LABEL DICTIONARY--------
labels = {}

windows = []


def resetAll():
    squrs.clear()
    ovals.clear()
    labels.clear()
    lines.clear()

def resetOvals():
    ovals.clear()


def resetSquares():
    squrs.clear()

def resetLines():
    lines.clear()

def resetLabels():
    labels.clear()


class Label():
    def __init__(self,x,y,name,color,size):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.name = name

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getColor(self):
        return self.color

    def getSize(self):
        return self.size

    def getName(self):
        return self.name

    def setX(self,X):
        self.x = X

    def setY(self,Y):
        self.y = Y

    def setColor(self,C):
        self.color = C

    def setName(self,NAME):
        self.name = NAME

    def setSize(self,num):
        self.size = num

class Square():
    def __init__(self,x,y,h,w,name,color):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
        self.name = name

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getColor(self):
        return self.color

    def getName(self):
        return self.name

    def getHeight(self):
       return self.h

    def getWidth(self):
       return self.w

    def setX(self,X):
        self.x = X

    def setY(self,Y):
        self.y = Y

    def setHeight(self,H):
        self.h = H

    def setWidth(self,W):
        self.w = W

    def setColor(self,C):
        self.color = C

    def setName(self,NAME):
        self.name = NAME

class Oval:
    def __init__(self,x,y,h,w,name,color):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
        self.name = name

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getHeight(self):
        return self.h

    def getWidth(self):
        return self.w

    def getColor(self):
        return self.color

    def getName(self):
        return self.name

    def setX(self,X):
        self.x = X

    def setY(self,Y):
        self.y = Y

    def setHeight(self,H):
        self.h = H

    def setWidth(self,W):
        self.w = W

    def setColor(self,C):
        self.color = C

    def setName(self,NAME):
        self.name = NAME

class Line:
    def __init__(self,x,y,h,w,name,color):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color
        self.name = name


    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getHeight(self):
        return  self.h

    def getWidth(self):
        return self.w

    def getColor(self):
        return self.color

    def getName(self):
        return self.name


    def setX(self,X):
        self.x = X

    def setY(self,Y):
        self.y = Y

    def setHeight(self,H):
        self.h = H

    def setWidth(self,W):
        self.w = W

    def setColor(self,C):
        self.color = C

    def setName(self,NAME):
        self.name = NAME


class App(tk.Frame):
    def __init__(self, parent, initialFrame):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.frames = []
        self.canvasView = None
        self.frames.append(initialFrame)
        self.currentFrame = 0
        self.init_Buttons()
        self.top = parent
        self.makeWindow(0,self.top)
        self.bg = 'white'

    def getTop(self):
        return self.top

    def getParent(self):

        return self.parent

    def generateShapes(self,canvas):
        self.generateBgColor(canvas)
        self.generateOvals(canvas)
        self.generateSquares(canvas)
        self.generateLines(canvas)
        self.generateLabels(canvas)

#=============BACKGROUND==========================
    def changeBack(self,color):
        self.bg = color

    def generateBgColor(self, canvas):
        self.parent.configure(bg = self.bg)

#-------------LABEL GENERATION--------------------------------------------------------
    def generateLabels(self, canvas):
        for n in labels:
            canvas.create_text(labels.get(n).getX(), labels.get(n).getY(),
                               text = labels.get(n).getName(), fill = labels.get(n).getColor(), font = ("Helvetica",labels.get(n).getSize()))

    def addLabel(self, x, y, name, color, size):
        labels[name] = Label(x, y, name, color,size)

#-------------------OVAL GENERATION--------------------------------------------------------
    def generateOvals(self,canvas):
        for n in ovals:
            canvas.create_oval(ovals.get(n).getX(),ovals.get(n).getX(),ovals.get(n).getHeight(),ovals.get(n).getWidth(), fill = ovals.get(n).getColor())

    def addOval(self, x , y, width, height,name,color):
        ovals[name] =  Oval(x,y,width,height,name,color)
#--------------------------------------------------------------------

#----------------SQUARE GENERATION-----------------------------------
    def generateSquares(self, canvas):
        for n in squrs:
            canvas.create_rectangle(squrs.get(n).getX(),squrs.get(n).getX(),
                               squrs.get(n).getHeight(),squrs.get(n).getWidth(),
                               fill = squrs.get(n).getColor())


    def addSquare(self, x, y, width, height, name, color):
        squrs[name] = Square(x,y,width,height,name,color)
#-------------------------------------------------------------------
# ----------------LINE GENERATION-----------------------------------
    def generateLines(self, canvas):
        for n in lines:
            canvas.create_line(lines.get(n).getX(), lines.get(n).getX(),
                                lines.get(n).getHeight(), lines.get(n).getWidth(),
                                fill=lines.get(n).getColor())

    def addLine(self, x, y, width, height, name, color):
            lines[name] = Line(x, y, width, height, name, color)

# --------------------------------------------------------------------



    def init_Buttons(self):

        for x in buttons:

            x.pack()


    def createButton(self, width, height, xpos, ypos,text,top):
        button = tk.Button(self.top, text = text)

        button.width = width
        button.height = height
        buttons.append(button)
        buttonsX.append(xpos)
        buttonsY.append(ypos)

    def loadFrame(self, index):
        self.currentFrame = index
        self.canvasView = self.frames[index].getCanvas(self.parent)
        self.canvasView.pack()
        self.canvasView.update_idletasks()

    #Adds current details to the tkinter canvas

    def makeWindow(self, index, top):

        self.currentFrame = index

        self.canvasView = self.frames[index].getCanvas(self.parent,self.top)

        self.generateShapes(self.canvasView)

        self.canvasView.pack()

        self.canvasView.update_idletasks()

    def getCurrentFrame(self):
        return self.frames[self.currentFrame]



class Frame:
    h = 0
    w = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = None
        h = height
        w = width

    def getCanvas(self, parent, top):
        self.canvas = tk.Canvas(top, height=self.height, width=self.width, bg="white",
                                highlightthickness=0, relief='ridge')

        return self.canvas


#Creates current iteration of canvas to be dsiplayed
def makeCanvas():
    root = tk.Tk()
    root.title('U-GUI')
    root.resizable(False, False)
    app = App(root, windows[currentFrame])
    app.init_Buttons()
    app.pack()
    app.update_idletasks()
    root.attributes('-topmost', True)
    root.lift()
    root.after_idle(root.attributes, '-topmost', False)

    app.mainloop()


# creates a new frame after the last one, with the same background, sprites and assets as the current one
def createFrame():
    global currentFrame
    windows.append(Frame(windowWidth, windowHeight))
    currentFrame = currentFrame + 1