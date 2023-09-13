from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from register import Register
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image 
        img=Image.open(r"college_images\icbt.png")
        # img=img.resize((400,150),Image.ANTIALIAS)
        img = img.resize((400, 150), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=50,y=20,width=400,height=100)

        #second image
        img1=Image.open(r"college_images\facialrecognition.png")
        # img1=img1.resize((500,130),Image.ANTIALIAS)
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=530,height=130)

        #third image
        img2=Image.open(r"college_images\cardiffMetUni.png")
        # img2=img2.resize((500,130),Image.ANTIALIAS)
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=980,y=0,width=530,height=130)

        #background image
        img3=Image.open(r"college_images\Teacher-with-students-1.jpg")
        # img3=img3.resize((1500,710),Image.ANTIALIAS)
        img3 = img3.resize((1500, 710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=15,y=150,width=1500,height=710)

        title_lbl=Label(bg_img,text="ICBT CAMPUS COLOMBO",font=("Arial",35,"bold"),bg="darkgrey",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"college_images\std.jpg")
        # img4=img4.resize((220,220),Image.ANTIALIAS)
        img4 = img4.resize((230, 220), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        #Student Text Button
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #detect face button
        img5=Image.open(r"college_images\fad.jpg")
        # img5=img5.resize((220,220),Image.ANTIALIAS)
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        #detect face text button
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        #attendance button
        img6=Image.open(r"college_images\attendant.jpg")
        # img6=img6.resize((220,220),Image.ANTIALIAS)
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        #attendance text button
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        #help button
        img7=Image.open(r"college_images\helpdesk.jpg")
        # img7=img7.resize((220,220),Image.ANTIALIAS)
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.newregister_data)
        b1.place(x=1100,y=100,width=220,height=220)

        #help text button
        b1_1=Button(bg_img,text="Register New User",cursor="hand2",command=self.newregister_data,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #train button
        img8=Image.open(r"college_images\traindata.jpg")
        # img8=img8.resize((220,220),Image.ANTIALIAS)
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        #train text button
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        
        #photos button
        img9=Image.open(r"college_images\photos.jpeg")
        # img9=img9.resize((220,220),Image.ANTIALIAS)
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        #photos text button
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        #developer button
        img10=Image.open(r"college_images\developer.jpg")
        # img10=img10.resize((220,220),Image.ANTIALIAS)
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        #developer text button
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        #exit button
        img11=Image.open(r"college_images\exit.jpg")
        # img11=img11.resize((220,220),Image.ANTIALIAS)
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        #exit text button
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")




    #==========function buttons================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def newregister_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)



if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()