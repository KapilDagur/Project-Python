from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class QrMaker(object):
    def __init__(self,root):        
        self.root = root

        #Widget Config........................
        self.root.title(" Student Details QR Code Maker....   || Doveloped By KAPIL DAGUR ")
        self.root.geometry("800x600+250+50")
        self.root.resizable(False,False)
        
        #All Variables.........................
        self.roll_no = StringVar()
        self.student_name = StringVar()
        self.course = StringVar()
        self.branch = StringVar()
        self.gender = StringVar()
        self.blood = StringVar()
        self.father_Name = StringVar()
        self.contact = StringVar()
        self.address = StringVar()

        #Top Label............................
        top_label = Label(self.root, text="Welcome Dear !!! ", font=("Copperplate Gothic",30), bg="#ff66ff",fg="#ffffff",anchor="w")
        top_label.place(x=0,y=0,relwidth=1)

        #Left Frame...........................
        self.left_frame = Frame(self.root,bd=2,bg="#ffffff",relief=RIDGE)
        self.left_frame.place(x=40,y=80,width=400,height=400)

        #Left Frame Label.....................
        student_roll_no = Label(self.left_frame,text="1. Student Roll No :",font=("arial",15),bg="#ffffff",fg="#191966")
        student_roll_no.place(x=0,y=10)
        student_name = Label(self.left_frame,text="2. Student Name :",font=("arial",15),bg="#ffffff",fg="#191966")
        student_name.place(x=0,y=50)
        student_course = Label(self.left_frame,text="3. Course Name :",font=("arial",15),bg="#ffffff",fg="#191966")
        student_course.place(x=0,y=90)
        student_branch = Label(self.left_frame,text="4. Branch Name :",font=("arial",15),bg="#ffffff",fg="#191966")
        student_branch.place(x=0,y=130)
        student_gender = Label(self.left_frame,text="5. Gender :",font=("arial",15),bg="#ffffff",fg="#191966")
        student_gender.place(x=0,y=170)
        student_blood = Label(self.left_frame,text="6. Blood Group :",font=("arial",15),bg="#ffffff",fg="#191966")
        student_blood.place(x=0,y=210)
        student_father_name = Label(self.left_frame,text="7. Father's Name :",font=("arial",15),bg="#ffffff",fg="#191966")
        student_father_name.place(x=0,y=250)
        student_contact = Label(self.left_frame,text="8. Address :",font=("arial",15),bg="#ffffff",fg="#191966")
        student_contact.place(x=0,y=290)
        student_address = Label(self.left_frame,text="9. Contact :",font=("arial",15),bg="#ffffff",fg="#191966")
        student_address.place(x=0,y=330)

        #Left Frame Label Data Input(Entry)
        value_roll = Entry(self.left_frame,textvariable=self.roll_no,font=("arial",15),bg="#ffffcc")
        value_roll.place(x=180,y=10,height=30,width=200)
        value_name = Entry(self.left_frame,textvariable=self.student_name,font=("arial",15),bg="#ffffcc")
        value_name.place(x=180,y=50,height=30,width=200)
        value_course = Entry(self.left_frame,textvariable=self.course,font=("arial",15),bg="#ffffcc")
        value_course.place(x=180,y=90,height=30,width=200)
        value_branch = Entry(self.left_frame,textvariable=self.branch,font=("arial",15),bg="#ffffcc")
        value_branch.place(x=180,y=130,height=30,width=200)
        value_gender = Entry(self.left_frame,textvariable=self.gender,font=("arial",15),bg="#ffffcc")
        value_gender.place(x=180,y=170,height=30,width=200)
        value_blood = Entry(self.left_frame,textvariable=self.blood,font=("arial",15),bg="#ffffcc")
        value_blood.place(x=180,y=210,height=30,width=200)
        value_father_name = Entry(self.left_frame,textvariable=self.father_Name,font=("arial",15),bg="#ffffcc")
        value_father_name.place(x=180,y=250,height=30,width=200)
        value_address = Entry(self.left_frame,textvariable=self.address,font=("arial",15),bg="#ffffcc")
        value_address.place(x=180,y=290,height=30,width=200)
        value_contact = Entry(self.left_frame,textvariable=self.contact,font=("arial",15),bg="#ffffcc")
        value_contact.place(x=180,y=330,height=30,width=200)

        #Button Frame.........................
        self.button_frame = Frame(self.root,bd=2,bg="#ffffff",relief=RIDGE)
        self.button_frame.place(x=40,y=490,height=50,width=400)
        create = Button(self.button_frame,text="Create QR",font=("times new roman",14),bg="#39e600",fg="#ffffff",relief=RIDGE,command=self.createqr)
        create.place(x=10,y=5,height=35,width=140)
        clear = Button(self.button_frame,text="Clear Details",font=("times new roman",14),bg="#ff4d4d",fg="#ffffff",relief=RIDGE,command=self.clearData)
        clear.place(x=250,y=5,height=35,width=140)

        #Notification Frame...................
        self.notification_frame = Frame(self.root,bd=2,bg="#ffffff",relief=RIDGE)
        self.notification_frame.place(x=40,y=545,width=400,height=50)
        self.notification = Label(self.notification_frame,text="",font=("arial",16),bg="#ffffff",fg="#39e600")
        self.notification.place(x=5,y=5,height=40,width=370)
        
        #Right Frame..........................
        self.right_frame = Frame(self.root,bd=2,bg="#b3e6ff",relief=RIDGE)
        self.right_frame.place(x=460,y=80,height=400,width=300)
        self.right_sub_frame = Frame(self.right_frame,bd=2,bg="#ffffff",relief=RIDGE)
        self.right_sub_frame.place(x=50,y=100,height=200,width= 200)
        self.right_sub_frame_label = Label(self.right_sub_frame,text="QR NOT\n AVLIABLE",font=("times new roman",14),bg="#00004d",fg="#ffffff")
        self.right_sub_frame_label.place(x=0,y=0,height=198,width=198)

        #Right Bottom Label...................
        right_bottom_label = Label(self.root,text="THANK YOU for \nUsing Our Service !!!",bd=2,font=("arial",20),bg="#ffffff",fg="#000000",relief=RIDGE)
        right_bottom_label.place(x=460,y=490,height=105,width=300)

    def createqr(self):
        if(self.roll_no.get() == "" or self.student_name.get() == "" or self.course.get() == "" or self.branch == "" or self.gender.get() == "" or self.blood.get() == "" or self.father_Name.get() == "" or self.address.get() == "" or self.contact.get() == ""):
           self.notification.config(text="All Fields Are Required !!!",fg="#ff4d4d")
        else:
            student_data = (f"Roll No : {self.roll_no.get()} \nStudent Name : {self.student_name.get()} \nCourse Name : {self.course.get()} \nBranch Name : {self.branch.get()} \nGender : {self.gender.get()} \nBlood Group : {self.blood.get()} \nFather\'s Name : {self.father_Name.get()} \nAddress : {self.address.get()} \nContact Number : {self.contact.get()} ")
            student_qr = qrcode.make(student_data)
            resize_image = resizeimage.resize_cover(student_qr,[200,200])
            self.student_qr_png = ImageTk.PhotoImage(resize_image)
            self.right_sub_frame_label.config(image=self.student_qr_png)
            student_qr.save(f"D:\\Python Project\\QR Generator\\QR Created\\Student_Roll_No_{self.roll_no.get()}.png")
            self.notification.config(text="Congrats !! QR Created Successfull !!!",fg="#39e600")


    def clearData(self):
        self.student_name.set("")
        self.roll_no.set("")
        self.course.set("")
        self.branch.set("")
        self.gender.set("")
        self.blood.set("")
        self.father_Name.set("")
        self.contact.set("")
        self.address.set("")
        self.notification.config(text="")

if __name__ == '__main__':
    root = Tk()
    test = QrMaker(root)
    root.mainloop()

