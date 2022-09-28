from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from colorthief import ColorThief
from PIL import Image,ImageTk
from os import getcwd,path


class Extractor(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("850x500+250+150")
        self.title("ColorExtractor")
        self.config(bg="#f1faee")
        self.iconbitmap("icon.ico")
        self.resizable(FALSE,FALSE)

        def loadImage(name:str):
            image = Image.open(name)
            image = image.resize((50,50))
            photo = ImageTk.PhotoImage(image=image)
            return photo

        def uploadImage():
            global fileName
            try:
                fileName = filedialog.askopenfilename(initialdir=getcwd(),
                            title="Select Image",
                            defaultextension = "*.png",
                            filetypes=[
                            ("PNG Images","*.png"),
                            ("JPG Images","*.jpg"),
                            ("All Files","*.*")])
                
                image = Image.open(fileName)
                image = image.resize((268,227))
                image = ImageTk.PhotoImage(image=image)
                topLabel.configure(image=image)
                topLabel.configure(image=image,width=268,height=227)
                topLabel.image = image


            except Exception as e:
                pass
            
        def extractColor():
            try:
                colorThief = ColorThief(fileName)
                palette = colorThief.get_palette(color_count=9)

                rgb1 = palette[0]            
                rgb2 = palette[1]            
                rgb3 = palette[2]            
                rgb4 = palette[3]            
                rgb5 = palette[4]            
                rgb6 = palette[5]            
                rgb7 = palette[6]            
                rgb8 = palette[7]   

                color1 = f'#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}'       
                color2 = f'#{rgb2[0]:02x}{rgb1[1]:02x}{rgb2[2]:02x}'       
                color3 = f'#{rgb3[0]:02x}{rgb1[1]:02x}{rgb3[2]:02x}'       
                color4 = f'#{rgb4[0]:02x}{rgb1[1]:02x}{rgb4[2]:02x}'       
                color5 = f'#{rgb5[0]:02x}{rgb1[1]:02x}{rgb5[2]:02x}'       
                color6 = f'#{rgb6[0]:02x}{rgb1[1]:02x}{rgb6[2]:02x}'       
                color7 = f'#{rgb7[0]:02x}{rgb1[1]:02x}{rgb7[2]:02x}'       
                color8 = f'#{rgb8[0]:02x}{rgb1[1]:02x}{rgb8[2]:02x}' 


                cP1.itemconfig(id1,fill=color1)      
                cP1.itemconfig(id2,fill=color2)      
                cP1.itemconfig(id3,fill=color3)      
                cP1.itemconfig(id4,fill=color4)      
                cP1.itemconfig(id5,fill=color5)      
                cP1.itemconfig(id6,fill=color6)      
                cP1.itemconfig(id7,fill=color7)      
                cP1.itemconfig(id8,fill=color8)

                c1Label.config(text=color1)   
                c2Label.config(text=color2)   
                c3Label.config(text=color3)   
                c4Label.config(text=color4)   
                c5Label.config(text=color5)   
                c6Label.config(text=color6)   
                c7Label.config(text=color7)   
                c8Label.config(text=color8)  

            except Exception as e:
                pass

        # topDesign
        Canvas(self,bg="#2ec4b6",width=850,height=150).pack()

        # mainCanvasWidget
        mainCanvas = Canvas(self,bg="white",width=700,height=400)
        mainCanvas.place(x=50,y=50)

        # logoForDesign
        self.logo = loadImage("logo.png")
        Label(mainCanvas,image=self.logo,bg="white").place(x=10,y=10)
        Label(mainCanvas,text="Image Color Extractor",font="arial 15 bold",bg="white",fg="black").place(x=70,y=10)

        # lowerFrames for the Image
        lowerFrame = Frame(self,width=310,height=340)
        lowerFrame.place(x=410,y=80)

        # ImageFrame
        topLabel = Label(lowerFrame,width=38,height=15,bg="Black",relief=GROOVE,borderwidth=5)
        topLabel.place(x=15,y=10)

        # selectImgButton
        selectImage = ttk.Button(self,text="Select Image",width=15,command = uploadImage)
        selectImage.place(x=430,y=375)

        # extractColorButton
        ExtractImage = ttk.Button(self,text="Extract Color",width=15,command=extractColor)
        ExtractImage.place(x=600,y=375)

        # colorPalett
        cP1 = Canvas(mainCanvas,width=30,height=280,bg="white",bd=0)
        cP1.place(x=20,y=90)

        id1 = cP1.create_rectangle((0,0,50,35),fill='#b8255f')
        id2 = cP1.create_rectangle((0,35,50,70),fill='#023047')
        id3 = cP1.create_rectangle((0,70,50,105),fill='#9d0208')
        id4 = cP1.create_rectangle((0,105,50,140),fill='#cdb4db')
        id5 = cP1.create_rectangle((0,140,50,175),fill='#ffb703')
        id6 = cP1.create_rectangle((0,175,50,210),fill='#ffb5a7')
        id7 = cP1.create_rectangle((0,210,50,245),fill='#38a3a5')
        id8 = cP1.create_rectangle((0,245,50,280),fill='#004b23')

        # colorName
        c1Label = Label(mainCanvas,text="#b8255f",fg="#000",font="arial 12 bold",bg="white")
        c1Label.place(x=60,y=100)
        c2Label = Label(mainCanvas,text="#023047",fg="#000",font="arial 12 bold",bg="white")
        c2Label.place(x=60,y=135)
        c3Label = Label(mainCanvas,text="#9d0208",fg="#000",font="arial 12 bold",bg="white")
        c3Label.place(x=60,y=170)
        c4Label = Label(mainCanvas,text="#cdb4db",fg="#000",font="arial 12 bold",bg="white")
        c4Label.place(x=60,y=200)
        c5Label = Label(mainCanvas,text="#ffb703",fg="#000",font="arial 12 bold",bg="white")
        c5Label.place(x=60,y=235)
        c6Label = Label(mainCanvas,text="#ffb5a7",fg="#000",font="arial 12 bold",bg="white")
        c6Label.place(x=60,y=270)
        c7Label = Label(mainCanvas,text="#38a3a5",fg="#000",font="arial 12 bold",bg="white")
        c7Label.place(x=60,y=310)
        c8Label = Label(mainCanvas,text="#004b23",fg="#000",font="arial 12 bold",bg="white")
        c8Label.place(x=60,y=345)

if __name__ == "__main__":
    window = Extractor()
    window.mainloop()