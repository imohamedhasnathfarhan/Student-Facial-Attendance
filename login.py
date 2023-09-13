from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   #pip install pillow
from tkinter import messagebox
import mysql.connector
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from register import Register
from main import Face_Recognition_System
from attendance import Attendance




def main():
    win=Tk() 
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Acer\Desktop\Facial Attendance System\college_images\Teacher-with-students-1.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=580,y=170,width=350,height=450)

        img1=Image.open(r"C:\Users\Acer\Desktop\Facial Attendance System\college_images\frontmahan.png")
        # img1=img1.resize((100,100),Image.ANTIALIAS)
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=700,y=180,width=100,height=100)

        get_str=Label(frame,text="Login Here",font=("Gill Sans MT",24,"bold"),fg="white",bg="black")
        get_str.place(x=80,y=110)

        # label
        username=lbl=Label(frame,text="User Name: ",font=("Arial",13,"bold"),fg="white",bg="black")
        username.place(x=65,y=185)

        self.txtuser=ttk.Entry(frame,font=("Courier",13,"bold"))
        self.txtuser.place(x=40,y=220,width=270)


        password=lbl=Label(frame,text="Password: ",font=("Arial",13,"bold"),fg="white",bg="black")
        password.place(x=65,y=256)

        self.txtpass=ttk.Entry(frame,show='*',font=("Arial",13,"bold"))
        self.txtpass.place(x=40,y=290,width=270)

        # =======icon images =======
        img2=Image.open(r"C:\Users\Acer\Desktop\FAS\college_images\loginfront.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        # img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=620,y=355,width=25,height=25)

        img3=Image.open(r"C:\Users\Acer\Desktop\FAS\college_images\pwpng.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        # img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=620,y=427,width=25,height=25)

        #login button
        loginbtn=Button(frame,command=self.login,text="Login",cursor="hand2",font=("Arial",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=330,width=120,height=35)

        #register button 
        #registerbtn=Button(frame,text="New User Register",command=self.register_window,cursor="hand2",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        #registerbtn.place(x=35,y=380,width=120)

        #forgetpassbtn
        registerbtn=Button(frame,text="Forgot Password..?",command=self.forgot_password_window,cursor="hand2",font=("times new roman",8,"bold"),borderwidth=0,fg="red",bg="black",activeforeground="red",activebackground="black")
        registerbtn.place(x=195,y=420,width=120)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="hasnath" and self.txtpass.get()=="farhan":
            messagebox.showinfo("Successful","Welcome to Hasnath Farhan")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="MHF@97611#",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            ))

            row=my_cursor.fetchone()
            #print
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                #self.root.destroy()
                open_main=messagebox.askyesno("YesNo","Access only admin",parent=self.root)
                #self.root.destroy()
                
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    #self.root.destroy()
                    self.app=Face_Recognition_System(self.new_window)
                    
                    
                else:
                    
                    if not open_main:
                        return
                        #self.root.destroy()
                        #self.root.destroy()
            
            conn.commit()
            conn.close()
           # self.root.destroy()
           # messagebox.showinfo("Success","Ok Done",parent=self.root)
   # def return_main(self):
      #  self.root.destroy()


            
            
    #=======================================reset password=================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="MHF@97611#",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())  
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset so please login new password",parent=self.root2)
                self.root2.destroy()



    #===============================================forget password window=================================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="MHF@97611#",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("320x420+930+200")

                l=Label(self.root2,text="Forgot Password",font=("Arial",16,"bold"),fg="white",bg="black")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question:",font=("Arial",12),bg="white")
                security_Q.place(x=40,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",12),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_security_Q.place(x=40,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer:",font=("Arial",12),bg="white")
                security_A.place(x=40,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("Courier",10,"bold"))
                self.txt_security.place(x=40,y=180,width=250)

                new_password=Label(self.root2,text="New Password:",font=("Arial",12),bg="white")
                new_password.place(x=40,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("Courier",10,"bold"))
                self.txt_newpass.place(x=40,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("Arial",12,"bold"),bg="red",fg="white")
                btn.place(x=110,y=290,width=100)



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ======== variables ========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #bg img
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Acer\Desktop\FAS\college_images\Teacher-with-students-1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #left img
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Acer\Desktop\FAS\college_images\employee.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=140,y=150,width=440,height=530)

        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=580,y=150,width=750,height=530)

        register_lbl=Label(frame,text="REGISTER HERE",font=("Arial",30,"bold"),fg="black",bg="white")
        register_lbl.place(x=200,y=20)

        #label and entry

        #row1
        fname=Label(frame,text="First Name:",font=("Arial",16),bg="white")
        fname.place(x=46,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("Courier",12,"bold"))
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name:",font=("Arial",16),bg="white")
        l_name.place(x=365,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Courier",12,"bold"))
        self.txt_lname.place(x=370,y=130,width=270)

        #row2
        contact=Label(frame,text="Contact No:",font=("Arial",16),bg="white")
        contact.place(x=46,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("Courier",12,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email:",font=("Arial",16),bg="white")
        email.place(x=365,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("Courier",12,"bold"))
        self.txt_email.place(x=370,y=200,width=270)

        #row3
        security_Q=Label(frame,text="Select Security Question:",font=("Arial",16),bg="white")
        security_Q.place(x=46,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer:",font=("Arial",16),bg="white")
        security_A.place(x=365,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("Courier",12,"bold"))
        self.txt_security.place(x=370,y=270,width=270)


        #row4
        pswd=Label(frame,text="Password:",font=("Arial",16),bg="white")
        pswd.place(x=46,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("Courier",12,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password:",font=("Arial",16),bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("Courier",12,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=270)

        #check button
        self.var_check=IntVar()
        Checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("Arial",10,"bold"),onvalue=1,offvalue=0,bg="white")
        Checkbtn.place(x=50,y=380)

        #buttons
        img=Image.open(r"C:\Users\Acer\Desktop\FAS\college_images\register.png")
        img=img.resize((150,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=90,y=420,width=150)

        #img1=Image.open(r"C:\Users\Acer\Desktop\FAS\college_images\back2.png")
        #img1=img1.resize((150,50),Image.ANTIALIAS)
        #self.photoimage1=ImageTk.PhotoImage(img1)
        #b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
        #b1.place(x=490,y=460,width=150)

    # =======Function declaration========

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="MHF@97611#",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)
            self.root.destroy()


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image 
        img=Image.open(r"college_images\icbt.png")
        img=img.resize((400,150),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=50,y=20,width=400,height=100)

        #second image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=530,height=130)

        #third image
        img2=Image.open(r"college_images\cardiffMetUni.png")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=980,y=0,width=530,height=130)

        #background image
        img3=Image.open(r"college_images\Teacher-with-students-1.jpg")
        img3=img3.resize((1500,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=15,y=150,width=1500,height=710)

        title_lbl=Label(bg_img,text="ICBT CAMPUS COLOMBO",font=("Arial",35,"bold"),bg="darkgrey",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"college_images\std.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        #Student Text Button
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #detect face button
        img5=Image.open(r"college_images\fad.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        #detect face text button
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        #attendance button
        img6=Image.open(r"college_images\attendant.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        #attendance text button
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        #help button
        img7=Image.open(r"college_images\helpdesk.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.newregister_data)
        b1.place(x=1100,y=100,width=220,height=220)

        #help text button
        b1_1=Button(bg_img,text="Register New Admin",cursor="hand2",command=self.newregister_data,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #train button
        img8=Image.open(r"college_images\traindata.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        #train text button
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        
        #photos button
        img9=Image.open(r"college_images\photos.jpeg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        #photos text button
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        #developer button
        img10=Image.open(r"college_images\developer.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        #developer text button
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("Arial",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        #exit button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
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


if __name__=="__main__":
    main()
    
    
