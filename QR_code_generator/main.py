# Libraries
from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

# Define the Class
class Personal_QR:
    def __init__(self,ws):
        self.ws = ws

        # Defining Basic Geometry
        self.ws.geometry("900x500+200+50")
        self.ws.resizable(False, False)   # To disable the resizable property of the window
        self.ws.configure(bg = '#03a9fc')

        # Defining Layout
        self.ws.title("Health SOS Generator | Developed by rookieML")
        title = Label(self.ws,
                        text = 'Health Card QR Generator',
                        font = ('Courier', 30),
                        bg = '#034efc',
                        fg = 'yellow').place(x=0,y=0,relwidth=1)

        #======== Personal Details Window ==========#
        per_frame = Frame(self.ws,
                            bd = 2,
                            bg = 'white',
                            relief = RIDGE)

        per_frame.place(x=30, y=80, width=500, height=380)

        per_title = Label(per_frame,
                        text = 'Personal Details',
                        font = ('Giddyup Std', 17),
                        bg = '#fc0349',
                        fg = 'yellow')
        per_title.place(x=0,y=0,relwidth=1)

        ##========= Defining Variables =========##
        self.var_name = StringVar()
        self.var_bg = StringVar()
        self.var_med_cond = StringVar()
        self.var_allrg = StringVar()
        self.var_em_name = StringVar()
        self.var_em_num = StringVar()
        self.var_smk = StringVar()

        ##======= Entry Labels =========##
        lbl_name = Label(per_frame,
                        text = 'Name:',
                        font = ('Prestige Elite Std', 10, 'bold'),
                        bg = 'white')
        lbl_name.place(x=50,y=60)

        lbl_bg = Label(per_frame,
                        text = 'Blood Group:',
                        font = ('Prestige Elite Std', 10, 'bold'),
                        bg = 'white')
        lbl_bg.place(x=50,y=95)

        lbl_med_cond = Label(per_frame,
                        text = 'Existing Medical Conditions:',
                        font = ('Prestige Elite Std', 10, 'bold'),
                        bg = 'white')
        lbl_med_cond.place(x=50,y=125)

        lbl_allrg = Label(per_frame,
                        text = 'Allergies:',
                        font = ('Prestige Elite Std', 10, 'bold'),
                        bg = 'white')
        lbl_allrg.place(x=50,y=155)

        lbl_em_name = Label(per_frame,
                        text = 'Emergency Contact Name:',
                        font = ('Prestige Elite Std', 10, 'bold'),
                        bg = 'white')
        lbl_em_name.place(x=50,y=185)

        lbl_em_num = Label(per_frame,
                        text = 'Emergency Contact Number:',
                        font = ('Prestige Elite Std', 10, 'bold'),
                        bg = 'white')
        lbl_em_num.place(x=50,y=215)

        lbl_smk = Label(per_frame,
                        text = 'Smoker:',
                        font = ('Prestige Elite Std', 10, 'bold'),
                        bg = 'white')
        lbl_smk.place(x=50,y=245)


        ##======= Entry Fields =========##
        txt_name = Entry(per_frame,
                        font = ('Prestige Elite Std', 10),
                        bg = 'lightyellow', 
                        textvariable = self.var_name)
        txt_name.place(x=250,y=60)

        txt_bg = Entry(per_frame,
                        font = ('Prestige Elite Std', 10),
                        bg = 'lightyellow',
                        textvariable = self.var_bg)
        txt_bg.place(x=250,y=95)

        txt_med_cond = Entry(per_frame,
                        font = ('Prestige Elite Std', 10),
                        bg = 'lightyellow',
                        textvariable = self.var_med_cond)
        txt_med_cond.place(x=250,y=125)

        txt_allrg = Entry(per_frame,
                        font = ('Prestige Elite Std', 10),
                        bg = 'lightyellow',
                        textvariable = self.var_allrg)
        txt_allrg.place(x=250,y=155)

        txt_em_name = Entry(per_frame,
                        font = ('Prestige Elite Std', 10),
                        bg = 'lightyellow',
                        textvariable = self.var_em_name)
        txt_em_name.place(x=250,y=185)

        txt_em_num = Entry(per_frame,
                        font = ('Prestige Elite Std', 10),
                        bg = 'lightyellow',
                        textvariable = self.var_em_num)
        txt_em_num.place(x=250,y=215)

        txt_smk = Entry(per_frame,
                        font = ('Prestige Elite Std', 10),
                        bg = 'lightyellow',
                        textvariable = self.var_smk)
        txt_smk.place(x=250,y=245)

        
        ##======= Defining Buttons =========##
        btn_generate = Button(per_frame,
                                text = 'Generate QR',
                                font = ('times new roman', 18, 'bold'),
                                bg = '#03fcf4',
                                fg = 'green',
                                command = self.generate_QR)
        btn_generate.place(x=100, y=285, width=150, height=30)

        btn_clear = Button(per_frame,
                                text = 'Clear',
                                font = ('times new roman', 18, 'bold'),
                                bg = '#03fcf4',
                                fg = 'red',
                                command = self.clear)
        btn_clear.place(x=285, y=285, width=100, height=30)

        ##======= Defining System Messages =========##
        self.msg = ''
        self.lbl_msg = Label(per_frame,
                        text = self.msg,
                        font = ('Charlemagne Std', 18),
                        bg = 'white',
                        fg = 'green')
        self.lbl_msg.place(x=50, y=325, relwidth=1)


        #======== QR Generated Window ==========#
        qr_frame = Frame(self.ws,
                            bd = 2,
                            bg = 'white',
                            relief = RIDGE)

        qr_frame.place(x=600, y=80, width=270, height=380)

        qr_title = Label(qr_frame,
                        text = 'QR Code',
                        font = ('Giddyup Std', 17),
                        bg = '#fc0349',
                        fg = 'yellow')
        qr_title.place(x=0,y=0,relwidth=1)

        self.qr_frame = Label(qr_frame,
                                text = 'No QR\nGenerated',
                                font = ('times new roman', 15),
                                bg = '#73736A',
                                fg = '#DBDB0B',
                                bd = 1, 
                                relief = RIDGE)
        self.qr_frame.place(x=50, y=100, width=180, height=180)

    # Main Function to Generate QR Code
    def generate_QR(self):
        if self.var_name.get()=='' or self.var_bg.get()=='' or self.var_med_cond.get()=='' or self.var_allrg.get()=='' or self.var_em_name.get()=='' or self.var_em_num.get()=='' or self.var_smk.get()=='':
            self.msg = 'All Fields are Required!!'
            self.lbl_msg.config(text = self.msg, fg = 'red')
        else:
            qr_data = (f'Name: {self.var_name.get()}\nBlood Group: {self.var_bg.get()}\nExisting Medical Condition: {self.var_med_cond.get()}\nAllergies: {self.var_allrg.get()}\nEmergency Contact Name: {self.var_em_name.get()}\nEmergency Contact Number: {self.var_em_num.get()}\nSmoker: {self.var_smk.get()}')
            qr_code = qrcode.make(qr_data)

            #####========= Saving QR Image =========#######
            qr_code = resizeimage.resize_cover(qr_code, [180,180] )
            qr_code.save("Health Card QR of "+ str(self.var_name.get())+'.png')
            
            #####========= Updating QR Image =========#######
            self.im = ImageTk.PhotoImage(file = "Health Card QR of "+ str(self.var_name.get())+'.png')
            self.qr_frame.config(image=self.im)

            #####========= Updating Notifications =========######
            self.msg = 'QR Generated Successfully!!!'
            self.lbl_msg.config(text = self.msg, fg = 'green')

    # Clear Button Functionality
    def clear(self):
        self.var_name.set('')
        self.var_bg.set('')
        self.var_med_cond.set('')
        self.var_allrg.set('')
        self.var_em_name.set('')
        self.var_em_num.set('')
        self.var_smk.set('')
        self.msg = ''
        self.lbl_msg.config(text = self.msg, fg = 'red')
        self.qr_frame.config(image='')


# Defining Objects
ws = Tk()
obj = Personal_QR(ws)

# Execution
ws.mainloop()