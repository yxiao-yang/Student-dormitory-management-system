import createDB
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

# 登录
def Login():
    def Signin():
        ## 连接数据库
        db, cur = createDB.db, createDB.mycursor

        ## 读取输入
        stu_Un = eval(entryUn.get())
        stu_Pw = eval(entryPw.get())

        ## 学号密码是否正确
        cur.execute("SELECT COUNT(*) from student where sno = '%s'" % str(stu_Un))
        flag1 = cur.fetchone()[0]
        if flag1 != 0: ### 学号存在
            cur.execute("SELECT Spassword from student where sno = '%s'" % str(stu_Un))
            flag2 = cur.fetchone()[0]
            if str(stu_Pw) == str.strip(str(flag2)):
                messagebox.showinfo('提示',message='登录成功！')
                root.destroy()
            else:
                messagebox.showerror('警告',message='密码错误，请重新输入')
        else: ### 学号不存在
            messagebox.showerror('警告',message='学号查找失败，请重新输入')

    # 学生登录界面
    root = Tk()
    root.resizable(False,False) # 禁止最大化按钮
    root.minsize(600,600) # 最小尺寸
    root.maxsize(600,600) # 最大尺寸
    root.title("学生宿舍管理系统") # 窗口名
    root.config(width=600)
    root.config(height=600)

    ## 创建关联字符变量
    username = StringVar(root, value='')
    password = StringVar(root, value='')

    ## 创建标签组件
    label = Label(root, text = "欢迎登录宿舍管理系统！", font = ("微软雅黑 -25"))
    label.place(x = 150, y = 100, height = 40, width = 300)
    label = Label(root, text = "（学生端）", font = ("微软雅黑 -20"))
    label.place(x = 250, y = 150, height = 40, width = 100)
    label = Label(root, text = "学号：", font = ("微软雅黑 -20"))
    label.place(x = 150, y = 250, height = 40, width = 80)
    label = Label(root, text = "密码：",font = ("微软雅黑 -20"))
    label.place(x = 150, y = 300, height = 40, width = 80)

    ## 创建文本框组件
    entryUn = Entry((root), textvariable = username)
    entryUn.place(x = 250, y = 250, height = 40, width = 200)
    entryPw = Entry((root), textvariable = password)
    entryPw.place(x = 250, y = 300, height = 40, width = 200)

    ## 登录键
    buttonSign = Button(root, text = "登录", font = ("微软雅黑 -20"), command = Signin)
    buttonSign.place(x = 275, y = 400, height = 40, width = 60)

    root.mainloop()