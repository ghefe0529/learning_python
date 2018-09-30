#导入数据库模块
import pymysql
#导入Flask框架，这个框架可以快捷地实现了一个WSGI应用 
from flask import Flask
#默认情况下，flask在程序文件夹中的templates子文件夹中寻找模块
from flask import render_template
#导入前台请求的request模块
from flask import request   
import traceback  
#传递根目录
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/regist')
def regist():
    return render_template('regist.html')

#获取注册请求及处理
@app.route('/registuser')
def getRigistRequest():
# 把用户名和密码注册到数据库中
    # 连接数据库，在数据库中创建数据库Testdb
    db = pymysql.connect(host="localhost",user="root",password="",database="TESTDB")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # sql插入语句
    sql = "insert into user(user,password) values( '" + request.args.get('user')+"','"+request.args.get('password')+"')"
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 注册成功之后跳转到登录界面
        return render_template('login.html')
    except:
        traceback.print_exc()
        db.rollback()
        return '注册失败'
    db.close()

# 获取登录参数及处理
@app.route('/login')
def getLoginRequest():
# 查询用户名及密码是否匹配存在
    # 连接数据库，此前在数据库中创建数据库TESTDB
    db = pymysql.connect(host="localhost",user="root",password="",database="TESTDB",port=3306)
    cursor = db.cursor()
    sql = "select * from user where user='"+request.args.get('user') + "' and password = '"+ request.args.get('password')+"'"
    print('-'*10+sql)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(len(results))
        if len(results) == 1:
            return "登录成功"
        else:
            return '用户名不正确'
        db.commit()
    except:
        traceback.print_exc()
        db.rollback()
    db.close()


if __name__ == '__main__':
    app.run(debug=True)
