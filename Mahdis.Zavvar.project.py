
#Mahdis_Zavvar
#Finall Project

from tkinter import Tk , Label , Button , Entry , PhotoImage , Toplevel , messagebox , StringVar
from tkinter.ttk import Combobox

name_list = [] ; family_list = [] ; code_list = [] ; avg_list = [] ; F_name = []

#---------------------Class: Append List---------------------

class AppendList:
    '''
    A class with a method 'Append' to append parameters from 'Student_Info' file to lists.

    Methods:
    ---------
        Append
    '''
    def Append(self):
        '''
        Parameters:
        ----------
            FName (str):
                 first name of the students
            LName (str):
                 last name of the students
            IDcode (int):
                 ID code number of the students
            avrg (float):
                 average of the students

        -----------
            name_list , family_list , code_list , avg_list: list

        '''
        with open('Student_Info.txt') as fname:
            for i in fname:
                c = i.split()
                FName = c[len(c) - 8]
                name_list.append(FName)


        with open('Student_Info.txt') as lname:
            for i in lname:
                c = i.split()
                LName = c[len(c) - 7]
                family_list.append(LName)


        with open('Student_Info.txt') as code:
            for i in code:
                c = i.split()
                IDcode = int(c[len(c) - 4])
                code_list.append(IDcode)


        with open('Student_Info.txt') as avg:
            for i in avg:
                c = i.split()
                avrg = float(c[len(c) - 1])
                avg_list.append(avrg)

#---------------------Form 2: ٍEnter And Add Data---------------------

def EnterData_Form():
    '''
    Function to create a form to enter or add new data such as first name, last name, ID code number and average.

    Methods:
    --------
        add_data
    '''
    def add_data():
        '''
        Function to add new data.

        Use if/else to prevent repeating same identity.

        Parameters:
        ----------
            name , firstname_txt (str):
                    students' first name
            family , lastname_txt (str):
                    students' last name
            code , code_txt (int):
                    students' ID code number
            avg , avg_txt (float):
                    students' average
        '''
        name = firstname_txt.get()
        family = lastname_txt.get()
        code = code_txt.get()
        avg = avg_txt.get()

        f_new = open('Student_Info.txt','a')
        f_new.close()

        with open('Student_Info.txt','r') as Code:
            for i in Code:
                c = i.split()
                d = int(c[len(c) - 4])
                code_list.append(d)

        if int(code) in code_list:
            lbl_code.set('< Repeated Error >\nSame Identity Exist.')

            firstname_txt.delete(0, 'end')
            lastname_txt.delete(0, 'end')
            code_txt.delete(0, 'end')
            avg_txt.delete(0, 'end')

            firstname_txt.focus()


        else:
            n = ('Fullname: ', name, ' ', family, ' , ', 'code= ', code, ' , ', 'avg= ', avg, '\n')

            with open('Student_Info.txt', 'a') as f:
                for i in n:
                    f.write(i)
            name_str = name+' '+family+' is saved.'
            lbl_code.set(name_str)

            firstname_txt.delete(0,'end')
            lastname_txt.delete(0,'end')
            code_txt.delete(0,'end')
            avg_txt.delete(0,'end')

            firstname_txt.focus()

    frm2 = Toplevel()
    frm2.title('Enter/Add Data')
    frm2.geometry('500x350')
    frm2.resizable(width=False, height=False)
    frm2.configure(bg='whitesmoke')

    lbl_code = StringVar()

    firstname_txt = Entry(frm2,bg='seashell',fg='black',font=('Bahnschrift SemiBold',12))
    firstname_txt.place(x=240, y=30)
    firstname_txt.focus()

    lastname_txt = Entry(frm2,bg='seashell',fg='black',font=('Bahnschrift SemiBold',12))
    lastname_txt.place(x=240,y=80)

    code_txt = Entry(frm2,bg='seashell',fg='black',font=('Bahnschrift SemiBold',12))
    code_txt.place(x=240,y=130)

    avg_txt = Entry(frm2,bg='seashell',fg='black',font=('Bahnschrift SemiBold',12))
    avg_txt.place(x=240,y=180)

    Label(frm2,text='Enter First Name:',bg='peachpuff',fg='black',font=('Berlin Sans FB Demi',12)).place(x=50,y=30)
    Label(frm2,text='Enter Last Name:',bg='peachpuff',fg='black',font=('Berlin Sans FB Demi',12)).place(x=50,y=80)
    Label(frm2,text='Enter ID Code Number:',bg='peachpuff',fg='black',font=('Berlin Sans FB Demi',12)).place(x=50,y=130)
    Label(frm2,text='Enter Average:',bg='peachpuff',fg='black',font=('Berlin Sans FB Demi',12)).place(x=50,y=180)
    Label(frm2,textvariable=lbl_code,font=('Bahnschrift SemiBold',13),bg='silver').place(x=180,y=220)

    Button(frm2,text='Add',command=add_data,bg='light blue',font=('G2 Rubber Stamp LET',12)).place(x=300,y=280)
    Button(frm2,text='Back to\nmain form',command=frm2.destroy,bg='light blue',font=('G2 Rubber Stamp LET',11)).place(x=90 ,y=275)

    frm2.mainloop()

