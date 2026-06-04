from tkinter import messagebox
from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
import Variables as V
from CaptureImages import capture_image
from ModelTraining import train_model
from MarkAttendance import mark_attendance
from ViewAttendance import view_logs

class Home:
    def __init__(self):
        self.window = Tk()
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d+%d+%d" % (self.width, self.height - 80, 0, 0))
        self.window.minsize(int(self.width /1.1), self.height // 2)
        self.window.configure(bg = "#F5F5F0")
        self.window.title("Face Detection Attendance System")
        self.window.state("zoomed")
        #Body
        #-----------------------------
        #Frame 1
        # SubFrame width
        self.subframe_width = self.width - 350
        self.subframe_font = ("Arial", 12)

        self.face = None

        self.f1_background = "#811844"
        self.f1 = Frame(self.window, bg = self.f1_background)
        self.f1.place(x = 0, y = 0, width = 300, height=self.height)

        self.menu = Label(self.f1,text = "Menu", fg = "white",bg = self.f1_background, font= ("Arial", 18, "bold"))
        self.menu.pack(pady = 20)

        button_font = ("Arial", 12)
        button_width = 15

        self.b1 = Button(self.f1, text="Register Student", font=button_font, width=button_width,
                         command= self.place_f11)
        self.b2 = Button(self.f1, text = "Mark Attendance",font=button_font, width = button_width, command = self.attendance)
        self.b3 = Button(self.f1, text = "Attendance Report",font=button_font, width = button_width, command = self.view)
        self.b4 = CTkButton(self.f1, text = "Exit", corner_radius=50 ,font=button_font, command= self.window.destroy)

        self.b1.pack(pady=20)
        self.b2.pack(pady=20)
        self.b3.pack(pady=20)
        self.b4.pack(pady=20)

        #Frame 2
        self.f2 = Frame(self.window, bg = 'White')
        self.f2.place(x=350, y=0, width=self.subframe_width, height=self.height)
        self.l1 = Label(self.f2, text = 'Face Detection Attendance System', font=('Arial', 30, 'bold'), bg= 'white')
        self.l1.pack(pady=40)
        self.logo = ImageTk.PhotoImage(Image.open("assets/logo.png").resize((500,500)))
        self.l2 = Label(self.f2, image = self.logo,bg = 'white')
        self.l2.pack()

        # Calling essential functions

        self.window.mainloop()

    def place_f11(self):
        # set flag value
        if not V.f11_flag:
            V.f11_flag = True

            self.f11_background = "white"
            self.f11 = Frame(self.window, bg=self.f11_background)
            self.f11.place(x=350, y=0, width=self.subframe_width, height=self.height)
            self.label = Label(self.f11, text="Register Student", font=("Arial", 18, "bold"), bg=self.f11_background)
            self.label.pack(pady=20)

            # Entry widgets
            self.l1_f11 = Label(self.f11, text="Enter Name : ",bg=self.f11_background ,font=self.subframe_font)
            self.e1_f11 = Entry(self.f11, highlightthickness=2, highlightcolor=self.f1_background, font=self.subframe_font)
            self.l2_f11 = Label(self.f11, text="Enter Roll Number : ",bg=self.f11_background, font=self.subframe_font)
            self.e2_f11 = Entry(self.f11, highlightthickness=2, highlightcolor=self.f1_background, font=self.subframe_font)
            self.clear1 = Label(self.f11, text = 'clear', font=self.subframe_font, bg=self.f1_background,fg="white")
            self.clear1.bind("<Button-1>",lambda e: self.clean1(e))
            self.clear1.bind("<Enter>", lambda e: self.onEnter(e,self.clear1))
            self.clear1.bind("<Leave>", lambda e: self.onLeave(e,self.clear1))

            self.clear2 = Label(self.f11, text = 'clear', font=self.subframe_font, bg=self.f1_background, fg="white")
            self.clear2.bind("<Button-1>", lambda e: self.clean2(e))
            self.clear2.bind("<Enter>", lambda e: self.onEnter(e,self.clear2))
            self.clear2.bind("<Leave>", lambda e: self.onLeave(e,self.clear2))

            # self.image_f11 = Label(self.f11, width=400, height=400)
            self.camera = ImageTk.PhotoImage(image = Image.open("assets/photographer.png").resize((100, 100)))
            self.b1_f11 = Button(self.f11, image=self.camera, text="Click to Capture Image", bg=self.f1_background, fg="white",
                                 font=self.subframe_font, anchor=CENTER, compound ="top",borderwidth=6,relief="raised",
                                 command = self.capture_image_samples)
            self.b2_f11 = Button(self.f11, text="Register", font=self.subframe_font,command=self.register)


            W = 270
            X,Y = 250,150
            X_diff,Y_diff =300,60
            self.l1_f11.place(x=X, y=Y,width = W)
            X+=X_diff
            self.e1_f11.place(x=X, y=Y, width = W)
            X+=X_diff
            self.clear1.place(x=X, y=Y, width = 100)
            Y+=Y_diff
            X=250
            self.l2_f11.place(x=X, y=Y, width = W)
            X+=X_diff
            self.e2_f11.place(x=X, y=Y,width = W)
            X+=X_diff
            self.clear2.place(x=X, y=Y,width = 100)
            Y+=Y_diff
            X=250
            self.b1_f11.place(x=X+200,y=Y,width= W+100,height=150)
            self.b2_f11.place(x=X+200,y=Y+200,width= W+100,)

    def clean1 (self,e):
        self.e1_f11.delete(0, END)

    def clean2(self,e):
        self.e2_f11.delete(0, END)

    def onEnter(self,e,widget):
        widget.config(font=("Arial", 12, "bold"))
    def onLeave(self,e,widget):
        widget.config(font = self.subframe_font)

    def capture_image_samples(self):
        name = self.e1_f11.get()
        roll = self.e2_f11.get()
        path = V.path
        ids = []
        names = []
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        for image_path in image_paths:
            student_id = int(os.path.split(image_path)[-1].split(".")[1])
            student_name = os.path.split(image_path)[-1].split(".")[0]
            ids.append(student_id)
            names.append(student_name)

        if not name:
                messagebox.showwarning("Warning", "Enter name.")
        elif not roll:
                messagebox.showwarning("Warning", "Enter roll number.")
        elif int(roll) in ids or name in names:
            messagebox.showwarning("Warning", "Student Already Registered.")
        elif not name.replace(" ", "").isalpha():
                messagebox.showwarning("Warning", "Name should contain only alphabets.")
        elif not roll.isdigit():
                messagebox.showwarning("Warning", "Roll number should be numeric.")
        elif len(roll) != 3:
                messagebox.showwarning("Warning", "Roll number should contain three digits.")
        else:
                capture_image(roll,name)

    def register(self):
        name = self.e1_f11.get()
        roll = self.e2_f11.get()
        if not name:
            messagebox.showwarning("Warning", "Enter name.")

        elif not name.replace(" ", "").isalpha():
            messagebox.showwarning("Warning", "Name should contain only alphabets.")

        elif not roll:
            messagebox.showwarning("Warning", "Enter roll number.")

        elif not roll.isdigit():
            messagebox.showwarning("Warning", "Roll number should be numeric.")

        if len(roll)!=3:
            messagebox.showwarning("Warning", "Roll number should contain three digits.")

        if not V.capture_flag:
            messagebox.showwarning("Warning", "Capture image First.")
        else:
            V.capture_flag = False
            train_model()
            messagebox.showinfo("Success", "Registration Successful.")
            try :
                self.connect_db()
                self.curr.execute("insert into students values (%s,%s)",(roll,name))
                self.conn.commit()
            except Exception as e:
                messagebox.showerror("Database Error", "Connect the Database .")

            self.e1_f11.delete(0,END)
            self.e2_f11.delete(0,END)
            self.e1_f11.focus()

    def connect_db(self):
        import pymysql
        try:
            self.conn = pymysql.connect(host=V.host, user=V.user, password=V.password, database=V.database)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error while connecting to the database :\n" + str(e),
                                 parent=self.window)

    def attendance(self):
        mark_attendance()

    def view(self):
        view_logs()

if __name__ == "__main__":
    app = Home()