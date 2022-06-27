import createDB
import login2
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

def add_stu():
    root2 = Tk()
    root2.resizable(False, False) ### 禁止最大化按钮
    root2.title("添加学生")
    root2.config(width = 600)
    root2.config(height = 600)

    ## 创建标签组件
    label = Label(root2, text = "学号：", font = ("微软雅黑 -20"))
    label.place(x = 80, y = 50, height = 40, width = 100)
    label = Label(root2, text = "姓名：", font = ("微软雅黑 -20"))
    label.place(x = 80, y = 110, height = 40, width = 100)
    label = Label(root2, text = "性别：", font = ("微软雅黑 -20"))
    label.place(x = 80, y = 170, height = 40, width = 100)
    label = Label(root2, text = "专业：", font = ("微软雅黑 -20"))
    label.place(x = 80, y = 230, height = 40, width = 100)
    label = Label(root2, text = "宿舍号：", font = ("微软雅黑 -20"))
    label.place(x = 80, y = 290, height = 40, width = 100)
    label = Label(root2, text = "入住时间：", font = ("微软雅黑 -20"))
    label.place(x = 80, y = 350, height = 40, width = 100)
    label = Label(root2, text = "核酸情况：", font = ("微软雅黑 -20"))
    label.place(x = 80, y = 410, height = 40, width = 100)
    label = Label(root2, text = "密码：", font = ("微软雅黑 -20"))
    label.place(x = 80, y = 470, height = 40, width = 100)

    ## 创建关联字符变量
    s_sno = StringVar(root2, value='')
    s_name = StringVar(root2, value='')
    s_sex = StringVar(root2, value='')
    s_dept = StringVar(root2, value='')
    s_dno = StringVar(root2, value='')
    s_checkin = StringVar(root2, value='')
    s_test = StringVar(root2, value='')
    s_password = StringVar(root2, value='')

    db, cur = createDB.db, createDB.mycursor

    ## 创建文本框组件
    S_sno = Entry((root2), textvariable = s_sno)
    S_sno.place(x = 180, y = 50, height = 40, width = 200)
    S_name = Entry((root2), textvariable = s_name)
    S_name.place(x = 180, y = 110, height = 40, width = 200)
    S_sex = Entry((root2), textvariable = s_sex)
    S_sex.place(x = 180, y = 170, height = 40, width = 200)
    S_dept = Entry((root2), textvariable = s_dept)
    S_dept.place(x = 180, y = 230, height = 40, width = 200)
    S_dno = Entry((root2), textvariable = s_dno)
    S_dno.place(x = 180, y = 290, height = 40, width = 200)
    S_checkin = Entry((root2), textvariable = s_checkin)
    S_checkin.place(x = 180, y = 350, height = 40, width = 200)
    S_test = Entry((root2), textvariable = s_test)
    S_test.place(x = 180, y = 410, height = 40, width = 200)
    S_password = Entry((root2), textvariable = s_password)
    S_password.place(x = 180, y = 470, height = 40, width = 200)

    ## 添加键
    def add():
        u_sno = S_sno.get()
        u_name = S_name.get()
        u_sex = S_sex.get()
        u_dept = S_dept.get()
        u_dno = S_dno.get()
        u_checkin = S_checkin.get()
        u_test = S_test.get()
        u_password = S_password.get()
        print(u_sno)
        cur.execute("INSERT INTO student (Sno,Sname,Spassword,Ssex,Sdept,Dno,scheckin,Test) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (u_sno, u_name, u_password, u_sex, u_dept, u_dno, u_checkin, u_test))
        messagebox.showinfo(title='恭喜',message='添加成功！')

    buttondel=Button(root2,text="添加",font="微软雅黑 -20",command = add)
    buttondel.place(x = 450,y = 50, height = 40,width =100)

    ## 重置键
    def cancel():
        s_sno.set('')
        s_name.set('')
        s_sex.set('')
        s_dept.set('')
        s_dno.set('')
        s_checkin.set('')
        s_test.set('')
        s_password.set('')

    buttoncancel=Button(root2,text="重置",font="微软雅黑 -20",command = cancel)
    buttoncancel.place(x = 450,y = 110, height = 40,width =100)

    ## 退出键
    buttondel=Button(root2,text="退出",font="微软雅黑 -20",command=root2.destroy)
    buttondel.place(x = 450,y = 170, height = 40, width = 100)

    root2.mainloop()