from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Image Viewer')
root.iconbitmap('')

my_img1=ImageTk.PhotoImage(Image.open("images/img1.webp"))
my_img2=ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("images/img3.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("images/img4.webp"))
my_img5=ImageTk.PhotoImage(Image.open("images/img5.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]


my_label=Label(image=my_img1,width=500,height=500)
my_label.grid(row=0,column=0,columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1],width=500,height=500)
    button_forward=Button(root,text=">>",command=lambda :forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda: back(image_number-1))

    if image_number == 5:
       button_forwar=Button(root,text=">>",state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status=Label(root,text="image" + str(image_number) + "of " + str(len(image_list)), bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1], width=500, height=500)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
       button_forwar=Button(root,text="<<",state=DISABLED)

    #putting it on the screen
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    #update statusbar
    status = Label(root, text="image" + str(image_number) + "of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back=Button(root,text="<<",command=back, state=DISABLED)
button_exit=Button(root,text="Exit Program",command=root.quit)
button_forward=Button(root,text=">>",command=lambda :forward(2))

status=Label(root,text="image 1 of " + str(len(image_list)), bd=1,relief=SUNKEN, anchor=E)


button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2,pady=10)
button_exit.grid(row=1,column=1)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)






root.mainloop()