#---------------------Function: Search Data---------------------

def search(X):
    '''
    Function to search and find data.

    Use if/else to check whether that identity exists or not.

    Arguments:
    ----------
        X: int

    Parameters:
    ----------
        lbl_search (str):
                result of the search process.
    '''

    lst = AppendList()
    lst.Append()

    global lbl_search
    lbl_search = StringVar()

    if X in code_list:
        e = code_list.index(X)
        Full_name = f'Fullname: {name_list[e]} {family_list[e]} , code= {code_list[e]} , avg= {avg_list[e]}'
        lbl_search.set(Full_name)
    else:
        lbl_search.set('Not Exist such identity.')

    name_list.clear() ; family_list.clear() ; code_list.clear() ; avg_list.clear()

#---------------------Form 3: Search Data---------------------

def SearchData_Form():
    '''
    Function to create a form to search and show the student information.

    Methods:
    --------
        show_data

    Parameters:
    -----------
        Search_txt (str):
                 Id code number (to search)
    '''

    frm3 = Toplevel()
    frm3.title('Serach Data')
    frm3.geometry('500x340')
    frm3.resizable(width=False, height=False)
    frm3.configure(bg='whitesmoke')

    Search_txt = Entry(frm3,bg='seashell',fg='black',font=('Bahnschrift SemiBold',12))
    Search_txt.place(x=250, y=50)
    Search_txt.focus()

    def show_data():
        '''
        Function to show the searched data.
        '''
        search(int(Search_txt.get()))
        Label(frm3,bg='whitesmoke',height=5,width=65).place(x=30, y=147)
        Label(frm3, textvariable=lbl_search, font=('Bahnschrift SemiBold', 13), bg='silver').place(x=70, y=170)
        Search_txt.delete(0,'end')


    Label(frm3,text='Enter ID Code Number:',bg='peachpuff',fg='black',font=('Berlin Sans FB Demi',12)).place(x=50,y=50)

    Button(frm3, text='Search', command=show_data, bg='light blue',font=('G2 Rubber Stamp LET', 11)).place(x=200, y=100)
    Button(frm3,text='Back to\nmain form',command=frm3.destroy,bg='light blue',font=('G2 Rubber Stamp LET',11)).place(x=185 ,y=240)

    frm3.mainloop()

#---------------------Form 4:Change Data---------------------

