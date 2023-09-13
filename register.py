from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   #pip install pillow
from tkinter import messagebox
import mysql.connector



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
        # img=img.resize((150,50),Image.ANTIALIAS)
        img = img.resize((150, 50), Image.LANCZOS)
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
            messagebox.showinfo("Success","Register Successfully")


    #def return_main(self):
      #  self.root.destroy()
                                                                         

                    
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()