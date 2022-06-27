import createDB
import login
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

# 查询学生信息
def sel_stu():
    root1 = Tk()
    root1.resizable(False, False) ### 禁止最大化按钮
    root1.title("查询学生基本信息")
    root1.config(width = 600)
    root1.config(height = 600)

    ## 创建关联变量
    sId = StringVar(root1, value='')

    ## 创建文本组件框\标签组件
    label = Label(root1, text = "学号", font = ("微软雅黑 -20"))
    label.place(x = 30, y = 30, height = 40, width = 80)
    selId = Entry((root1), textvariable = sId)
    selId.place(x = 120, y = 30, height = 40, width = 200)

    ## 查询键
    def select():
        ## 创建关联字符变量
        s_name = StringVar(root1, value='')
        s_sex = StringVar(root1, value='')
        s_dept = StringVar(root1, value='')
        s_dno = StringVar(root1, value='')
        s_checkin = StringVar(root1, value='')
        s_test = StringVar(root1, value='')

        db, cur = createDB.db, createDB.mycursor
        stu_id = eval(selId.get()) ### 学号输入
        cur.execute("SELECT * from student where Sno = " + str(stu_id) + ' ;')
        res = cur.fetchone()
        if res is not None:
            stu_name = res[1].encode('latin1').decode('gbk')
            stu_sex = res[3].encode('latin1').decode('gbk')
            stu_dept = res[4].encode('latin1').decode('gbk')
            stu_dno = res[5].encode('latin1').decode('gbk')
            stu_checkin = res[6]
            stu_test = res[7].encode('latin1').decode('gbk')
            s_name.set(stu_name)
            s_sex.set(stu_sex)
            s_dept.set(stu_dept)
            s_dno.set(stu_dno)
            s_checkin.set(stu_checkin)
            s_test.set(stu_test)
        else:
            messagebox.showinfo(title='警告', message = '无当前学生信息')

        ## 创建标签组件
        label = Label(root1, text = "姓名：", font = ("微软雅黑 -20"))
        label.place(x = 80, y = 110, height = 40, width = 100)
        label = Label(root1, text = "性别：", font = ("微软雅黑 -20"))
        label.place(x = 80, y = 170, height = 40, width = 100)
        label = Label(root1, text = "专业：", font = ("微软雅黑 -20"))
        label.place(x = 80, y = 230, height = 40, width = 100)
        label = Label(root1, text = "宿舍号：", font = ("微软雅黑 -20"))
        label.place(x = 80, y = 290, height = 40, width = 100)
        label = Label(root1, text = "入住时间：", font = ("微软雅黑 -20"))
        label.place(x = 80, y = 350, height = 40, width = 100)
        label = Label(root1, text = "核酸情况：", font = ("微软雅黑 -20"))
        label.place(x = 80, y = 410, height = 40, width = 100)

        ## 创建文本框组件
        entryUn = Entry((root1), textvariable = s_name)
        entryUn.place(x = 200, y = 110, height = 40, width = 200)
        entryUn = Entry((root1), textvariable = s_sex)
        entryUn.place(x = 200, y = 170, height = 40, width = 200)
        entryUn = Entry((root1), textvariable = s_dept)
        entryUn.place(x = 200, y = 230, height = 40, width = 200)
        entryUn = Entry((root1), textvariable = s_dno)
        entryUn.place(x = 200, y = 290, height = 40, width = 200)
        entryUn = Entry((root1), textvariable = s_checkin)
        entryUn.place(x = 200, y = 350, height = 40, width = 200)
        entryUn = Entry((root1), textvariable = s_test)
        entryUn.place(x = 200, y = 410, height = 40, width = 200)

    buttonselect=Button(root1,text="查询",font=("微软雅黑 -20"),command=select)
    buttonselect.place(x = 340, y = 30, height = 40, width=100)

    ## 重置键
    def cancel():
        sId.set('')

    buttoncancel=Button(root1,text="重置",font="微软雅黑 -20",command = cancel)
    buttoncancel.place(x = 450,y = 30, height = 40,width =100)

    ## 退出键
    buttondel=Button(root1,text="退出",font="微软雅黑 -20",command=root1.destroy)
    buttondel.place(x = 250,y = 500, height = 40, width = 100)

    root1.mainloop()