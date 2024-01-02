import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
import math

from assets import animal
from assets import animal_wolf
from assets import animal_sheep
from assets import animal_fox
from assets import animal_turtle
from assets import animal_antilope
from assets import human
from assets import animal_cybersheep
from assets import plant
from assets import plant_belladonna
from assets import plant_dandelion
from assets import plant_grass
from assets import plant_guarana
from assets import plant_pineborscht
from assets import world



class GUI:
    __sizeX = 0
    __sizeY = 0
    __selectedX = 0
    __selectedY = 0
    __index = 0
    __firstName = ""
    __lastName = ""
    __userInput = ""
    __world = None

    __root = None
    __outsideMap = None
    __mapFrame = None
    __logs = None
    __buttons = []
    __sideFrame = None
    __loadButton = None
    __saveButton = None
    __nextTurnButton = None
    __inputText = None
    __cursorText = None
    __strengthLabel = None
    __strengthText = None
    __initiativeLabel = None
    __initiativeText = None
    __ageLabel = None
    __ageText = None
    __rangeLabel = None
    __rangeText = None
    __saveButton = None
    __combo = None

    __organisms = ["None", "Human", "Wolf", "Sheep", "Fox", "Turtle", "Antilope", "CyberSheep", "Belladonna", "Dandelion", "Grass", "Guarana", "PineBorscht"]

    def __init__(self, x, y, index, firstName, lastName):
        self.__selectedX = -1
        self.__selectedY = -1
        self.__sizeX = x
        self.__sizeY = y
        self.__index = index
        self.__firstName = firstName
        self.__lastName = lastName
        self.__world = world.World(x, y, self)
        self.__root = Tk(firstName + " " + lastName + " " + str(index))

        self.__root.geometry("1920x1080")
        self.__root.resizable(False, False)
        self.__root.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.__root.bind("<Key>", self.__keyPressed)
        self.__root.bind("<Left>", self.__leftKey)
        self.__root.bind("<Right>", self.__rightKey)
        self.__root.bind("<Up>", self.__upKey)
        self.__root.bind("<Down>", self.__downKey)

        self.__outsideMap = Frame(self.__root, width=1080, height=1080)
        self.__outsideMap.pack(side=LEFT)

        self.__mapFrame = Frame(self.__outsideMap, width=1080, height=1080)
        width = math.floor(1080 / x)
        height = math.floor(1080 / y)
        for a in range(0, 1080, width):
            for b in range(0, 1080, height):
                butt = tkinter.Button(self.__mapFrame, text="X",
                                      command = lambda x=a/width, y=b/height: self.__updateCursor(x, y))
                butt.place(x=a, y=b, width= width, height=height)
                butt.configure(fg="black", bg="white", font=("Arial", 6, "bold"))
                self.__buttons.append(butt)

        self.__mapFrame.pack(side=LEFT)

        self.__logs = scrolledtext.ScrolledText(self.__root, width=60, height=67)
        self.__logs.configure(state="normal")
        self.__logs.insert(END, "Turn: " + str(self.__world.getTurn()) + "\n")
        self.__logs.configure(state="disabled")
        self.__logs.pack(side=LEFT, padx=10)

        self.__sideFrame = Frame(self.__root, width=500, height=1080)
        self.__sideFrame.pack(side=TOP)

        self.__inputText = Text(self.__sideFrame, width=30, height=1)
        self.__inputText.configure(state="disabled")
        self.__inputText.tag_configure("center", justify='center')
        self.__inputText.tag_add("center", 1.0, "end")
        self.__inputText.pack(pady=5, padx=20)

        self.__loadButton = Button(self.__sideFrame, height=4, width=15, text="Load", command=self.__loadFromFile)
        self.__loadButton.pack(pady=5, padx=20)

        self.__saveButton = Button(self.__sideFrame, height=4, width=15, text="Save", command=self.__saveToFile)
        self.__saveButton.pack(pady=5, padx=20)

        self.__nextTurnButton = Button(self.__sideFrame, height=4, width=15, text="Next Turn", command=self.__nextTurn)
        self.__nextTurnButton.pack(pady=5, padx=20)

        self.__cursorText = Text(self.__sideFrame, width=30, height=1)
        self.__cursorText.insert(1.0, "[ " + str(self.__selectedX) + ", " + str(self.__selectedY) + " ]")
        self.__cursorText.tag_configure("center", justify='center')
        self.__cursorText.tag_add("center", 1.0, "end")
        self.__cursorText.configure(state="disabled")
        self.__cursorText.pack(pady=5, padx=20)

        self.__combo = ttk.Combobox(self.__sideFrame, values=self.__organisms)
        self.__combo.current(0)

        self.__combo.pack(pady=5, padx=20)

        self.__strengthLabel = Label(self.__sideFrame, text="Strength")
        self.__strengthLabel.pack(pady=5, padx=20)

        self.__strengthText = Text(self.__sideFrame, width=30, height=1)
        self.__strengthText.insert(1.0, "0")
        self.__strengthText.pack(pady=5, padx=20)

        self.__initiativeLabel = Label(self.__sideFrame, text="Initiative")
        self.__initiativeLabel.pack(pady=5, padx=20)

        self.__initiativeText = Text(self.__sideFrame, width=30, height=1)
        self.__initiativeText.insert(1.0, "0")
        self.__initiativeText.pack(pady=5, padx=20)

        self.__ageLabel = Label(self.__sideFrame, text="Age")
        self.__ageLabel.pack(pady=5, padx=20)

        self.__ageText = Text(self.__sideFrame, width=30, height=1)
        self.__ageText.insert(1.0, "0")
        self.__ageText.pack(pady=5, padx=20)

        self.__rangeLabel = Label(self.__sideFrame, text="Range")
        self.__rangeLabel.pack(pady=5, padx=20)

        self.__rangeText = Text(self.__sideFrame, width=30, height=1)
        self.__rangeText.insert(1.0, "0")
        self.__rangeText.pack(pady=5, padx=20)

        self.__saveButton = Button(self.__sideFrame, height=4, width=15, text="Add", command=self.__saveOrganism)
        self.__saveButton.pack(pady=5, padx=20)

        self.__combo.bind("<<ComboboxSelected>>", self.__updateDisplayOrganism)
        self.__updateNames()

        print(self.__buttons[0]["text"])

        self.__root.mainloop()



    def getUserInput(self):
        return self.__userInput



    def __on_closing(self):
        self.__root.destroy()
        exit(0)

    def __leftKey(self, event):
        self.__userInput = "a"
        self.__updateAction("LEFT")

    def __rightKey(self, event):
        self.__userInput = "d"
        self.__updateAction("RIGHT")

    def __upKey(self, event):
        self.__userInput = "w"
        self.__updateAction("UP")

    def __downKey(self, event):
        self.__userInput = "s"
        self.__updateAction("DOWN")

    def __keyPressed(self, event):
        if (event.char == "w" or event.char == "a" or event.char == "s" or event.char == "d" or event.char == "e"):
            self.__userInput = event.char
            if (event.char == "w"):
                self.__updateAction("UP")
            elif (event.char == "a"):
                self.__updateAction("LEFT")
            elif (event.char == "s"):
                self.__updateAction("DOWN")
            elif (event.char == "d"):
                self.__updateAction("RIGHT")
            elif (event.char == "e"):
                self.__updateAction("ABILITY")

    def __updateAction(self, action):
        self.__inputText.configure(state="normal")
        self.__inputText.delete(1.0, END)
        self.__inputText.insert(1.0, "Current Action: " + action)
        self.__inputText.tag_add("center", 1.0, "end")
        self.__inputText.configure(state="disabled")

    def __updateDisplayOrganism(self, event):
        name = self.__combo.get()

        if (name == "Human"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(5))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(4))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))
        elif (name == "Wolf"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(9))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(5))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))
        elif (name == "Sheep"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(4))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(4))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))
        elif (name == "Fox"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(3))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(7))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))
        elif (name == "Turtle"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(2))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(1))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))
        elif (name == "Antilope"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(4))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(4))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(2))
        elif (name == "CyberSheep"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(11))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(4))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))
        elif (name == "Guarana" or name == "Dandelion" or name == "Grass"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(0))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(0))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))
        elif (name == "Belladonna"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(99))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(0))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))
        elif (name == "PineBorscht"):
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(10))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(0))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))
        else:
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(0))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(0))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(1))

    def __saveOrganism(self):
        if (not self.__world.isEmpty(self.__selectedX, self.__selectedY)):
            self.__world.clearOrganism(self.__selectedX, self.__selectedY)

        if (self.__combo.get() != "None"):
            newOrg = self.__interpretOrganism(self.__combo.get(), self.__selectedX, self.__selectedY, self.__world)
            newOrg.setStrength(int(self.__strengthText.get(1.0, END)))
            newOrg.setInitiative(int(self.__initiativeText.get(1.0, END)))
            newOrg.setAge(int(self.__ageText.get(1.0, END)))
            newOrg.setRange(int(self.__rangeText.get(1.0, END)))
            self.__world.setOrganism(newOrg)

        self.__updateNames()

    def __loadOrganism(self, x, y):
        if (not self.__world.isEmpty(x, y)):
            org = self.__world.getOrganism(x, y)
            self.__combo.set(org.getName())
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, str(org.getStrength()))
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, str(org.getInitiative()))
            self.__ageText.delete(1.0, END)
            self.__ageText.insert(1.0, str(org.getAge()))
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, str(org.getRange()))
        else:
            self.__combo.set("None")
            self.__strengthText.delete(1.0, END)
            self.__strengthText.insert(1.0, "0")
            self.__initiativeText.delete(1.0, END)
            self.__initiativeText.insert(1.0, "0")
            self.__ageText.delete(1.0, END)
            self.__ageText.insert(1.0, "0")
            self.__rangeText.delete(1.0, END)
            self.__rangeText.insert(1.0, "0")



    def __updateMapSize(self, x, y):
        self.__sizeX = x
        self.__sizeY = y
        self.__buttons = []
        self.__mapFrame.destroy()
        self.__mapFrame = Frame(self.__outsideMap, width=1080, height=1080)
        width = math.floor(1080 / x)
        height = math.floor(1080 / y)
        for a in range(0, 1080, width):
            for b in range(0, 1080, height):
                butt = tkinter.Button(self.__mapFrame, text="X",
                                      command=lambda x=a / width, y=b / height: self.__updateCursor(x, y))
                butt.place(x=a, y=b, width=width, height=height)
                butt.configure(fg="black", bg="white", font=("Arial", 6, "bold"))
                self.__buttons.append(butt)

        self.__mapFrame.pack(side=LEFT)


    def __updateNames(self):
        for x in range(self.__sizeX):
            for y in range(self.__sizeY):
                org = self.__world.getOrganism(x, y)
                if (org != None):
                    self.__buttons[x * self.__sizeY + y]["text"] = org.getName()
                else:
                    self.__buttons[x * self.__sizeY + y]["text"] = "X"

    def __updateCursor(self, x, y):
        self.__selectedX = x
        self.__selectedY = y
        self.__cursorText.configure(state="normal")
        self.__cursorText.delete(1.0, END)
        self.__cursorText.insert(1.0, "[ " + str(x) + ", " + str(y) + " ]")
        self.__cursorText.tag_add("center", 1.0, "end")
        self.__cursorText.configure(state="disabled")
        self.__loadOrganism(x, y)

    def __log(self, message):
        self.__logs.configure(state="normal")
        self.__logs.insert(END, message + "\n")
        self.__logs.configure(state="disabled")

    def __logAction(self, subject, object, action):
        subX = subject.getX()
        subY = subject.getY()
        objX = object.getX()
        objY = object.getY()

        self.__log("[" + str(subX) + ", " + str(subY) + "] " + subject.getName() + " " + action +
                   " [" + str(objX) + ", " + str(objY) + "] " + object.getName())

    def __logSingleAction(self, subject, action):
        subX = subject.getX()
        subY = subject.getY()

        self.__log("[" + str(subX) + ", " + str(subY) + "] " + subject.getName() + " " + action)

    def logEating(self, eater, eaten):
        self.__logAction(eater, eaten, "ate")

    def logAteDeath(self, eater, eaten):
        self.__logAction(eater, eaten, "died while eating")

    def logKill(self, killer, killed):
        self.__logAction(killer, killed, "killed")

    def logReproduction(self, subject):
        self.__logSingleAction(subject, "reproduced")

    def logPineBorscht(self, stepper, pine):
        self.__logAction(stepper, pine, "stepped on ")

    def logReflect(self, turtle, reflected):
        self.__logAction(turtle, reflected, "reflected")

    def logEscape(self, escaper, chaser):
        self.__logAction(escaper, chaser, "escaped from")

    def logWontEnter(self, fox, other):
        self.__logAction(fox, other, "wont enter")

    def __interpretOrganism(self, name, x, y, world):
        if (name == "Human"):
            return human.Human(x, y, world)
        elif (name == "Wolf"):
            return animal_wolf.Wolf(x, y, world)
        elif (name == "Sheep"):
            return animal_sheep.Sheep(x, y, world)
        elif (name == "Fox"):
            return animal_fox.Fox(x, y, world)
        elif (name == "Turtle"):
            return animal_turtle.Turtle(x, y, world)
        elif (name == "Antilope"):
            return animal_antilope.Antilope(x, y, world)
        elif (name == "CyberSheep"):
            return animal_cybersheep.CyberSheep(x, y, world)
        elif (name == "Belladonna"):
            return plant_belladonna.Belladonna(x, y, world)
        elif (name == "Dandelion"):
            return plant_dandelion.Dandelion(x, y, world)
        elif (name == "Grass"):
            return plant_grass.Grass(x, y, world)
        elif (name == "Guarana"):
            return plant_guarana.Guarana(x, y, world)
        elif (name == "PineBorscht"):
            return plant_pineborscht.PineBorscht(x, y, world)
        else:
            return None



    def __nextTurn(self):
        self.__logs.configure(state="normal")
        self.__logs.delete(1.0, END)
        self.__logs.insert(END, "Turn: " + str(self.__world.getTurn()) + "\n")
        self.__logs.configure(state="disabled")

        self.__world.doTurn()

        self.__updateNames()

    def __saveToFile(self):
        filetypes = (("All files", "*.*"), ("Text files", "*.txt"))
        filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=filetypes)

        if (filename == ""):
            return

        file = open(filename, "w")
        file.write(self.__world.outputString())
        file.close()

    def __loadFromFile(self):
        filetypes = (("All files", "*.*"), ("Text files", "*.txt"))
        filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=filetypes)

        if (filename == ""):
            return

        file = open(filename, "r")
        sizex = int(file.readline())
        sizey = int(file.readline())
        turn = int(file.readline())
        count = int(file.readline())

        self.__world = world.World(sizex, sizey, self)
        self.__world.setTurn(turn)

        for _ in range(count):
            name = file.readline().rstrip()
            x = int(file.readline())
            y = int(file.readline())
            strength = int(file.readline())
            initiative = int(file.readline())
            age = int(file.readline())
            arange = int(file.readline())
            ability = int(file.readline())
            organism = self.__interpretOrganism(name, x, y, self.__world)
            organism.setStrength(strength)
            organism.setInitiative(initiative)
            organism.setAge(age)
            organism.setRange(arange)
            organism.setAbilityCooldown(ability)
            self.__world.setOrganism(organism)

        self.__sizeX = sizex
        self.__sizeY = sizey

        self.__updateMapSize(sizex, sizey)
        self.__updateNames()

        file.close()
