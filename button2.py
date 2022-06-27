import createDB
import login
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

def sel_delivery():
    root2 = Tk()
    root2.resizable(False, False) ### 禁止最大化按钮
    root2.title("快递信息查询")
    root2.config(width = 600)
    root2.config(height = 600)

    ## 创建关联变量
    sId = StringVar(root2, value='')

    ## 创建文本组件框\标签组件
    label = Label(root2, text = "学号", font = ("微软雅黑 -20"))
    label.place(x = 30, y = 30, height = 40, width = 80)
    selId = Entry((root2), textvariable = sId)
    selId.place(x = 120, y = 30, height = 40, width = 200)

    ## 查询键
    def select():
        ## 创建关联字符变量
        s_name = StringVar(root2, value='')
        m_arrive = []
        m_receive = []
        m_number = []
        for i in range(4):
            m_arrive.append(0)
            m_receive.append(0)
            m_number.append(0)
        m_arrive[0] = StringVar(root2, value='')
        m_arrive[1] = StringVar(root2, value='')
        m_arrive[2] = StringVar(root2, value='')
        m_arrive[3] = StringVar(root2, value='')
        m_receive[0] = StringVar(root2, value='')
        m_receive[1] = StringVar(root2, value='')
        m_receive[2] = StringVar(root2, value='')
        m_receive[3] = StringVar(root2, value='')
        m_number[0] = StringVar(root2, value='')
        m_number[1] = StringVar(root2, value='')
        m_number[2] = StringVar(root2, value='')
        m_number[3] = StringVar(root2, value='')

        db, cur = createDB.db, createDB.mycursor
        stu_id = eval(selId.get()) ### 学号输入

        cur.execute("select Sname from student where Sno = " + str(stu_id) + ' ;')
        res = cur.fetchone()
        if res is not None:
            stu_name = res[0].encode('latin1').decode('gbk')
            s_name.set(stu_name)
        else:
            messagebox.showinfo(title='警告', message = '无当前学生信息')

        cur.execute("select Marrive from delivery where Sname = '%s'" % str(stu_name))
        res = cur.fetchall()
        if res is not None:
            for i in range(len(res)):
                m_arrive[i].set(res[i])

        cur.execute("select Mreceive from delivery where Sname = '%s'" % str(stu_name))
        res = cur.fetchall()
        if res is not None:
             for i in range(len(res)):
                m_receive[i].set(res[i])

        cur.execute("select Mnumber from delivery where Sname = '%s'" % str(stu_name))
        res = cur.fetchall()
        if res is not None:
            for i in range(len(res)):
                m_number[i].set(res[i][0])
   
        ## 创建标签组件
        label = Label(root2, text = "姓名：", font = ("微软雅黑 -20"))
        label.place(x = 30, y = 110, height = 40, width = 100)
        label = Label(root2, text = "到达时间", font = ("微软雅黑 -20"))
        label.place(x = 80, y = 170, height = 40, width = 100)
        label = Label(root2, text = "签收时间", font = ("微软雅黑 -20"))
        label.place(x = 280, y = 170, height = 40, width = 100)
        label = Label(root2, text = "快递数量", font = ("微软雅黑 -20"))
        label.place(x = 430, y = 170, height = 40, width = 100)

        ## 创建文本框组件
        entryUn = Entry((root2), textvariable = s_name)
        entryUn.place(x = 120, y = 110, height = 40, width = 150)

        entryUn = Entry((root2), textvariable = m_arrive[0])
        entryUn.place(x = 60, y = 230, height = 40, width = 150)
        entryUn = Entry((root2), textvariable = m_receive[0])
        entryUn.place(x = 250, y = 230, height = 40, width = 150)
        entryUn = Entry((root2), textvariable = m_number[0])
        entryUn.place(x = 440, y = 230, height = 40, width = 100)

        entryUn = Entry((root2), textvariable = m_arrive[1])
        entryUn.place(x = 60, y = 290, height = 40, width = 150)
        entryUn = Entry((root2), textvariable = m_receive[1])
        entryUn.place(x = 250, y = 290, height = 40, width = 150)
        entryUn = Entry((root2), textvariable = m_number[1])
        entryUn.place(x = 440, y = 290, height = 40, width = 100)
    
        entryUn = Entry((root2), textvariable = m_arrive[2])
        entryUn.place(x = 60, y = 350, height = 40, width = 150)
        entryUn = Entry((root2), textvariable = m_receive[2])
        entryUn.place(x = 250, y = 350, height = 40, width = 150)
        entryUn = Entry((root2), textvariable = m_number[2])
        entryUn.place(x = 440, y = 350, height = 40, width = 100)

        entryUn = Entry((root2), textvariable = m_arrive[3])
        entryUn.place(x = 60, y = 410, height = 40, width = 150)
        entryUn = Entry((root2), textvariable = m_receive[3])
        entryUn.place(x = 250, y = 410, height = 40, width = 150)
        entryUn = Entry((root2), textvariable = m_number[3])
        entryUn.place(x = 440, y = 410, height = 40, width = 100)

    buttonselect=Button(root2,text="查询",font=("微软雅黑 -20"),command=select)
    buttonselect.place(x = 340, y = 30, height = 40, width=100)

    ## 重置键
    def cancel():
        sId.set('')

    buttoncancel=Button(root2,text="重置",font="微软雅黑 -20",command = cancel)
    buttoncancel.place(x = 450,y = 30, height = 40,width =100)

    ## 退出键
    buttondel=Button(root2,text="退出",font="微软雅黑 -20",command=root2.destroy)
    buttondel.place(x = 250,y = 500, height = 40, width = 100)

    root2.mainloop()