def ChangeData_Form():
    '''
    Function to create a form to change a specific data.

    Methods:
    --------
        change and show data


    Parameters:
    -----------
        Former_txt (str):
                ID code number (to change data of that person)

        New_txt (str):
                new data of a person (it can be first name, last name, ID code or average)

        cmb (combobox):
                to select an icon to change

        lbl_change (StringVar):
                to set the situation of changing
    '''

    def change():
        '''
        Function to change data.

        Use ask ok/cancel confirmation to affirm changing data.

        Use if/elif to recognize the part of transformation.
        '''
        lst = AppendList()
        lst.Append()

        x = int(Former_txt.get())
        ID = code_list.index(x)

        if messagebox.askokcancel('Confirmation', 'Do you want to change?', icon=messagebox.WARNING):
            f = open('Student_Info.txt', 'w')
            if current_var.get() == 'First Name':
                name_list[ID] = New_txt.get()
                for item in range(len(name_list)):
                    n = ('Fullname: ', name_list[item], ' ', family_list[item], ' , ', 'code= ', str(code_list[item]), ' , ', 'avg= ', str(avg_list[item]), '\n')
                    for i in n:
                        f.write(i)

            elif current_var.get() == 'Last Name':
                family_list[ID] = New_txt.get()
                for item in range(len(name_list)):
                    n = ('Fullname: ', name_list[item], ' ', family_list[item], ' , ', 'code= ', str(code_list[item]), ' , ', 'avg= ', str(avg_list[item]), '\n')
                    for i in n:
                        f.write(i)

            elif current_var.get() == 'ID Code Number':
                code_list[ID] = int(New_txt.get())
                for item in range(len(name_list)):
                    n = ('Fullname: ', name_list[item], ' ', family_list[item], ' , ', 'code= ', str(code_list[item]), ' , ', 'avg= ', str(avg_list[item]), '\n')
                    for i in n:
                        f.write(i)

            elif current_var.get() == 'Average':
                avg_list[ID] = int(New_txt.get())
                for item in range(len(name_list)):
                    n = ('Fullname: ', name_list[item], ' ', family_list[item], ' , ', 'code= ', str(code_list[item]), ' , ', 'avg= ', str(avg_list[item]), '\n')
                    for i in n:
                        f.write(i)

            new_Fullname = f'Successfully changed.\nFullname: {name_list[ID]} {family_list[ID]} , code= {code_list[ID]} , avg= {avg_list[ID]}'
            lbl_change.set(new_Fullname)
            f.close()

        else:
            lbl_change.set('Not Changed.')

        name_list.clear() ; family_list.clear() ; code_list.clear() ; avg_list.clear()

    frm4 = Toplevel()
    frm4.title('Change Data')
    frm4.geometry('500x400')
    frm4.resizable(width=False, height=False)
    frm4.configure(bg= 'whitesmoke')

    lbl_change = StringVar()
    current_var = StringVar()

    cmb = Combobox(frm4,values= ('First Name','Last Name','ID Code Number','Average'),textvariable= current_var)
    cmb.place(x=315,y=150)
    cmb.current(1)

    Former_txt = Entry(frm4,bg='seashell',fg='black',font=('Bahnschrift SemiBold',12))
    Former_txt.place(x=273,y=20)
    Former_txt.focus()

    New_txt = Entry(frm4,bg='seashell',fg='black',font=('Bahnschrift SemiBold',12))
    New_txt.place(x=273,y=200)

    def show_data():
        '''
        Function to show the searched data.
        '''
        search(int(Former_txt.get()))
        Label(frm4,bg='whitesmoke',height=2,width=65).place(x=30, y=95)
        Label(frm4, textvariable=lbl_search, font=('Bahnschrift SemiBold', 13), bg='silver').place(x=80, y=100)

    Label(frm4,text='Enter ID Code Number:',bg='peachpuff',font=('Berlin Sans FB Demi',12)).place(x=30,y=20)
    Label(frm4,text='Which part do you want to change?',bg='lightcoral',font=('Berlin Sans FB Demi',12)).place(x=30,y=150)
    Label(frm4,text='Enter New Data:',bg='peachpuff',font=('Berlin Sans FB Demi',12)).place(x=30,y=200)
    Label(frm4,textvariable=lbl_change,font=('Bahnschrift SemiBold',13),bg='silver').place(x=80,y=280)

    Button(frm4,text='Show Data',command=show_data,bg='light blue',font=('G2 Rubber Stamp LET',11)).place(x=180,y=55)
    Button(frm4,text='Change',command=change,bg='light blue',font=('G2 Rubber Stamp LET',11)).place(x=190,y=237)
    Button(frm4,text='Back to\nmain form',command=frm4.destroy,bg='light blue',font=('G2 Rubber Stamp LET',11)).place(x=180 ,y=335)

    frm4.mainloop()

