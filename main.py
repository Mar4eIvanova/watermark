from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = Tk()
window.title("WaterMark")
window.geometry("300x300")
window.config(bg="tan")
label = Label(text="Welcome to Watermark App! Please: ", font=("bahnschrift",10),bg="tan")
label.grid(row=0, columnspan=2)
label1= Label(text="Water Mark Text", font=("bahnschrift",10),bg="tan")
label1.grid(row=1,column=0)
label2 = Label(text="Upload Picture", font=("bahnschrift",10),bg="tan")
label2.grid(row=2,column=0)
text = Entry()
text.grid(row=1, column=1)


def upload():
    water_mark = text.get()
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("jpeg", "*.jpg"), ("png", "*.png")))
    image = Image.open(filename)
    width, height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("BRUSHSCI", 56)
    t_width, t_height = draw.textsize(water_mark, font)
    margin = 10
    x = width - t_width - margin
    y = height - t_height - margin
    draw.text((x, y), water_mark, font=font)
    image.show()


add_button = Button(text="Upload Picture", command=upload)
add_button.grid(row=2, column=1)

print(text)
window.mainloop()




