from tkinter import*

main = Tk()
main.geometry("515x640")
main.title("SymbolFinder")


ans = "None"

DisplayFrame = Frame(main,bg="BLUE",relief=GROOVE,borderwidth=5,width=75)
DisplayFrame.grid(column=0,row=0,columnspan=5)
DisplayFrame1 = Frame(DisplayFrame,bg="BLUE",relief=GROOVE,borderwidth=5,width=75)
DisplayFrame1.grid(column=1,row=0)
AnswerLable = Label(DisplayFrame,text=ans,width=62,height=3)  
AnswerLable.grid(column=0,row=0)
ButtonVariable = StringVar()
FontChangeVar = IntVar()
FieldChangeVar = IntVar()




def OnClick():
    Tsymbol.symbolCheck(ButtonVariable.get())

def change():
    n = len(Tsymbol.lib)
    if FontChangeVar.get() == 0:
        for i in range(n):
            Tsymbol.button.destroy()
        Tsymbol.ChangeImg("upper")
    if FontChangeVar.get() == 1:
        for i in range(n):
            Tsymbol.button.destroy()
        Tsymbol.ChangeImg("lower")
    if FontChangeVar.get() == 10:
        for i in range(n):
            Tsymbol.button.destroy()
        Tsymbol.ChangeImg("Part1")
    if FontChangeVar.get() == 11:
        for i in range(n):
            Tsymbol.button.destroy()
        Tsymbol.ChangeImg("Part2")
    if FontChangeVar.get() == 12:
        for i in range(n):
            Tsymbol.button.destroy()
        Tsymbol.ChangeImg("Part3")



class symbol():
    lib = [0]
    img = []
    def __init__(self):
        pass
        
        
    def Greek(self,data):

        self.ChangeImageButton = Radiobutton(DisplayFrame1,text="Upper",variable=FontChangeVar,value=0,command=change)   
        self.ChangeImageButton.grid(column=0,row=0)
        self.ChangeImageButton = Radiobutton(DisplayFrame1,text="Lower",variable=FontChangeVar,value=1,command=change)   
        self.ChangeImageButton.grid(column=0,row=1)


        greekSymbolName = ["Alpha","Beta","Gama","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu","Nu","Xi","Omicron","Pi","Rho","Sigma","Tau","Upsilon","Phi","Chi","Psi","Omega"]
        self.lib = greekSymbolName
        if data == "upper":
            greekSymbolImage = []
            n=len(self.lib)
            for i in range(n):
                greekSymbolImage.append(PhotoImage(file=f"Images/Greek/upper/{i+1}.png"))
            self.img = greekSymbolImage
        if data == "lower":
            greekSymbolImage = []
            n=len(self.lib)
            print("Working")
            for i in range(n):
                greekSymbolImage.append(PhotoImage(file=f"Images/Greek/lower/{i+1}.png"))
            self.img = greekSymbolImage

    def BasicLogic(self,data):
        
        self.ChangeImageButton = Radiobutton(DisplayFrame1,text="Part1",variable=FontChangeVar,value=10,command=change)   
        self.ChangeImageButton.grid(column=0,row=0)
        self.ChangeImageButton = Radiobutton(DisplayFrame1,text="Part2",variable=FontChangeVar,value=11,command=change)   
        self.ChangeImageButton.grid(column=0,row=1)
        self.ChangeImageButton = Radiobutton(DisplayFrame1,text="Part3",variable=FontChangeVar,value=12,command=change)   
        self.ChangeImageButton.grid(column=0,row=2)



        BasicLogicSymbolName = ["Material Implication","Material equivalence","negation","Domain of discourse","logical conjunction","logical (inclusive) disjunction","exclusive disjunction","Tautology","Contradiction","universal quantification","existential quantification","uniqueness quantification","definition","	precedence grouping","turnstile","double turnstile"]
        self.lib = BasicLogicSymbolName
        if data == "Part1":
            BasicLogicSymbolImage = []
            n=len(self.lib)
            for i in range(n):
                BasicLogicSymbolImage.append(PhotoImage(file=f"Images/BasicLogic/part1/{i+1}.png"))
            self.img = BasicLogicSymbolImage
        if data == "Part2":
            BasicLogicSymbolImage = []
            n=len(self.lib)
            for i in range(n):
                BasicLogicSymbolImage.append(PhotoImage(file=f"Images/BasicLogic/part1/{i+1}.png"))
            self.img = BasicLogicSymbolImage
        

    def ChangeImg(self,data):
        greekSymbolImage = []
        n=len(self.lib)
        
        if data == "upper":
            for i in range(n):
                greekSymbolImage.append(PhotoImage(file=f"Images/Greek/upper/{i+1}.png"))
            self.img = greekSymbolImage       
        
        if data == "lower":
            
            for i in range(n):
                greekSymbolImage.append(PhotoImage(file=f"Images/Greek/lower/{i+1}.png"))
            self.img = greekSymbolImage
        
        if data == "Part1":
            print("Part1")
            for i in range(n):
                greekSymbolImage.append(PhotoImage(file=f"Images/BasicLogic/part1/{i+1}.png"))
            self.img = greekSymbolImage 
        if data == "Part2":
            print("Part2")
            for i in range(n):
                greekSymbolImage.append(PhotoImage(file=f"Images/BasicLogic/part2/{i+1}.png"))
            self.img = greekSymbolImage 
        if data == "Part3":
            print("Part3")
            for i in range(n):
                greekSymbolImage.append(PhotoImage(file=f"Images/BasicLogic/part3/{i+1}.png"))
            self.img = greekSymbolImage 

        self.symbolButton()

    def symbolCheck(self,data):
        n = len(self.lib)
        for i in range(n):
            if self.lib[i] == data:
                print(f"Data is : {data} , Index is : {i}")
                ans =  self.lib[i]
                print(f"Answer is {ans} ")
                AnswerLable.config(text=ans)

    def symbolButton(self):
        n = len(self.lib)
        c=0
        r=2
        for i in range(n):
            if c == 4:
                c=0
                r+=1
            self.button = Radiobutton(main,image=self.img[i],value=self.lib[i],variable=ButtonVariable,command=OnClick,indicatoron=False,relief=RAISED,width=80,height=82)
            self.button.grid(row=r,column=c)
            c+=1
               
                     

Tsymbol = symbol()
Tsymbol.Greek("upper")
#trial
ButtonVariable.set("A")


def FieldChange():
    n = len(Tsymbol.lib)
    for i in range(n):
        Tsymbol.ChangeImageButton.destroy()

    if FieldChangeVar.get() == 0:
        Tsymbol.Greek("upper")
    if FieldChangeVar.get() == 1:
        Tsymbol.BasicLogic("Part1")
    

FieldButton=Radiobutton(main,text="Greek",value=0,variable=FieldChangeVar,command=FieldChange)
FieldButton1=Radiobutton(main,text="BasicLogic",value=1,variable=FieldChangeVar,command=FieldChange)       
FieldButton.grid(column=0,row=1)
FieldButton1.grid(column=1,row=1)

Tsymbol.symbolButton()
print(Tsymbol.lib)
mainloop()