#---------------------Form 5:Delete Data---------------------

def DeleteData_Form():
    '''
    Function to create a form to delete selected information.

    Methods:
    --------
        Delete and show_data

    Parameters:
    ----------
        Delete_txt (str):
                ID code number to delete an identity

        lbl_delete (StringVar):
                    to set the situation of the deletion
    '''

    def Delete():
        '''
        Ask ok/cancel confirmation to confirm the deletion.

        Use try/except to manage the errors if there doesn't exist such identity.

        Parameters:
        -----------
            IDcode (int):
                  ID code number (to delete)
        '''
        lst = AppendList()
        lst.Append()

        IDcode = int(Delete_txt.get())

        if messagebox.askokcancel('Confirmation', 'Do you want to delete?', icon=messagebox.WARNING):
            try:
                b = code_list.index(IDcode)
                name_str = (name_list[b] +' '+ family_list[b]+' '+'is deleted')
                code_list.pop(b)
                name_list.pop(b)
                family_list.pop(b)
                avg_list.pop(b)
                lbl_delete.set(name_str)

                f = open('Student_Info.txt', 'w')
                for i in range(len(name_list)):
                    b = ('Fullname: ', name_list[i], ' ', family_list[i], ' , ', 'code= ', str(code_list[i]), ' , ', 'avg= ', str(avg_list[i]), '\n')
                    for x in b:
                        f.write(x)

                f.close()
                Delete_txt.delete(0,'end')

            except:
                lbl_delete.set('Not exist such identity.')
                Delete_txt.delete(0, 'end')

        else:
            lbl_delete.set('Not Deleted.')

        name_list.clear() ; family_list.clear() ; code_list.clear() ; avg_list.clear()

    frm5 = Toplevel()
    frm5.title('Delete Data')
    frm5.geometry('500x350')
    frm5.resizable(width=False, height=False)
    frm5.configure(bg='whitesmoke')

    lbl_delete = StringVar()

    Delete_txt = Entry(frm5,bg='seashell',fg='black',font=('Bahnschrift SemiBold',12))
    Delete_txt.place(x=250, y=50)
    Delete_txt.focus()

    def show_data():
        '''
        Function to show the searched data.
        '''
        search(int(Delete_txt.get()))
        Label(frm5,bg='whitesmoke',height=2,width=65).place(x=30, y=140)
        Label(frm5, textvariable=lbl_search, font=('Bahnschrift SemiBold', 13), bg='silver').place(x=80, y=145)

    Label(frm5,text='Enter ID Code Number:',bg='peachpuff',fg='black',font=('Berlin Sans FB Demi',12)).place(x=50,y=50)
    Label(frm5,textvariable=lbl_delete,font=('Bahnschrift SemiBold',13),bg='silver').place(x=150,y=235)

    Button(frm5,text='Delete',command=Delete,bg='light blue',font=('G2 Rubber Stamp LET',11)).place(x=200,y=190)
    Button(frm5,text='Show Data',command=show_data,bg='light blue',font=('G2 Rubber Stamp LET',11)).place(x=180,y=90)
    Button(frm5,text='Back to\nmain form',command=frm5.destroy,bg='light blue',font=('G2 Rubber Stamp LET',11)).place(x=185 ,y=280)

    frm5.mainloop()

#---------------------Form 6:Show Student Average Mean---------------------

