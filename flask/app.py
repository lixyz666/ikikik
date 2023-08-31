from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)


username = "lixuanze"
password = "lixuanze"

@app.route("/adminlogin", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entered_username = request.form.get("username")
        entered_password = request.form.get("password")

        if entered_username == username and entered_password == password:
            return redirect(url_for("admin"))
        else:
            error = "用户名或密码错误"
            return render_template("login.html", error=error)

    return render_template("login.html")

@app.route("/admin", methods=["POST"])
def admin():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='ikikik', password="ikikik", charset='utf8', db='ikikik')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from admin"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()
    print(data_list)
    return render_template('admin.html', data_list=data_list)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    passwd = request.form.get("passwd")
    user = request.form.get("user")

    # 连接数据库
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='ikikik', password="ikikik", charset='utf8', db='ikikik')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 发送给MySQL
    sql = ("insert into admin(user, passwd) values (%s,%s)")
    cursor.execute(sql, [user, passwd])
    conn.commit()
    # 关闭
    cursor.close()
    conn.close()

@app.route("login")
def loginuser():
    return render_template("loginuser.html")

if __name__ == '__main__':
    app.run(port=7091)
