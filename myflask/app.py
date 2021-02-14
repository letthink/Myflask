from flask import Flask,render_template,request,url_for #使用flask模块
import sqlite3  #使用数据库模块
import Spider_woman  #调用爬虫程序
import json #与前端数据进行交互
app = Flask(__name__)
# import Cloudword  #如果需要每次都更新词语图片，可以取消注释
# Cloudword.main()

@app.route('/')
def index():
    num = [] #给出数据总数
    con = sqlite3.connect("joblist.db")
    cur = con.cursor()
    sql1 = "select count(id) from joblist"   #以id作为计数标准
    cur.execute(sql1)
    temp = cur.fetchall()
    print(temp)
    num = temp[0]
    # print(num)
    # data = cur.fetchall()
    # for item in temp:
    #     num.append(temp)
    print("S-------------------------------------------------------------")
    print(type(num))    #测试
    num = list(num)
    print(num)
    print(num[0])
    cur.close()
    con.close()
    return render_template("index.html",num1=num[0])

@app.route('/index')
def home():
    return index()

@app.route('/update')
def update():
    return render_template("update.html")

@app.route('/temp')
def temp():
    Spider_woman.main()  # 避免加载动画无法显示与数据库无法更新的矛盾，选择使用一个复刻网页解决此问题
    num = []  # 给出数据总数
    con = sqlite3.connect("joblist.db")
    cur = con.cursor()
    sql1 = "select count(id) from joblist"  # 以id作为计数标准
    cur.execute(sql1)
    temp = cur.fetchall()
    print(temp)
    num = temp[0]
    # print(num)
    # data = cur.fetchall()
    # for item in temp:
    #     num.append(temp)
    num = list(num)
    cur.close()
    con.close()
    #return render_template("index.html")
    print("-------------------------------------------------------------")
    print("爬取完毕，数据更新")
    return render_template("temp.html",num1=num[0])


@app.route('/job')
def job():
    datalist = []
    con = sqlite3.connect("joblist.db")
    cur = con.cursor()
    sql = "select * from joblist"
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("job.html", jobs = datalist)


@app.route('/score')
def score():
    salary = []  #工资
    num = []    #每个评分所统计出的岗位
    con = sqlite3.connect("joblist.db")
    cur = con.cursor()
    sql1 = "select salary,count(salary) from joblist group by salary"   #以工资为标准划分区间
    data1 = cur.execute(sql1)
    for item in data1:
        salary.append(str(item[0]))
        num.append(item[1])
    location = [] #所处地理位置
    count = [] #每个地理位置所统计出来的岗位
    sql2 = "select address,count(address) from joblist group by address"    #以地理位置为标准划分取件
    data2 = cur.execute(sql2)
    for item in data2:
        location.append(str(item[0]))
        count.append(item[1])
    two = dict(zip(location,count))   #将列表转换为字典
    lenth = len(location)               #将对应列表长度数据传入
    print(location)
    print(count)
    print(two)
    cur.close()
    con.close()
    return render_template("score.html",salary= salary,num=num,location=location,count=count,two=two,lenth=lenth)


@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("myself.html") #注意直接执行html是“无法调用“其他文件，（也就说外置的js，css无法使用）但是可以通过python使用@app.route()进行调用

@app.route('/myself')
def myself():
    return render_template("myself.html")

# @app.route('/original1')
# def original1():    #注意直接执行html是“无法调用“其他文件，（也就说外置的js，css无法使用）但是可以通过python使用@app.route()进行调用
#     return render_template("myself.html")
# @app.route('/save',methods=['POST'])
# def save():   较为可惜的是，并没有合适足够的基础和时间精力，研究透如何html传参给服务器并传参给py后端，直接调用脚本，终究是需要app.py做中介
#     name = request.form['name']
#     print('------------------',name)
#     return name
@app.route('/game')
def game():
     #技术问题，无法提前申明（如果提前申明会导致游戏直接打开，应该是game那没有启用开始关键词）
    import game
    # snake.main()
    return render_template("game.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2021)


