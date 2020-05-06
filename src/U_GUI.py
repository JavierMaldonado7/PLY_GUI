import tkinter as tk

currentFrame = -1
windowWidth = 500
windowHeight = 500
frameImages = []
buttons = []
buttonsX = []
buttonsY = []
#--------OVAL SETUPS--------------------
ovals = []
ovalsX = []
ovalsY = []
ovalsW = []
ovalsH = []
ovalCol = []
#---------------------------------------
#-------SQUARE SETUPS-------------------
squrs = []
sqursX = []
sqursY = []
sqursW = []
sqursH = []
squrCol = []
#---------------------------------------

framesArray = []


def resetAll():
    del ovals[:]
    del ovalsX[:]
    del ovalsY[:]
    del ovalsW[:]
    del ovalsH[:]
    del ovalCol[:]
    del squrs[:]
    del sqursX[:]
    del sqursY[:]
    del sqursW[:]
    del sqursH[:]
    del squrCol[:]

def resetOvals():
    del ovals[:]
    del ovalsX[:]
    del ovalsY[:]
    del ovalsW[:]
    del ovalsH[:]
    del ovalCol[:]

def resetSquares():
    del squrs[:]
    del sqursX[:]
    del sqursY[:]
    del sqursW[:]
    del sqursH[:]
    del squrCol[:]



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

    def getTop(self):
        return self.top

    def getParent(self):

        return self.parent

    def generateShapes(self,canvas):
        self.generateOvals(canvas)
        self.generateSquares(canvas)

#-------------------OVAL GENERATION--------------------------------------------------------
    def generateOvals(self,canvas):
        for n in ovals:
            canvas.create_oval(ovalsX[ovals.index(n)],ovalsY[ovals.index(n)],ovalsH[ovals.index(n)],ovalsW[ovals.index(n)], fill = ovalCol[ovals.index(n)])

    def addOval(self, x , y, width, height,name,color):
        ovals.append(name)
        ovalsX.append(x)
        ovalsY.append(y)
        ovalsH.append(height)
        ovalsW.append(width)
        ovalCol.append(color)
#--------------------------------------------------------------------
#----------------SQUARE GENERATION-----------------------------------
    def generateSquares(self, canvas):
        for n in squrs:
            canvas.create_rectangle(sqursX[squrs.index(n)], sqursY[squrs.index(n)], sqursH[squrs.index(n)],
                               sqursW[squrs.index(n)], fill=squrCol[squrs.index(n)])

    def addSquare(self, x, y, width, height, name, color):
        squrs.append(name)
        sqursX.append(x)
        sqursY.append(y)
        sqursH.append(height)
        sqursW.append(width)
        squrCol.append(color)



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
    app = App(root, framesArray[currentFrame])
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
    framesArray.append(Frame(windowWidth, windowHeight))
    currentFrame = currentFrame + 1