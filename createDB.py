# 创建数据库
import pymssql

## 建立连接
db = pymssql.connect()
if db:
    print("连接成功!")
mycursor = db.cursor() ### 创建一个游标对象python里的sql语句都要通过cursor来执行
db.autocommit(True)

## 建表
### dpho表 宿舍
sql = """
        IF OBJECT_ID('student') IS NOT NULL
            DROP TABLE student
        IF OBJECT_ID('dpho') IS NOT NULL
            DROP TABLE dpho
        create table dpho
        (
        Dno char(6) not null primary key,
        Dphone char(15),
        emoney char(8),
        );
      """
mycursor.execute(sql)
if sql:
    print("dpho表创建成功！")

### student表 学生
sql = """
        IF OBJECT_ID('student') IS NOT NULL
            DROP TABLE student
        create table student
        (
        Sno char(20) not null primary key,
        Sname char(20),
        Spassword char(20),
        Ssex char(20),
        Sdept char(20),
        Dno char(6),
        Scheckin smalldatetime,
        Test char(8),
        foreign key(Dno) references dpho(Dno)
        );
      """
mycursor.execute(sql)
if sql:
    print("student表创建成功！")

### supervisor表 管理员
sql = """
        IF OBJECT_ID('supervisor') IS NOT NULL
            DROP TABLE supervisor
        create table supervisor
        (
        Uname char(20) not null primary key,
        Uno char(20),
        Upassword char(20),
        Utype tinyint,
        );
      """
mycursor.execute(sql)
if sql:
    print("supervisor表创建成功！")

### dpro表 宿舍物品
sql = """
        IF OBJECT_ID('dpro') IS NOT NULL
            DROP TABLE dpro
        create table dpro
        (
        Pno char(6) not null primary key,
        Pname char(20),
        );
      """
mycursor.execute(sql)
if sql:
    print("dpro表创建成功！")

### delivery表 快递
sql = """
        IF OBJECT_ID('delivery') IS NOT NULL
            DROP TABLE delivery
        create table delivery
        (
        Sname char(20),
        Dno char(6),
        Marrive date,
        Mreceive date,
        Mnumber char(8),
        primary key(Sname,Dno,Marrive)
        );
      """
mycursor.execute(sql)
if sql:
    print("delivery表创建成功！")

### repairs表 修理
sql = """
        IF OBJECT_ID('repairs') IS NOT NULL
            DROP TABLE repairs
        create table repairs
        (
        Dno char(6),
        Pno int,
        Rsubmit date,
        Rsolve date,
        Rreason char(50),
        primary key(Dno,Pno,Rsubmit)
        );
      """
mycursor.execute(sql)
if sql:
    print("repairs表创建成功！")

### lateback表 晚归
sql = """
        IF OBJECT_ID('lateback') IS NOT NULL
            DROP TABLE lateback
        create table lateback
        (
        Sno char(20),
        Dno char(6),
        Btime datetime,
        Breason char(10),
        primary key (Sno,Dno,Btime)
        );
      """
mycursor.execute(sql)
if sql:
    print("lateback表创建成功！")

### leave表 离校
sql = """
        IF OBJECT_ID('leave') IS NOT NULL
            DROP TABLE leave
        create table leave
        (
        Sno char(20),
        Dno char(6),
        Ltime date,
        Lreturn date,
        primary key (Sno,Dno)
        );
      """
mycursor.execute(sql)
if sql:
    print("leave表创建成功！")

### inout表 出入
sql = """
        IF OBJECT_ID('inout') IS NOT NULL
            DROP TABLE inout
        create table inout
        (
        Sno char(20),
        Gstate char(8), 
        Gtime date,
        Gtemp char(8),
        primary key(Sno,Gstate)
        );
      """
mycursor.execute(sql)
if sql:
    print("inout表创建成功！")

## 插入测试数据
### dpho表
sql = """
        insert into dpho (Dno,Dphone,emoney)
        values ('01','20001','20');
        insert into dpho (Dno,Dphone,emoney)
        values ('02','20002','35');
        insert into dpho (Dno,Dphone,emoney)
        values ('03','20003','90');
        insert into dpho (Dno,Dphone,emoney)
        values ('04','20004','90');
        insert into dpho (Dno,Dphone,emoney)
        values ('05','20005','90');
      """
mycursor.execute(sql)
if sql:
    print("dpho表插入成功！")

### student表
sql = """
        INSERT INTO student (Sno,Sname,Spassword,Ssex,Sdept,Dno,scheckin,Test)
        VALUES ('10001','张三','123','男','计算机','01','2020-09-01','阴性');
        INSERT INTO student (Sno,Sname,Spassword,Ssex,Sdept,Dno,scheckin,Test)
        VALUES ('10002','王昭君','123','女','计算机','03','2020-09-01','阴性');
        INSERT INTO student (Sno,Sname,Spassword,Ssex,Sdept,Dno,scheckin,Test)
        VALUES ('10003','宫本武藏','123','男','软件','01','2020-09-01','阴性');
        INSERT INTO student (Sno,Sname,Spassword,Ssex,Sdept,Dno,scheckin,Test)
        VALUES ('10004','露娜','123','女','网安','05','2020-09-01','阴性');
        INSERT INTO student (Sno,Sname,Spassword,Ssex,Sdept,Dno,scheckin,Test)
        VALUES ('10005','澜朋友','123','男','软件','02','2020-09-01','阴性');
      """
