#Bank Management System by TacoUdit
from tkinter import *
import datetime
import sqlite3 as sq
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

date = datetime.datetime.now().date()
date = str(date)
conn=sq.connect("database")

class Application(object):
    def __init__(self , master):
        self.master = master
        self.date = datetime.date.today().strftime("%B %d, %Y")
        self.time = datetime.datetime.now().strftime('%I:%M %p')
        #frames        
        self.top = Frame(master,height = 150,bg = 'white')
        self.top.pack(fill = X)
        self.buttom = Frame(self.master,height = 500,bg = '#66cccc')
        self.buttom.pack(fill = X)

       
        # Top frame designs
        self.top_img = PhotoImage(file = 'icons/logo8000.png')
        self.top_img_label = Label(self.top, image = self.top_img, bg = 'white')
        self.top_img_label.place(x= 120, y =25)

        self.heading = Label(self.top, text = 'Bank Management System', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
        self.heading.place(x= 200,y = 40)
        
        self.date = Label(self.top,text= 'Date: '+date, font ='arial 12 bold', bg='white', fg = '#52bfe3')
        self.date.place(x= 500, y = 110)

        # buttons #create account
        def click_btn1():
            
            #self.buttom.destroy()
            self.label1 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label1.place(x=0,y=150)
            self.heading1 = Label(self.top, text = 'Create Account', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading1.place(x= 250,y = 110)
            #labels##############################
            i = IntVar()
            label_name = Label(self.label1,text = "Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 30)
            label_age = Label(self.label1,text = "Age",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 60)
            label_mobno = Label(self.label1,text = "Mob. No.",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 90)
            label_gender = Label(self.label1,text = 'Gender',bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 150)
            r1 = Radiobutton(self.label1,text = 'Male', value = 'Male',variable = i,bg ="#66cccc",font = 'arial 12 bold')
            r2 = Radiobutton(self.label1,text = 'Female', value = 'Female',variable = i,bg ="#66cccc",font = 'arial 12 bold')
            r1.place(x = 295,y = 150)
            r2.place(x= 380,y = 150)
            label_mail = Label(self.label1,text = 'E-Mail',bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 120)
            label_address = Label(self.label1,text = 'Address',bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 180)
            label_aadhar = Label(self.label1,text = 'Aadhar No.',bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 280)
            label_amount = Label(self.label1,text = 'Amount',bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 310)
            # Entries 
            ent_name = Entry(self.label1,width=30)
            ent_name.place(x=285,y=33)
            ent_age = Entry(self.label1,width=30)
            ent_age.place(x=285,y=63)
            ent_mobno = Entry(self.label1,width=30)
            ent_mobno.place(x=285,y=93)
            ent_mail = Entry(self.label1,width=30)
            ent_mail.place(x=285,y=123)
            ent_add = Text(self.label1 , height = 5 , width =23)
            ent_add.place(x=285,y=183)
            ent_aad = Entry(self.label1,width=30)
            ent_aad.place(x=285,y=283)
            ent_amount = Entry(self.label1,width=30)
            ent_amount.place(x=285,y=313)
            # get all the datas
            def get_data():
                conn.execute("create table if not exists data(Name varchar,Age varchar,Mob_no varchar,Mail varchar,Address varchar,Aadhar varchar,Amount varchar,Acno varchar primary key);")
                conn.commit()
                data_name = (ent_name.get())
                data_age = (ent_age.get())
                data_mobno = (ent_mobno.get())
                data_mail = (ent_mail.get())
                data_add =(ent_add.get('1.0',END))
                data_aad = (ent_aad.get())
                data_amount = (ent_amount.get())
                list_data = []
                if (data_name) == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")                   
                elif (data_age) == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif (data_mobno) == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif (data_mail) == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif (data_add) == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif (data_aad) == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif (data_amount) == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif type(data_name) == str:
                    list_data.append(1)
                    messagebox.showinfo("Bank Management System","Account created successfully !")
                elif type(data_age) == str:
                    list_data.append(1)
                    messagebox.showinfo("Bank Management System","Account created successfully !")
                elif type(data_mobno) == str:
                    list_data.append(1)
                    messagebox.showinfo("Bank Management System","Account created successfully !")
                elif type(data_mail) == str:
                    list_data.append(1)
                    messagebox.showinfo("Bank Management System","Account created successfully !")
                elif type(data_add) == str:
                    list_data.append(1)
                    messagebox.showinfo("Bank Management System","Account created successfully !")
                elif type(data_amount) == str:
                    list_data.append(1)
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif type(data_aad) == str:
                    list_data.append(1)
                    messagebox.showinfo("Bank Management System","Account created successfully !")
                #generate account number
                fact = 0
                convert_sort = (data_aad[0:4])
                aad_str = int(convert_sort)
                for i in range (1,aad_str+1):
                    fact = fact +10 * 66663
                convert_str = str(fact)
                ac_no = (convert_str[0:4])

                #check for acno
                pre_result = ("SELECT Acno FROM data")
                result = conn.execute(pre_result)
                for i in result:
                    for j in (i):
                        j = j
                    if str(ac_no) in j:
                        ac_no = int(ac_no)
                        ac_no = ac_no + 29
                    else:
                        ac_no = ac_no
                try:
                    insert_values = ("insert into data values(%a,%a,%a,%a,%a,%a,%a,%a)"%(data_name,data_age,data_mobno,data_mail,data_add,data_aad,data_amount,ac_no))
                    conn.execute(insert_values)
                    conn.commit()
                    # create passbook
                    create_pass = ("Create table if not exists p%d (Date varchar,Time Varchar,Particulars varchar,Dr varchar,Cr varchar,Balance varchar)"%(ac_no))
                    conn.execute(create_pass)
                    conn.commit()
                    #insert values
                    self.date = datetime.date.today().strftime("%B %d, %Y")
                    self.time = datetime.datetime.now().strftime('%I:%M %p')
                    Dr = '-'
                    part = ('New Account Created')
                    insert_val = ("insert into p%d values(%a,%a,%a,%a,%a,%a)"%(ac_no,self.date,self.time,part,Dr,data_amount,data_amount))
                    print(insert_val)
                    conn.execute(insert_val)
                    conn.commit()
                except:
                    ac_no = int(ac_no) + 29
                    conn.execute("create table if not exists data(Name varchar,Age varchar,Mob_no varchar,Mail varchar,Address varchar,Aadhar varchar,Amount varchar,Acno varchar primary key);")
                    insert_values = ("insert into data values(%a,%a,%a,%a,%a,%a,%a,%a)"%(data_name,data_age,data_mobno,data_mail,data_add,data_aad,data_amount,ac_no))
                    conn.execute(insert_values)
                    conn.commit()
                    # create passbook
                    create_pass = ("Create table if not exists p%d (Date varchar,Time Varchar,Particulars varchar,Dr varchar,Cr varchar,Balance varchar)"%(ac_no))
                    conn.execute(create_pass)
                    conn.commit()
                    #insert values
                    self.date = datetime.date.today().strftime("%B %d, %Y")
                    self.time = datetime.datetime.now().strftime('%I:%M %p')
                    Dr = '-'
                    part = ('New Account Created')
                    insert_val = ("insert into p%d values(%a,%a,%a,%a,%a,%a)"%(ac_no,self.date,self.time,part,Dr,data_amount,data_amount))
                    conn.execute(insert_val)
                    conn.commit()
                  
                ab = ("Remember your Account Number %a") %(ac_no)
                messagebox.showinfo("Bank Management System",ab)
                if sum(list_data) == 1:
                    self.label1.destroy()
                    self.heading1.destroy()
                    btn_back.destroy()
            self.create_account = Button(self.label1 , text =  'Create Account',width = 13 , fg = '#1c9eb8', font = 'arial 12 bold', command= get_data)
            self.create_account.place(x=305, y = 350)
            def back():
                self.label1.destroy()
                self.heading1.destroy()
                btn_back.destroy()
            btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
            btn_back.place(x=5,y=115)
            
        self.btn1 = Button(self.buttom , text =  'Create Account',width = 13 , fg = '#1c9eb8', font = 'arial 12 bold', command= click_btn1)
        self.btn1.place(x=250, y = 30)
        # Deposit money
        def click_btn2():
            self.label2 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label2.place(x=0,y=150)
            self.heading2 = Label(self.top, text = 'Deposit Money', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading2.place(x= 250,y = 110)
            
            #labels
            label_name = Label(self.label2,text = "Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 80)
            label_acno = Label(self.label2,text = "Account No.",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 110)
            label_amount = Label(self.label2,text = "Amount",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 140)
            # Entries
            ent_name = Entry(self.label2,width=30)
            ent_name.place(x=295,y=83)
            ent_acno = Entry(self.label2,width=30)
            ent_acno.place(x=295,y=113)
            ent_amount = Entry(self.label2,width=30)
            ent_amount.place(x=295,y=143)
            def get_data():
                data_acno = (ent_acno.get())
                data_amount = (ent_amount.get())
                if data_acno == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif data_amount == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif type(data_acno and data_amount) == str:
                    ab = ("Rupees %a Deposited to your Account") %(data_amount)
                    messagebox.showinfo("Bank Management System",ab)
                    #data to database
                    command = ("update data set amount = amount + %a where Acno = %a") %(data_amount,data_acno)
                    conn.execute(command)
                    conn.commit()
                    #insert values
                    pre_result = ("SELECT AMOUNT FROM data WHERE acno = %a")%(data_acno)
                    result = conn.execute(pre_result)
                    for i in result:
                        for amount in (i):
                            amount = amount
                    self.date = datetime.date.today().strftime("%B %d, %Y")
                    self.time = datetime.datetime.now().strftime('%I:%M %p')
                    Dr = '-'
                    part = ('Rs %a Deposited')%(data_amount)
                    insert_val = ("insert into p%d values(%a,%a,%a,%a,%a,%a)"%(int(data_acno),self.date,self.time,part,Dr,data_amount,amount))
                    print(insert_val)
                    conn.execute(insert_val)
                    conn.commit()
                    self.label2.destroy()
                    self.heading2.destroy()
                    btn_back.destroy()
            self.Deposit_Money = Button(self.label2 , text =  'Deposit Money',width = 13 , fg = '#1c9eb8', font = 'arial 12 bold',command = get_data)
            self.Deposit_Money.place(x=305, y = 200)
            def back():
                self.label2.destroy()
                self.heading2.destroy()
                btn_back.destroy()
            
            btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
            btn_back.place(x=5,y=115)
        
        self.btn2 = Button(self.buttom , text = 'Deposit Money' ,width = 13, fg = '#1c9eb8', font = 'arial 12 bold',command = click_btn2)
        self.btn2.place(x=250, y = 70)
        # Transfer money
        def click_btn3():
            self.label1 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label1.place(x=0,y=150)
            self.heading1 = Label(self.top, text = 'Transfer Money', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading1.place(x= 250,y = 110)
            self.label_from = Label(self.label1,text='From',font = 'arial 15 bold', bg = '#66cccc', fg = 'white')
            self.label_from.place(x = 300,y = 20)
            #labels From
            label_name = Label(self.label1,text = "Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 80)
            label_acno = Label(self.label1,text = "Account No.",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 110)
            label_amount = Label(self.label1,text = "Amount",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 140)
            #Entries From
            ent_name = Entry(self.label1,width=30)
            ent_name.place(x=295,y=83)
            ent_acno = Entry(self.label1,width=30)
            ent_acno.place(x=295,y=113)
            ent_amount = Entry(self.label1,width=30)
            ent_amount.place(x=295,y=143)
            self.label_to = Label(self.label1,text='To',font = 'arial 15 bold', bg = '#66cccc', fg = 'white')
            self.label_to.place(x = 300,y = 180)
            # labels To
            label_name_to = Label(self.label1,text = "Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 220)
            label_acno_to = Label(self.label1,text = "Account No.",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 250)
            label_amount_to = Label(self.label1,text = "Remarks",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 280)
            #Entries to
            ent_name_to = Entry(self.label1,width=30)
            ent_name_to.place(x=295,y=220)
            ent_acno_to = Entry(self.label1,width=30)
            ent_acno_to.place(x=295,y=250)
            ent_amount_to = Entry(self.label1,width=30)
            ent_amount_to.place(x=295,y=280)
            def transfer():
                from_ent_acno = (ent_acno.get())
                from_ent_amount = (ent_amount.get())
                to_ent_acno_to = (ent_acno_to.get())
                if from_ent_acno == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif from_ent_amount  == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif to_ent_acno_to  == '':
                    messagebox.showerror("Bank Management System","All fields are necessary !")
                elif type(to_ent_acno_to) and type(from_ent_amount) and type(from_ent_acno)   == str:
                    command = ("update data set amount = amount - %a where acno = %a") %(from_ent_amount,from_ent_acno)
                    conn.execute(command)
                    pre_result = ("update data set amount = amount + %a where acno = %a") %(from_ent_amount,to_ent_acno_to)
                    result = conn.execute(pre_result)
                    conn.commit()
                    #_______________________________
                    #insert values
                    pre_result = ("SELECT AMOUNT FROM data WHERE acno = %a")%(from_ent_acno)
                    result = conn.execute(pre_result)
                    for i in result:
                        for amount in (i):
                            amount = amount
                    self.date = datetime.date.today().strftime("%B %d, %Y")
                    self.time = datetime.datetime.now().strftime('%I:%M %p')
                    Dr = from_ent_amount
                    Cr = '-'
                    part = ('Rs %a Transferred')%(from_ent_amount)
                    insert_val = ("insert into p%d values(%a,%a,%a,%a,%a,%a)"%(int(from_ent_acno),self.date,self.time,part,Dr,Cr,amount))
                    print(insert_val)
                    conn.execute(insert_val)
                    conn.commit()
                    #_______________________________
                    transfer = 'Money transferred to %a' %(to_ent_acno_to)
                    messagebox.showinfo("Bank Management System",transfer)
                    self.label1.destroy()
                    self.heading1.destroy()
                    btn_back.destroy()
            self.transfer_money = Button(self.label1 , text = 'Transfer Money' ,width = 13, fg = '#1c9eb8', font = 'arial 12 bold',command = transfer)
            self.transfer_money.place(x=260, y = 330)
            def back():
                self.label1.destroy()
                self.heading1.destroy()
                btn_back.destroy()
            btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
            btn_back.place(x=5,y=115)
        self.btn3 = Button(self.buttom , text = 'Transfer Fund' ,width = 13,fg = '#1c9eb8', font = 'arial 12 bold',command = click_btn3)
        self.btn3.place(x=250, y = 110)
        # withdraw money
        def click_btn4():
            self.label1 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label1.place(x=0,y=150)
            self.heading1 = Label(self.top, text = 'Withdraw Money', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading1.place(x= 250,y = 110)
            #labels
            label_name = Label(self.label1,text = "Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 80)
            label_acno = Label(self.label1,text = "Account No.",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 110)
            label_amount = Label(self.label1,text = "Amount",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 140)
            # Entries
            ent_name = Entry(self.label1,width=30)
            ent_name.place(x=295,y=83)
            ent_acno = Entry(self.label1,width=30)
            ent_acno.place(x=295,y=113)
            ent_amount = Entry(self.label1,width=30)
            ent_amount.place(x=295,y=143)
            def withdraw():
                data_ent_acno = (ent_acno.get())
                data_ent_amount = (ent_amount.get())
                if data_ent_acno == '' and data_ent_amount == '':
                    messagebox.showerror("Bank Management System",'Fields cannot be empty')
                elif type(data_ent_acno) and type (data_ent_amount) == str:
                
                    command = ("update data set amount = amount - %a where acno = %a") %(data_ent_amount,data_ent_acno)
                    conn.execute(command)
                    conn.commit()
                    transfer = 'Money Withdrawn Rupees %a' %(data_ent_amount)
                    messagebox.showinfo("Bank Management System",transfer)
                    #_________________________________________
                    #insert values
                    pre_result = ("SELECT AMOUNT FROM data WHERE acno = %a")%(data_ent_acno)
                    result = conn.execute(pre_result)
                    for i in result:
                        for amount in (i):
                            amount = amount
                    self.date = datetime.date.today().strftime("%B %d, %Y")
                    self.time = datetime.datetime.now().strftime('%I:%M %p')
                    Dr = data_ent_amount
                    Cr = '-'
                    part = ('Rs %a Withdrawn')%(data_ent_amount)
                    insert_val = ("insert into p%d values(%a,%a,%a,%a,%a,%a)"%(int(data_ent_acno),self.date,self.time,part,Dr,Cr,amount))
                    print(insert_val)
                    conn.execute(insert_val)
                    conn.commit()
                    #_________________________________________
                    self.label1.destroy()
                    self.heading1.destroy()
                    btn_back.destroy()
            self.withdraw_money = Button(self.label1 , text = 'Withdraw Money' ,width = 13, fg = '#1c9eb8', font = 'arial 12 bold',command = withdraw)
            self.withdraw_money.place(x=260, y = 250)
            def back():
                self.label1.destroy()
                self.heading1.destroy()
                btn_back.destroy()
            btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
            btn_back.place(x=5,y=115)
        self.btn4 = Button(self.buttom , text = 'Withdraw Money',width = 13 ,fg = '#1c9eb8',font = 'arial 12 bold',command = click_btn4)
        self.btn4.place(x=250, y = 150)
        # Balance Enquiry
        def click_btn5():
            self.label1 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label1.place(x=0,y=150)
            self.heading1 = Label(self.top, text = 'Balance Enquiry', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading1.place(x= 250,y = 110)
            #labels
            label_name = Label(self.label1,text = "Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 80)
            label_acno = Label(self.label1,text = "Account No.",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 110)
            # Entries
            ent_name = Entry(self.label1,width=30)
            ent_name.place(x=295,y=83)
            ent_acno = Entry(self.label1,width=30)
            ent_acno.place(x=295,y=113)
            def enquiry():
                data_ent_acno = (ent_acno.get())
                if data_ent_acno  == '':
                    messagebox.showerror("Bank Management System",'Fields cannot be empty')
                else:
                    self.label2 = Label(master,width=300,height = 500,bg = '#66cccc')
                    self.label2.place(x=0,y=150)
                    self.heading2 = Label(self.top, text = 'Balance Enquiry', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
                    self.heading2.place(x= 250,y = 110)
                    label_name = Label(self.label2,text = 'Name    :',bg ="#66cccc",fg = 'white',font = 'arial 20 bold').place(x = 150,y = 100)
                    label_balance = Label(self.label2,text = 'Balance : ₹',bg ="#66cccc",fg = 'white',font = 'arial 20 bold').place(x = 150,y = 150)
                    write = ("select name from data where acno = %a") %(data_ent_acno)
                    result = conn.execute(write)
                    for i in result:
                        for j in (i) :
                            label_name = Label(self.label2,text = j,bg ="#66cccc",fg = 'white',font = 'arial 20 bold').place(x = 280,y = 100)
                    write = ("select amount from data where acno = %a") %(data_ent_acno)
                    result = conn.execute(write)
                    for i in result:
                        for j in (i) :
                            label_name = Label(self.label2,text = j,bg ="#66cccc",fg = 'white',font = 'arial 20 bold').place(x = 300,y = 150)
                    def back1():
                        self.label2.destroy()
                        self.heading2.destroy()
                        btn_back.destroy()
                    btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back1)
                    btn_back.place(x=5,y=115)
            self.enquiry = Button(self.label1 , text = 'Balance Enquiry' ,width = 13, fg = '#1c9eb8', font = 'arial 12 bold',command = enquiry)
            self.enquiry.place(x=260, y = 250)
            def back():
                self.label1.destroy()
                self.heading1.destroy()
                btn_back.destroy()
            btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
            btn_back.place(x=5,y=115)
        self.btn5 = Button(self.buttom , text = 'Balance Enquiry' ,width = 13,fg = '#1c9eb8', font = 'arial 12 bold',command = click_btn5)
        self.btn5.place(x=250, y = 190)
        # Delete Account
        def click_btn6():
            self.label1 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label1.place(x=0,y=150)
            self.heading1 = Label(self.top, text = 'Delete Account', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading1.place(x= 250,y = 110)
            #labels
            label_name = Label(self.label1,text = "Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 80)
            label_acno = Label(self.label1,text = "Account No.",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 110)
            # Entries
            ent_name = Entry(self.label1,width=30)
            ent_name.place(x=295,y=83)
            ent_acno = Entry(self.label1,width=30)
            ent_acno.place(x=295,y=113)
            def delete():
                data_ent_acno = (ent_acno.get())
                if data_ent_acno == '':
                    messagebox.showerror("Bank Management System",'Fields cannot be empty!')
                else:
                    command = ("delete from data where  acno = %a") %(data_ent_acno)
                    conn.execute(command)
                    conn.commit()
                    messagebox.showinfo("Bank Management System",'Account sucessfully deleted !')
                    self.label1.destroy()
                    self.heading1.destroy()
                    btn_back.destroy()
            self.delete = Button(self.label1 , text = 'Delete Account' ,width = 13, fg = '#1c9eb8', font = 'arial 12 bold',command = delete)
            self.delete.place(x=260, y = 250)
            def back():
                self.label1.destroy()
                self.heading1.destroy()
                btn_back.destroy()
            btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
            btn_back.place(x=5,y=115)
        self.btn6 = Button(self.buttom , text = 'Delete Account',width = 13 ,fg = '#1c9eb8', font = 'arial 12 bold',command = click_btn6)
        self.btn6.place(x=250, y = 230)
        #more
        def click_btn7():
            self.label1 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label1.place(x=0,y=150)
            self.heading1 = Label(self.top, text = '  More', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading1.place(x= 290,y = 110)
            def passbook():
                self.label2 = Label(master,width=300,height = 500,bg = '#66cccc')
                self.label2.place(x=0,y=150)
                self.heading2 = Label(self.top, text = 'Passbook', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
                self.heading2.place(x= 270,y = 110)
                # labels
                label_name = Label(self.label2,text = "Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 80)
                label_acno = Label(self.label2,text = "Account No.",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 110)
                # Entries
                ent_name = Entry(self.label2,width=30)
                ent_name.place(x=295,y=83)
                ent_acno = Entry(self.label2,width=30)
                ent_acno.place(x=295,y=111)
                def check_passbook():
                    #___________________________________________________________
                    acno = ent_acno.get()
                    if acno == '':
                        messagebox.showerror('Bank Management System','Fields cannot be empty !')
                    else:
                        try:
                            self.label3 = Label(master,width=300,height = 500,bg = 'white')
                            self.label3.place(x=0,y=150)
                            self.heading3 = Label(self.top, text = 'Passbook', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
                            self.heading3.place(x= 270,y = 110)    
                            self.label_headings = Label(self.label3,text = '      Date\t          \
      Time\t\
              Particulars\t\
            Dr.\t\
        Cr.\t             Balance',fg ='black',bg='White',font =("helvetica",'10','bold')).place(x=10,y=10)
                            #date
                            fetch_data3= ("select Date from p%d")%(int(acno))
                            write1 = pd.read_sql(fetch_data3,conn)
                            label_passbook1 = Label(self.label3,text = write1,bg = 'white',font =("helvetica",'10')).place(x = 0,y = 50)
                            label_label_passbook1 = Label(self.label3,height=1000,width=1,bg='white').place(x=0,y=30)
                            label_label_passbook2 = Label(self.label3,text='2019',height=1,width=12,bg='white').place(x=0,y=50)
                            # Time
                            fetch_data1= ("select time from p%d")%(int(acno))
                            write1 = pd.read_sql(fetch_data1,conn)
                            label_passbook1 = Label(self.label3,text = write1,bg = 'white',font =("helvetica",'10')).place(x = 100,y = 50)
                            label_label_passbook1 = Label(self.label3,height=1000,width=4,bg='white').place(x=80,y=30)
                            label_label_passbook2 = Label(self.label3,height=1,width=10,bg='white').place(x=100,y=50)
                            # particulars
                            fetch_data2= ("select particulars from p%d")%(int(acno))
                            write2 = pd.read_sql(fetch_data2,conn)
                            label_passbook1 = Label(self.label3,text = write2,bg = 'white',font =("helvetica",'10')).place(x = 190,y = 50)
                            label_label_passbook1 = Label(self.label3,height=1000,width=2,bg='white').place(x=188,y=30)
                            label_label_passbook2 = Label(self.label3,height=1,width=20,bg='white').place(x=210,y=50)
                            #Dr
                            fetch_data4= ("select Dr from p%d")%(int(acno))
                            write1 = pd.read_sql(fetch_data4,conn)
                            label_passbook1 = Label(self.label3,text = write1,bg = 'white',font =("helvetica",'10')).place(x = 380,y = 50)
                            label_label_passbook1 = Label(self.label3,height=1000,width=1,bg='white').place(x=380,y=30)
                            label_label_passbook2 = Label(self.label3,height=1,width=5,bg='white').place(x=380,y=50)
                            #cr
                            fetch_data4= ("select cr from p%d")%(int(acno))
                            write1 = pd.read_sql(fetch_data4,conn)
                            label_passbook1 = Label(self.label3,text = write1,bg = 'white',font =("helvetica",'10')).place(x = 470,y = 50)
                            label_label_passbook1 = Label(self.label3,height=1000,width=1,bg='white').place(x=473,y=30)
                            label_label_passbook2 = Label(self.label3,height=1,width=5,bg='white').place(x=470,y=50)
                            #balance
                            fetch_data4= ("select balance from p%d")%(int(acno))
                            write1 = pd.read_sql(fetch_data4,conn)
                            label_passbook1 = Label(self.label3,text = write1,bg = 'white',font =("helvetica",'10')).place(x = 560,y = 50)
                            label_label_passbook1 = Label(self.label3,height=1000,width=2,bg='white').place(x=560,y=30)
                            label_label_passbook2 = Label(self.label3,height=1,width=10,bg='white').place(x=560,y=50)

                            canvas1 = Canvas(self.label3,height=1000,width=1,bg='black').place(x=100,y=5)
                            canvas2 = Canvas(self.label3,height=1000,width=1,bg='black').place(x=190,y=5)
                            canvas3 = Canvas(self.label3,height=1000,width=1,bg='black').place(x=350,y=5)
                            canvas4 = Canvas(self.label3,height=1000,width=1,bg='black').place(x=450,y=5)
                            canvas5 = Canvas(self.label3,height=1000,width=1,bg='black').place(x=540,y=5)
                            canvas6 = Canvas(self.label3,height=1,width=1000,bg='black').place(x=0,y=4)
                            canvas7 = Canvas(self.label3,height=1,width=1000,bg='black').place(x=0,y=40)
                        except:
                            messagebox.showerror('Bank Management System','No such account !')
                    # ________________________________________________________
                    def back():
                        self.label3.destroy()
                        self.heading3.destroy()
                        btn_back.destroy()
                    btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
                    btn_back.place(x=5,y=115)
                self.inner_passbook = Button(self.label2 , text = 'Check Passbook' ,width = 13, fg = '#1c9eb8', font = 'arial 12 bold',command = check_passbook)
                self.inner_passbook.place(x=260, y = 250)
                def back():
                    self.label2.destroy()
                    self.heading2.destroy()
                    btn_back.destroy()
                btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
                btn_back.place(x=5,y=115)
            self.check_passbook = Button(self.label1 , text = 'Passbook' ,width = 13,fg = '#1c9eb8', font = 'arial 12 bold',command = passbook)
            self.check_passbook.place(x=250, y = 130)
            def visualize():
                # get acno
                list_acno = []
                fetch_acno= ("select Acno from data")
                result = conn.execute(fetch_acno)
                for i in result:
                    for j in (i):
                        j = j
                    list_acno.append(j)
                
                # get age
                list_age = []
                fetch_age= ("select Age from data")
                result = conn.execute(fetch_age)
                for i in result:
                    for j in (i):
                        j = j
                    list_age.append(j)
                self.label2 = Label(master,width=300,height = 500,bg = '#66cccc')
                self.label2.place(x=0,y=150)
                self.heading2 = Label(self.top, text = 'Data Visualize', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
                self.heading2.place(x= 250,y = 110)
                def Bar():
                    l10 = []
                    l20 = []
                    l30 = []
                    l40 = []
                    l50 = []
                    l60 = []
                    l70 = []
                    l80 = []
                    l90 = []
                    l100 = []
                    str_list = []
                    for j in range(len(list_age)):
                        str_list.append(int(list_age[j]))
                    for i in range (len(str_list)):
                        if str_list[i] < 11:
                            l10.append(str_list)
                        if str_list[i] > 10 and str_list[i] < 21:
                            l20.append(str_list)
                        if str_list[i] > 20 and str_list[i] < 31:
                            l30.append(str_list)
                        if str_list[i] > 30 and str_list[i] < 41:
                            l40.append(str_list)
                        if str_list[i] > 40 and str_list[i] < 51:
                            l50.append(str_list)
                        if str_list[i] > 50 and str_list[i] < 61:
                            l60.append(str_list)
                        if str_list[i] > 60 and str_list[i] < 71:
                            l70.append(str_list)
                        if str_list[i] > 70 and str_list[i] < 81:
                            l80.append(str_list)
                        if str_list[i] > 80 and str_list[i] < 91:
                            l90.append(str_list)
                        if str_list[i] > 90 and str_list[i] < 101:
                            l100.append(str_list) 
                    plt.xlabel('Age')
                    plt.ylabel('Frequency')
                    x_axis = ['0-10','10-20','20-30','30-40','40-50','60-60','60-70','70-80','80-90','90-100']
                    y_axis = [len(l10),len(l20),len(l30),len(l40),len(l50),len(l60),len(l70),len(l80),len(l90),len(l100)]
                    plt.bar(x_axis,y_axis)
                    plt.title('Bar Chart')
                    plt.tick_params(axis='x', which='major', labelsize=8)
                    plt.show()
        
                self.bar_chart = Button(self.label2 , text = 'Bar Chart' ,width = 13,fg = '#1c9eb8', font = 'arial 12 bold',command = Bar)
                self.bar_chart.place(x=250, y = 130)
                def line():
                    l10 = []
                    l20 = []
                    l30 = []
                    l40 = []
                    l50 = []
                    l60 = []
                    l70 = []
                    l80 = []
                    l90 = []
                    l100 = []
                    str_list = []
                    for j in range(len(list_age)):
                        str_list.append(int(list_age[j]))
                    for i in range (len(str_list)):
                        if str_list[i] < 11:
                            l10.append(str_list)
                        if str_list[i] > 10 and str_list[i] < 21:
                            l20.append(str_list)
                        if str_list[i] > 20 and str_list[i] < 31:
                            l30.append(str_list)
                        if str_list[i] > 30 and str_list[i] < 41:
                            l40.append(str_list)
                        if str_list[i] > 40 and str_list[i] < 51:
                            l50.append(str_list)
                        if str_list[i] > 50 and str_list[i] < 61:
                            l60.append(str_list)
                        if str_list[i] > 60 and str_list[i] < 71:
                            l70.append(str_list)
                        if str_list[i] > 70 and str_list[i] < 81:
                            l80.append(str_list)
                        if str_list[i] > 80 and str_list[i] < 91:
                            l90.append(str_list)
                        if str_list[i] > 90 and str_list[i] < 101:
                            l100.append(str_list) 
                    plt.xlabel('Age')
                    plt.ylabel('Frequency')
                    x_axis = ['0-10','10-20','20-30','30-40','40-50','60-60','60-70','70-80','80-90','90-100']
                    y_axis = [len(l10),len(l20),len(l30),len(l40),len(l50),len(l60),len(l70),len(l80),len(l90),len(l100)]
                    plt.plot(x_axis,y_axis)
                    plt.title('Line Chart')
                    plt.tick_params(axis='x', which='major', labelsize=8)
                    plt.show()
                self.Line_chart = Button(self.label2 , text = 'Line Chart' ,width = 13,fg = '#1c9eb8', font = 'arial 12 bold',command = line)
                self.Line_chart.place(x=250, y = 170)
                def scatter():
                    l10 = []
                    l20 = []
                    l30 = []
                    l40 = []
                    l50 = []
                    l60 = []
                    l70 = []
                    l80 = []
                    l90 = []
                    l100 = []
                    str_list = []
                    for j in range(len(list_age)):
                        str_list.append(int(list_age[j]))
                    for i in range (len(str_list)):
                        if str_list[i] < 11:
                            l10.append(str_list)
                        if str_list[i] > 10 and str_list[i] < 21:
                            l20.append(str_list)
                        if str_list[i] > 20 and str_list[i] < 31:
                            l30.append(str_list)
                        if str_list[i] > 30 and str_list[i] < 41:
                            l40.append(str_list)
                        if str_list[i] > 40 and str_list[i] < 51:
                            l50.append(str_list)
                        if str_list[i] > 50 and str_list[i] < 61:
                            l60.append(str_list)
                        if str_list[i] > 60 and str_list[i] < 71:
                            l70.append(str_list)
                        if str_list[i] > 70 and str_list[i] < 81:
                            l80.append(str_list)
                        if str_list[i] > 80 and str_list[i] < 91:
                            l90.append(str_list)
                        if str_list[i] > 90 and str_list[i] < 101:
                            l100.append(str_list) 
                    plt.xlabel('Age')
                    plt.ylabel('Frequency')
                    plt.title('Scatter Chart')
                    x_axis = ['0-10','10-20','20-30','30-40','40-50','60-60','60-70','70-80','80-90','90-100']
                    y_axis = [len(l10),len(l20),len(l30),len(l40),len(l50),len(l60),len(l70),len(l80),len(l90),len(l100)]
                    plt.scatter(x_axis,y_axis)
                    plt.tick_params(axis='x', which='major', labelsize=8)
                    plt.show()
                self.scatter_chart = Button(self.label2 , text = 'Scatter Chart' ,width = 13,fg = '#1c9eb8', font = 'arial 12 bold',command = scatter)
                self.scatter_chart.place(x=250, y = 210)
                def back():
                    self.label2.destroy()
                    self.heading2.destroy()
                    btn_back.destroy()
                btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
                btn_back.place(x=5,y=115)
            self.data_visualize = Button(self.label1 , text = 'Data Visualize' ,width = 13,fg = '#1c9eb8', font = 'arial 12 bold',command = visualize)
            self.data_visualize.place(x=250, y = 170)
            def back():
                self.label1.destroy()
                self.heading1.destroy()
                btn_back.destroy()
            btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
            btn_back.place(x=5,y=115)
        self.btn7 = Button(self.buttom , text = 'More' ,width = 13,fg = '#1c9eb8',font = 'arial 12 bold',command = click_btn7)
        self.btn7.place(x=250, y = 270)
        #about
        def click_btn8():
            self.label1 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label1.place(x=0,y=150)
            self.heading1 = Label(self.top, text = 'About', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading1.place(x= 290,y = 110)
            text = Text(self.label1,height = 20,width = 80)
            text.place(x=1,y=5)
            text.tag_configure('big', font=('Verdana', 20, 'bold'))
            text.tag_configure('version', font=('Verdana', 10, 'bold'))
            text.insert(END, "            Bank Management System\n\
                           (About)",'big')
            text_writing = "Enter Your Text Here"
            text.insert(END,text_writing)
            text.insert(END,'\n\n\
                                  \
                            Version - 1.0.000','version')
            text.config(state = 'disabled')
            def back():
                self.label1.destroy()
                self.heading1.destroy()
                btn_back.destroy()
            btn_back =Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back)
            btn_back.place(x=5,y=115)
            def OK():
                self.label1.destroy()
                self.heading1.destroy()
                btn_back.destroy()
            btn_OK =Button(self.label1 , text =  'OK',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = OK)
            btn_OK.place(x=250,y=350)
        self.btn8 = Button(self.buttom , text = 'About' ,width = 13,fg = '#1c9eb8',font = 'arial 12 bold',command = click_btn8)
        self.btn8.place(x=250, y = 310)
        # Exit
        def click_btn9():
            self.master.destroy()
        self.btn9 = Button(self.buttom , text = 'Exit' ,width = 13,fg = '#1c9eb8',font = 'arial 12 bold',command = click_btn9)
        self.btn9.place(x=250, y = 350) 
       
        # login/signup
        self.Label_login_signup = Label(self.master,width=300,height = 500,bg = '#66cccc')
        self.Label_login_signup.place(x=0,y=150)
        def login():
            self.label2 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label2.place(x=0,y=150)
            #labels
            self.heading2 = Label(self.top, text = 'Log In', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading2.place(x= 290,y = 110)
            label_user_name = Label(self.label2,text = "User Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 80)
            label_pswd = Label(self.label2,text = "Password",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 110)
            # Entries
            ent_name = Entry(self.label2,width=30)
            ent_name.place(x=295,y=83)
            ent_pswd = Entry(self.label2,width=30)
            ent_pswd.place(x=295,y=113)
            def inside_login():
                self.heading2.destroy()
                data_name = (ent_name.get())
                data_pswd = (ent_pswd.get())
                pre_result = ("create table if not exists data1(Name varchar,Pswd varchar);")
                conn.execute(pre_result)
                conn.commit()
                try:
                    if data_name  and data_pswd != '':
                        pre_result = ("SELECT pswd FROM data1 WHERE NAME = %a")%(data_name)
                        result = conn.execute(pre_result)
                        for i in result:
                            for Pswd in (i):
                                if Pswd == data_pswd:
                                    self.label2.destroy()
                                    self.Label_login_signup.destroy()
                                    btn_back.destroy()
                                else:
                                    messagebox.showerror("Bank Management System","Wrong Username or Password!")
                    else:
                        messagebox.showerror("Bank Management System","Fields cannot be empty!")
                except UnboundLocalError:
                    messagebox.showerror("Bank Management System","Wrong Username!")
            self.login123 = Button(self.label2 , text = 'Log In' ,width = 13, fg = '#1c9eb8', font = 'arial 12 bold',command = inside_login)
            self.login123.place(x=260, y = 250)
            def back1():
                self.label2.destroy()
                self.heading2.destroy()
                btn_back.destroy()
            btn_back = Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back1)
            btn_back.place(x=5,y=115)
        self.btn_login = Button(self.Label_login_signup , text = 'Login' ,width = 13, fg = '#1c9eb8', font = 'arial 12 bold',command =login)
        self.btn_login.place(x=250, y = 110)
        def signup():
            self.label2 = Label(master,width=300,height = 500,bg = '#66cccc')
            self.label2.place(x=0,y=150)
            #labels
            self.heading2 = Label(self.top, text = 'Sign Up', font = 'arial 15 bold', bg = 'white', fg = '#52bfe3')
            self.heading2.place(x= 290,y = 110)
            label_user_name = Label(self.label2,text = "User Name",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 80)
            label_pswd = Label(self.label2,text = "Password",bg ="#66cccc",fg = 'white',font = 'arial 12 bold').place(x = 185,y = 110)
            # Entries
            ent_name = Entry(self.label2,width=30)
            ent_name.place(x=295,y=83)
            ent_pswd = Entry(self.label2,width=30)
            ent_pswd.place(x=295,y=113)
            def SignUp():
                pre_result = ("create table if not exists data1(Name varchar,Pswd varchar);")
                conn.execute(pre_result)
                conn.commit()
                data_name = (ent_name.get())
                data_pswd = (ent_pswd.get())
                # check for existing username !!!

                if data_name  and data_pswd != '':
                    pre_result = ("SELECT name from data1")
                    result = conn.execute(pre_result)
                    for i in result:
                        for find_name in (i):
                            find_name == find_name
                    
                    if data_name == find_name :
                        messagebox.showerror("Bank Management System","Username already taken!")
                    else:
                        pre_result1 = ("insert into data1 values(%a ,%a);"%(data_name,data_pswd))
                        conn.execute(pre_result1)
                        conn.commit()
                        messagebox.showinfo("Bank Management System","Account sucessfully created !")
                        self.label2.destroy()
                        self.heading2.destroy()
                        btn_back.destroy()    
                else:
                    messagebox.showerror("Bank Management System","Fields cannot be empty!")
            self.signup123 = Button(self.label2 , text = 'Sign Up' ,width = 13, fg = '#1c9eb8', font = 'arial 12 bold',command = SignUp)
            self.signup123.place(x=260, y = 250)
            def back1():
                self.label2.destroy()
                self.heading2.destroy()
                btn_back.destroy()
            btn_back = Button(self.top , text =  '◀◀◀ Back',width = 13 , fg = '#1c9eb8',bg = 'white',font = 'arial 12 bold',command = back1)
            btn_back.place(x=5,y=115)
        self.btn_signup = Button(self.Label_login_signup , text = 'Sign Up' ,width = 13,fg = '#1c9eb8', font = 'arial 12 bold',command = signup)
        self.btn_signup.place(x=250, y = 150)

def main():
    root = Tk()
    app = Application(root)
    root.title('Bank Management System')
    root.geometry('650x550+350+90')
    root.resizable(False,False)
    root.iconbitmap('icons/icon8000.ico')
    root.mainloop()

if __name__ == '__main__':
    main()
