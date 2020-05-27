from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'itheima'      # 保证密码不会被混淆关键字


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':

        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if not all([username, password, password2]):
            flash(u"参数不完整")     # 编码问题加一个u
        elif password != password2:
            flash(u"密码不一致")
        else:
            print("成功")
            return "success"

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