mycursor.execute(sql)
if sql:
    print("student表插入成功！")

### dpro表
sql = """
        insert into dpro (Pno,Pname)
        values ('01','风扇');
        insert into dpro (Pno,Pname)
        values ('02','空调');
        insert into dpro (Pno,Pname)
        values ('03','灯管');
        insert into dpro (Pno,Pname)
        values ('04','椅子');
      """
mycursor.execute(sql)
if sql:
    print("dpro表插入成功！")

### delivery表
sql = """
        insert into delivery (Sname,Dno,Marrive,Mreceive,Mnumber)
        values ('澜朋友','02','2022-6-17','2022-6-20','2');
        insert into delivery (Sname,Dno,Marrive,Mreceive,Mnumber)
        values ('澜朋友','02','2022-6-16','2022-6-18','1');
        insert into delivery (Sname,Dno,Marrive,Mreceive,Mnumber)
        values ('宫本武藏','01','2022-6-17','2022-6-19','3');
        insert into delivery (Sname,Dno,Marrive,Mreceive,Mnumber)
        values ('露娜','05','2022-6-12','2022-6-12','1');
        insert into delivery (Sname,Dno,Marrive,Mreceive,Mnumber)
        values ('张三','01','2022-6-11','2022-6-15','4');
        insert into delivery (Sname,Dno,Marrive,Mreceive,Mnumber)
        values ('王昭君','03','2022-6-17','2022-6-19','2');
      """
mycursor.execute(sql)
if sql:
    print("delivery表插入成功！")

### repairs表
sql = """
        insert into repairs (Dno,Pno,Rsubmit,Rsolve,Rreason)
        values ('01','03','2022-5-17','2022-5-19','灯管烧了');
        insert into repairs (Dno,Pno,Rsubmit,Rsolve,Rreason)
        values ('02','01','2022-6-02','2022-6-07','风扇不转了');
        insert into repairs (Dno,Pno,Rsubmit,Rsolve,Rreason)
        values ('04','02','2022-6-10','2022-6-12','空调没雪种了，很热');
      """
mycursor.execute(sql)
if sql:
    print("repairs表插入成功！")

### lateback表
sql = """
        insert into lateback (Sno,Dno,Btime,Breason)
        values ('10001','01','2022-06-01 23:22:09','自习室学习');
        insert into lateback (Sno,Dno,Btime,Breason)
        values ('10002','03','2022-06-01 23:22:09','操场唱歌');
      """
mycursor.execute(sql)
if sql:
    print("lateback表插入成功！")

### leave表
sql = """
        insert  into leave(Sno,Dno,Ltime,Lreturn)
        values ('10001','01','2022-5-12','2022-6-20')
        insert  into leave(Sno,Dno,Ltime,Lreturn)
        values ('10002','03','2022-5-12','2022-6-22')
        insert  into leave(Sno,Dno,Ltime,Lreturn)
        values ('10003','01','2022-5-12','2022-6-18')
        insert  into leave(Sno,Dno,Ltime,Lreturn)
        values ('10004','05','2022-5-12','2022-6-20')
        insert  into leave(Sno,Dno,Ltime,Lreturn)
        values ('10005','02','2022-5-12','2022-6-19')
      """
mycursor.execute(sql)
if sql:
    print("leave表插入成功！")

### inout表
sql = """
        insert into inout(Sno,Gstate,Gtime,Gtemp)
        values ('10001','出','2022-6-19','36.3 C')
        insert into inout(Sno,Gstate,Gtime,Gtemp)
        values ('10002','出','2022-6-19','36.3 C')
        insert into inout(Sno,Gstate,Gtime,Gtemp)
        values ('10003','入','2022-6-19','36.3 C')
        insert into inout(Sno,Gstate,Gtime,Gtemp)
        values ('10004','出','2022-6-19','36.3 C')
        insert into inout(Sno,Gstate,Gtime,Gtemp)
        values ('10005','入','2022-6-19','36.3 C')
        insert into inout(Sno,Gstate,Gtime,Gtemp)
        values ('10006','出','2022-6-19','36.3 C')
      """
mycursor.execute(sql)
if sql:
    print("inout表插入成功！")

### supervisor表
sql = """
        insert into supervisor(Uname,Uno,Upassword,Utype)
        values ('嬴政','201','321',1);
        insert into supervisor(Uname,Uno,Upassword,Utype)
        values ('唐太宗','202','321',1);
        insert into supervisor(Uname,Uno,Upassword,Utype)
        values ('魏忠贤','203','321',0);
      """
mycursor.execute(sql)
if sql:
    print("supervisor表插入成功！")

print("数据库配置完成！")