def Miangin_Form():
    '''
    Function to show the average grade mean of the students and the maximum and minimum average.

    Parameters:
    -----------
        Sum (float):
              counter of the summation

        Miangin (float):
              average grade mean

        MaxName_str (str):
                max average with its name

        MinName_str (str):
                min average with its name
    '''
    lst = AppendList()
    lst.Append()

    Sum = 0
    for i in range(len(avg_list)):
        Sum += avg_list[i]

    Miangin = '{:.2f}'.format(Sum / len(avg_list))

    iMax = avg_list.index(max(avg_list))
    MaxName_str = f'{max(avg_list)} ( {name_list[iMax]} {family_list[iMax]} )'

    iMin = avg_list.index(min(avg_list))
    MinName_str = f'{min(avg_list)} ( {name_list[iMin]} {family_list[iMin]} )'

    name_list.clear() ; family_list.clear() ; code_list.clear() ; avg_list.clear()

    lbl_miangin = StringVar()
    lbl_MaxName = StringVar()
    lbl_MinName = StringVar()

    lbl_miangin.set(Miangin)
    lbl_MaxName.set(MaxName_str)
    lbl_MinName.set(MinName_str)

    frm6 = Toplevel()
    frm6.title('Student Average Mean')
    frm6.geometry('430x300')
    frm6.resizable(width=False, height=False)
    frm6.configure(bg='whitesmoke')

    Label(frm6,text='Student Average Mean is:',font=('Bahnschrift SemiBold',12),bg='darksalmon').place(x=50,y=40)
    Label(frm6,textvariable = lbl_miangin,font=('Bahnschrift SemiBold',12),bg='darksalmon').place(x=265,y=40)
    Label(frm6,text='Maximum Average:',font=('Bahnschrift SemiBold',12),bg='tan').place(x=50,y=100)
    Label(frm6,textvariable=lbl_MaxName,font=('Bahnschrift SemiBold',12),bg='tan').place(x=220,y=100)
    Label(frm6,text='Minimum Average:',font=('Bahnschrift SemiBold',12),bg='tan').place(x=50,y=150)
    Label(frm6,textvariable=lbl_MinName,font=('Bahnschrift SemiBold',12),bg='tan').place(x=220,y=150)

    Button(frm6,text='Back to\nmain form',command=frm6.destroy,bg='light blue',font=('G2 Rubber Stamp LET',11)).place(x=150 ,y=230)

    frm6.mainloop()

#---------------------Form 7:Show Student Average Grade Plot---------------------

import matplotlib.pyplot as plt

def plot():
     lst = AppendList()
     lst.Append()
     '''
    Plot to show names with averages in a chart.

    Parameters:
        Full_name (str):
                students' first name and last name
    '''

    

     for i in range(len(name_list)):
        Full_name = name_list[i]+'\n'+family_list[i]
        F_name.append(Full_name)

     plt.bar([i for i in range(len(name_list))],avg_list,color='darkcyan',edgecolor='navy',label='Student Average Grade', width=0.5)
     plt.xticks([i for i in range(len(name_list))],F_name)
     plt.title('Average Plot')
     plt.xlabel('Names')
     plt.ylabel('Average')
     plt.legend()
     plt.grid()

     plt.show()

#---------------------Exit Form---------------------

def Exit_Form():
    '''
    Function with ask ok/cancel to confirm the exit.
    '''
    if messagebox.askokcancel('Exit','Do you want to quit?'):
        frm.destroy()

#---------------------Main Form---------------------

'''
A form to get, edit, search and delete data with an average grade plot.

It has a logo of Tehran University Jahad and the exit button.
'''

frm = Tk()
frm.title('Student Information')
frm.geometry('700x400')
frm.resizable(width=False,height=False)
frm.configure(bg='lightgray')

Button(frm,text='Enter/ Add Data',bg='light pink',font=('Maiandra GD',16),command=EnterData_Form).place(x=145,y=50)
Button(frm,text='Search Data',bg='light pink',font=('Maiandra GD',16),command=SearchData_Form).place(x=160,y=110)
Button(frm,text='Change Data',bg='light pink',font=('Maiandra GD',16),command=ChangeData_Form).place(x=70,y=170)
Button(frm,text='Delete Data',bg='light pink',font=('Maiandra GD',16),command=DeleteData_Form).place(x=250,y=170)
Button(frm,text='Show Student\nAverage Mean ',bg='light pink',font=('Maiandra GD',16),command=Miangin_Form).place(x=150,y=230)
Button(frm,text='Student Average\nGrade Plot',bg='light pink',font=('Maiandra GD',16),command=plot).place(x=150,y=310)
Button(frm,text='Exit',bg='firebrick',fg='white',font=('',14),command=Exit_Form).place(x=480,y=300)

try:
    jahadpic = PhotoImage(file='jahad pic.png')
    Label(frm, image=jahadpic).place(x=450, y=60)
except:
    print('No picture')

frm.mainloop()

