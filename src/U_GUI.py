import tkinter as tk



currentFrame = -1
windowWidth = 500
windowHeight = 500
frameImages = []
buttons = []
buttonsX = []
buttonsY = []
# --------OVAL DICTIONARY--------------------
ovals = {}

# -------SQUARE DICTIONARY-------------------
squrs = {}

# -------LINE DICTIONARY---------------------
lines = {}

# -------IMAGE DICTIONARY---------------------
images = {}

framesArray = []


def resetAll():
    squrs.clear()
    ovals.clear()
    lines.clear()


def resetOvals():
    ovals.clear()


def resetSquares():
    squrs.clear()


def resetLines():
    lines.clear()


class Square():
    def __init__(self, x, y, h, w, name, color):
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

    def setX(self, X):
        self.x = X

    def setY(self, Y):
        self.y = Y

    def setHeight(self, H):
        self.h = H

    def setWidth(self, W):
        self.w = W

    def setColor(self, C):
        self.color = C

    def setName(self, NAME):
        self.name = NAME


class Oval:
    def __init__(self, x, y, h, w, name, color):
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

    def setX(self, X):
        self.x = X

    def setY(self, Y):
        self.y = Y

    def setHeight(self, H):
        self.h = H

    def setWidth(self, W):
        self.w = W

    def setColor(self, C):
        self.color = C

    def setName(self, NAME):
        self.name = NAME


class Line:
    def __init__(self, x, y, h, w, name, color):
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

    def setX(self, X):
        self.x = X

    def setY(self, Y):
        self.y = Y

    def setHeight(self, H):
        self.h = H

    def setWidth(self, W):
        self.w = W

    def setColor(self, C):
        self.color = C

    def setName(self, NAME):
        self.name = NAME


class Picture:
    def __init__(self, path, name, width, height, Xpos, Ypos):
        self.name = name
        self.width = width
        self.height = height
        self.image = path
        self.path = path
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.imageArray = []

    # def createImage(self):
    #     if isinstance(self.path, str):
    #         try:
    #             self.image = Image.open(self.path).convert('RGBA')
    #             y = 0
    #             while y < self.image.size[1]:
    #                 x = 0
    #                 while x < self.image.size[0]:
    #                     box = (x, y, (x + self.width), (y + self.height))
    #                     self.imageArray.append(self.image.crop(box))
    #                     x = x + self.width
    #                 y = y + self.height
    #
    #         except FileNotFoundError:
    #             print("File doesn't exist or couldn't be read:", self.path)
    #     else:
    #         print("Invalid Parameter", self.path)

    def getIndex(self):
        return self.index

    def getName(self):
        return self.name

    def getImage(self):
        return self.image

    def setIndex(self, index):
        self.index = index

    def setName(self, name):
        self.name = name


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
        self.makeWindow(0, self.top)

    def getTop(self):
        return self.top

    def getParent(self):

        return self.parent

    def generateShapes(self, canvas):
        self.generateOvals(canvas)
        self.generateSquares(canvas)
        self.generateLines(canvas)

    # -------------------OVAL GENERATION--------------------------------------------------------
    def generateOvals(self, canvas):
        for n in ovals:
            canvas.create_oval(ovals.get(n).getX(), ovals.get(n).getX(), ovals.get(n).getHeight(),
                               ovals.get(n).getWidth(), fill=ovals.get(n).getColor())

    def addOval(self, x, y, width, height, name, color):
        ovals[name] = Oval(x, y, width, height, name, color)

    # --------------------------------------------------------------------

    # ----------------SQUARE GENERATION-----------------------------------
    def generateSquares(self, canvas):
        for n in squrs:
            canvas.create_rectangle(squrs.get(n).getX(), squrs.get(n).getX(),
                                    squrs.get(n).getHeight(), squrs.get(n).getWidth(),
                                    fill=squrs.get(n).getColor())

    def addSquare(self, x, y, width, height, name, color):
        squrs[name] = Square(x, y, width, height, name, color)

    # -------------------------------------------------------------------
    # ----------------LINE GENERATION-----------------------------------
    def generateLines(self, canvas):
        for n in lines:
            canvas.create_line(lines.get(n).getX(), lines.get(n).getX(),
                               lines.get(n).getHeight(), lines.get(n).getWidth(),
                               fill=lines.get(n).getColor())

    def addLine(self, x, y, width, height, name, color):
        lines[name] = Line(x, y, width, height, name, color)

    # --------------------------------------------------------------------
    # -----------------Image Loading---------------------------------------
    def generatePictures(self, canvas):
        for n in images:
            canvas.create_image(images.get(n).getXpos(), images.get(n).getYpos(), image= tk.PhotoImage(file = n.path))

    def addImage(self, path):
        images['test'] = Picture(self, 'test', 'remotebomb.png', 100, 100, 100)

    def init_Buttons(self):

        for x in buttons:
            x.pack()

    def createButton(self, width, height, xpos, ypos, text, top):
        button = tk.Button(self.top, text=text)

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

    # Adds current details to the tkinter canvas

    def makeWindow(self, index, top):

        self.currentFrame = index

        self.canvasView = self.frames[index].getCanvas(self.parent, self.top)

        self.generateShapes(self.canvasView)

        self.generateImages(self.canvasView)

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


# Creates current iteration of canvas to be dsiplayed
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
