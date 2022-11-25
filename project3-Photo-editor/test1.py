from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from PIL import ImageFont
from PIL import ImageDraw
# Font style
FONT = ImageFont.truetype('Helvetica', 16)

window = Tk()
window.title("Photo Editor")
# window.geometry("700x350")
window.config(padx=10,pady=10, bg="black")

#zoom for change size of picture
def zoom():
    zoom_num = scale_h.get()
    res = zoom_num/100
    return res

#text on canvas
def text():
    someword = entry.get()
    p_x = px.get()
    p_y = py.get()
    try:
        canvas.delete("some_tag")
        text1 = canvas.create_text(p_x,p_y,text=someword, fill="lightgreen", font=FONT,tag="some_tag")
    except:
        text1 = canvas.create_text(p_x,p_y,text=someword, fill="lightgreen", font=FONT,tag="some_tag")
    
    
#upload function
def UploadAction(zoom):
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    
    #write something on image
    # draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype("sans-serif.ttf", 16)
    # draw.text((100, 50),"Sample Text",(255,255,255),font=font)
    
    #multiple image size by zoom
    pixels_x, pixels_y = tuple([int(zoom * x)  for x in img.size])
    image = ImageTk.PhotoImage(img.resize((pixels_x, pixels_y))) 
    width, height = img.resize((pixels_x, pixels_y)).size
    
    canvas.config(height=height,width=width)
    canvas.create_image(0,0,image=image,anchor="nw")
    canvas.image=image
    
    

#button
button = Button(window, text='Open', command=lambda :UploadAction(zoom()))
button.grid(column=1, row=3)



scale_h = Scale(window, from_=0, to=100, orient='horizontal')   # 加入水平調整滑桿 ( orient='horizontal' )
scale_h.grid(column=1,row=4)

#entry
entry = Entry(width=38)
entry.grid(column=1,row=5,columnspan=2)
entry.insert(0, "write something")
px = Entry(width=30)
px.grid(column=1,row=6)
px.insert(0, "100")
py = Entry(width=30)
py.grid(column=2,row=6)
py.insert(0, "100")


#canvas
canvas =Canvas(highlightthickness=0,bg= 'black')
canvas.grid(column=1 ,row=2)


submit = Button(window, text="ADD",command = text)
submit.grid(column=2, row=5)


# label= Label(window)
# label.grid(column=1, row=4)




window.mainloop()