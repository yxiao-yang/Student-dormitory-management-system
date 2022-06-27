import createDB
import login
import button1
import button2
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

## 主页
def home_stu():
    ## 设置UI界面
    root0 = Tk()
    root0.resizable(False,False) ### 禁止最大化按钮
    root0.minsize(600,600) ### 最小尺寸
    root0.maxsize(600,600) ### 最大尺寸
    root0.title("学生宿舍管理系统(学生端)") ### 窗口名
    root0.config(width=600)
    root0.config(height=600)

    ## 添加窗口背景图片
    canvas = tkinter.Canvas(root0, width = 600, height = 600, bg = 'white') ### 设置canvas大小及颜色
    image = Image.open('home.png') ### 插入图片位置
    im = ImageTk.PhotoImage(image) ### 用photoImage打开图片
    canvas.create_image(200, 170, image=im) ### 使用creat_image将图片添加到Canvas
    canvas.pack()

    ## 按钮
    buttonSign = Button(root0, text = "学生信息查询", font = ("微软雅黑 -20"), command = button1.sel_stu)
    buttonSign.place(x = 90, y = 100, height = 40, width = 180)
    buttonSign = Button(root0, text = "快递信息查询", font = ("微软雅黑 -20"), command = button2.sel_delivery)
    buttonSign.place(x = 330, y = 100, height = 40, width = 180)
    buttonSign = Button(root0, text = "报修记录", font = ("微软雅黑 -20"))
    buttonSign.place(x = 90, y = 180, height = 40, width = 180)
    buttonSign = Button(root0, text = "离(返)校记录", font = ("微软雅黑 -20"))
    buttonSign.place(x = 330, y = 180, height = 40, width = 180)
    buttonSign = Button(root0, text = "宿舍电费查询", font = ("微软雅黑 -20"))
    buttonSign.place(x = 90, y = 260, height = 40, width = 180)
    buttonSign = Button(root0, text = "出(入)宿舍记录", font = ("微软雅黑 -20"))
    buttonSign.place(x = 330, y = 260, height = 40, width = 180)
    buttonSign = Button(root0, text = "修改密码", font = ("微软雅黑 -20"))
    buttonSign.place(x = 90, y = 340, height = 40, width = 180)
    buttonSign = Button(root0, text = "退出", font = ("微软雅黑 -20"), command = root0.destroy)
    buttonSign.place(x = 330, y = 340, height = 40, width = 180)
    root0.mainloop()



if __name__ == "__main__":
    login.Login() ### 登录窗口
    home_stu() ### 主菜单