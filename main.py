from tkinter import *
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage
from tkinter import messagebox
from deep_translator import GoogleTranslator


class GUI(Tk):
    def __int__(self):
        super().__int__()

    def createLabel(self,txt,xAxcis,yAxcis,color="yellow"):
        label = Label(self, text=f"{txt}")
        label.config(font=("Arial", 18, "bold"),foreground = color)
        label.place(x=xAxcis,y=yAxcis)

    def translate(self):
        self.text = self.input.get()
        self.str = GoogleTranslator(source="auto",target=self.var.get()).translate(text=self.text)

        #showing the output
        self.createLabel("Your output is -> ",100,600,"cyan")
        self.ShowAnswer(self.str,300,600,"white")

    def TranslateButton(self):
        # Create a button widget
        button = Button(obj, text="Translate!", command=lambda: self.translate())
        # Place the button in the window
        button.place(x=300,y=300)
    def takeUserInput(self,color = "yellow"):
        self.input = Entry(self)
        self.input.config(foreground=color,font=("Arial",14,"bold"))
        self.input.place(x=300,y=105)


    def dropdownMeny(self):
        self.var = StringVar(self)
        self.var.set("english")  # default value
        option = OptionMenu(self, self.var, "english", "bengali", "hindi","spanish","chichewa","arabic","japanese")
        option.place(x=250,y=200)

    def ShowAnswer(self, str,xAxcis,yAxcis,color="yellow"):
        self.text = Text(self)
        self.text.insert(INSERT, str)
        self.text.configure(height=0,width=50)
        self.text.config(font=("Arial", 18, "bold"),foreground = color)
        self.text.place(x=xAxcis,y=yAxcis)


if __name__ == '__main__':
    # Create a new Tkinter window
    obj = GUI()
    obj.geometry("700x800")
    obj.maxsize(height=800,width=700)
    obj.config(background="black")
    #background picture
    image = Image.open("backGround.png")
    image = image.resize((700,700))
    # Convert the image to a PhotoImage object
    photo_image = ImageTk.PhotoImage(image)
    # Create a label with the image
    background_label = Label(obj, image=photo_image)
    # Set the label to fill the entire window
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    #taking the user input
    obj.takeUserInput()

    #creating the labels
    obj.createLabel(txt="Enter your text :",xAxcis=100,yAxcis=100,color='lightgray')
    # Set the window title
    obj.title("translator by Souvik")


    #setting the dropdown menu
    obj.dropdownMeny()


    obj.TranslateButton()
    # Run the Tkinter event loop
    obj.mainloop()
