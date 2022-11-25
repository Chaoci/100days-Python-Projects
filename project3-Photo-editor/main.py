from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from PIL import ImageFont
from PIL import ImageDraw

img = ""
image = ""
width = ""
height = ""
def get_image():
    global img
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    change_size(zoom(),img)
    load_image()

#zoom for change size of picture
def zoom():
    zoom_num = scale_h.get()
    res = zoom_num/100
    return res

def change_size(zoom,img):
    #multiple image size by zoom
    global image, width, height
    pixels_x, pixels_y = tuple([int(zoom * x)  for x in img.size])
    image = ImageTk.PhotoImage(img.resize((pixels_x, pixels_y))) 
    #for canvas size
    width, height = img.resize((pixels_x, pixels_y)).size
    
def text_on_image():
    global img
    #write something on image
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Helvetica',55)
    draw.text((100, 50),"Sample Text",(0,0,0),font=font)
    
def load_image():
    global image
    if image=="":
        image = img
        canvas.config(height=height,width=width)
        canvas.create_image(0,0,image=image,anchor="nw")
        canvas.image=image
    else:
        change_size(zoom(),img)
        canvas.config(height=height,width=width)
        canvas.create_image(0,0,image=image,anchor="nw")
        canvas.image=image
    
window = Tk()
window.title("Photo Editor")
# window.geometry("700x350")
window.config(padx=10,pady=10, bg="black")

#canvas
canvas =Canvas(highlightthickness=0,bg= 'black')
canvas.pack()

#button
button = Button(window, text='Open', command=get_image)
button.pack()
load_image_button = Button(window, text='refresh',command=load_image)
load_image_button.pack()

#change size UI
scale_h = Scale(window, from_=0, to=100, orient='horizontal')   # 加入水平調整滑桿 ( orient='horizontal' )
scale_h.pack()

write = Button(window, text='write',command=text_on_image)
write.pack()


window.mainloop()