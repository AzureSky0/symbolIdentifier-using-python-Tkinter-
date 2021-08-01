from tkinter import*

main = Tk()
main.geometry("520x520")
main.title("SymbolFinder")


ans = "None"
Upper = True
DisplayFrame = Frame(main,bg="BLUE",relief=GROOVE,borderwidth=5,width=75)
DisplayFrame.grid(column=0,row=0,columnspan=5)
AnswerLable = Label(DisplayFrame,text=ans,width=62,height=3)  
AnswerLable.grid(column=0,row=0)

class symbol():
    lib = [0]
    img = []
    def __init__(self):
        pass
        
        
    def Greek(self,data):
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
            
    def ChangeImg(self,data):
        n = len(self.lib)
        for i in range(n):
            self.button.destroy()
        greekSymbolImage = []
        n=len(self.lib)
        if data == "upper":
            for i in range(n):
                greekSymbolImage.append(PhotoImage(file=f"Images/Greek/upper/{i+1}.png"))
            self.img = greekSymbolImage       
        if data == "lower":
            print("Working")
            for i in range(n):
                greekSymbolImage.append(PhotoImage(file=f"Images/Greek/lower/{i+1}.png"))
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
        r=1
        for i in range(n):
            if c == 5:
                c=0
                r+=1
            self.button = Radiobutton(main,image=self.img[i],value=self.lib[i],variable=ButtonVariable,command=OnClick,indicatoron=False,relief=RAISED,width=80,height=82)
            self.button.grid(row=r,column=c)
            c+=1
               
                     

Tsymbol = symbol()
Tsymbol.Greek("upper")
#trial
ButtonVariable = StringVar()
FontChangeVar = IntVar()
ButtonVariable.set("A")
def OnClick():
    Tsymbol.symbolCheck(ButtonVariable.get())

def change():
    if FontChangeVar.get() == 0:
        Tsymbol.ChangeImg("upper")
    if FontChangeVar.get() == 1:
        Tsymbol.ChangeImg("lower")
        
DisplayFrame1 = Frame(DisplayFrame,bg="BLUE",relief=GROOVE,borderwidth=5,width=75)
DisplayFrame1.grid(column=1,row=0)
ChangeImageButton = Radiobutton(DisplayFrame1,text="Upper",variable=FontChangeVar,value=0,command=change)   
ChangeImageButton.grid(column=0,row=0)
ChangeImageButton = Radiobutton(DisplayFrame1,text="Lower",variable=FontChangeVar,value=1,command=change)   
ChangeImageButton.grid(column=0,row=1)
Tsymbol.symbolButton()
print(Tsymbol.lib)
mainloop()