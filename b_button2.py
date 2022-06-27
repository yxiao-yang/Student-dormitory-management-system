import createDB
import login2
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk


def upd_stu():
    root2 = Tk()
    root2.resizable(False, False) ### 禁止最大化按钮
    root2.title("修改学生基本信息")
    root2.config(width = 600)
    root2.config(height = 600)

    ## 创建关联变量
    sId = StringVar(root2, value='')

    ## 创建文本组件框\标签组件
    label = Label(root2, text = "学号：", font = ("微软雅黑 -20"))
    label.place(x = 30, y = 30, height = 40, width = 80)
    selId = Entry((root2), textvariable = sId)
    selId.place(x = 120, y = 30, height = 40, width = 200)

    ## 查询键
    def select():
        ## 创建关联字符变量
        s_name = StringVar(root2, value='')
        s_sex = StringVar(root2, value='')
        s_dept = StringVar(root2, value='')
        s_dno = StringVar(root2, value='')
        s_checkin = StringVar(root2, value='')
        s_test = StringVar(root2, value='')
        upd_name = StringVar(root2, value='')
        upd_sex = StringVar(root2, value='')
        upd_dept = StringVar(root2, value='')
        upd_dno = StringVar(root2, value='')
        upd_checkin = StringVar(root2, value='')
        upd_test = StringVar(root2, value='')

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
        label = Label(root2, text = "姓名：", font = ("微软雅黑 -20"))
        label.place(x = 40, y = 160, height = 40, width = 100)
        label = Label(root2, text = "性别：", font = ("微软雅黑 -20"))
        label.place(x = 40, y = 220, height = 40, width = 100)
        label = Label(root2, text = "专业：", font = ("微软雅黑 -20"))
        label.place(x = 40, y = 280, height = 40, width = 100)
        label = Label(root2, text = "宿舍号：", font = ("微软雅黑 -20"))
        label.place(x = 40, y = 340, height = 40, width = 100)
        label = Label(root2, text = "入住时间：", font = ("微软雅黑 -20"))
        label.place(x = 40, y = 400, height = 40, width = 100)
        label = Label(root2, text = "核酸情况：", font = ("微软雅黑 -20"))
        label.place(x = 40, y = 460, height = 40, width = 100)
        label = Label(root2, text = "修改前", font = ("微软雅黑 -20"))
        label.place(x = 170, y = 120, height = 40, width = 80)
        label = Label(root2, text = "修改后", font = ("微软雅黑 -20"))
        label.place(x = 400, y = 120, height = 40, width = 80)

        ## 创建文本框组件
        entryUn = Entry((root2), textvariable = s_name)
        entryUn.place(x = 150, y = 160, height = 40, width = 200)
        entryUn = Entry((root2), textvariable = s_sex)
        entryUn.place(x = 150, y = 220, height = 40, width = 200)
        entryUn = Entry((root2), textvariable = s_dept)
        entryUn.place(x = 150, y = 280, height = 40, width = 200)
        entryUn = Entry((root2), textvariable = s_dno)
        entryUn.place(x = 150, y = 340, height = 40, width = 200)
        entryUn = Entry((root2), textvariable = s_checkin)
        entryUn.place(x = 150, y = 400, height = 40, width = 200)
        entryUn = Entry((root2), textvariable = s_test)
        entryUn.place(x = 150, y = 460, height = 40, width = 200)

        U_name = Entry((root2), textvariable = upd_name)
        U_name.place(x = 370, y = 160, height = 40, width = 200)
        U_sex = Entry((root2), textvariable = upd_sex)
        U_sex.place(x = 370, y = 220, height = 40, width = 200)
        U_dept = Entry((root2), textvariable = upd_dept)
        U_dept.place(x = 370, y = 280, height = 40, width = 200)
        U_dno = Entry((root2), textvariable = upd_dno)
        U_dno.place(x = 370, y = 340, height = 40, width = 200)
        U_checkin = Entry((root2), textvariable = upd_checkin)
        U_checkin.place(x = 370, y = 400, height = 40, width = 200)
        U_test = Entry((root2), textvariable = upd_test)
        U_test.place(x = 370, y = 460, height = 40, width = 200)

        ## 修改键
        def commit():
            u_name = U_name.get()
            u_sex = U_sex.get()
            u_dept = U_dept.get()
            u_dno = U_dno.get()
            u_checkin = U_checkin.get()
            u_test = U_test.get()
            cur.execute("update student SET Sname='%s',Ssex='%s',Sdept='%s',Dno='%s',Scheckin='%s',Test='%s' where Sno='%s'" % (u_name, u_sex, u_dept, u_dno, u_checkin, u_test, stu_id))
            messagebox.showinfo(title='恭喜',message='保存成功！')

        buttoncancel=Button(root2,text="修改",font="微软雅黑 -20",command = commit)
        buttoncancel.place(x = 80,y = 520, height = 40,width =100)

        ## 删除键
        def _del():
            cur.execute("delete from student where Sno = '%s'" % str(stu_id))
            messagebox.showinfo(title='恭喜',message='删除成功！')

        buttondel=Button(root2,text="删除",font="微软雅黑 -20",command = _del)
        buttondel.place(x = 320,y = 520, height = 40,width =100)

    buttonselect=Button(root2,text="查询",font=("微软雅黑 -20"),command=select)
    buttonselect.place(x = 340, y = 30, height = 40, width=100)

    ## 重置键
    def cancel():
        sId.set('')

    buttoncancel=Button(root2,text="重置",font="微软雅黑 -20",command = cancel)
    buttoncancel.place(x = 450,y = 30, height = 40,width =100)

    ## 退出键
    buttondel=Button(root2,text="退出",font="微软雅黑 -20",command=root2.destroy)
    buttondel.place(x = 440,y = 520, height = 40, width = 100)

    root2.mainloop()