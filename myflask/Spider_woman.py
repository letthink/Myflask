# Author: Lishiyao
# CreatTime: 2020/11/3 14 47
# FileName: Spider_woman 
# Description: Simple introductiong of the code

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
# import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import os   #引入os模块就行文件是否存在的判断

def main():
    baseurl = "https://cn.japanese-jobs.com/city-dalian?page="   # 1.爬取网页
    datalist = getData(baseurl)
    # print("______________________________")
    # print(datalist)
    # 3.保存数据
    dbpath = "joblist.db"
    tmp = saveDatadb(datalist,dbpath)
    print(tmp)
    # askURL("https://movie.douban.com/top250?start=")


# 创建全局变量，创建正则表达式对象，表示规则（字符串的模式
# 对应招聘链接
findLink = re.compile(r'<a data-cassette-anchor="target" href="(.*?)" target="_blank">')
#对应HTML代码：<a href="https://cn.japanese-jobs.com/jobs/details/33950" data-cassette-anchor="target">（高级）日语教研</a>
# 制位
findJob = re.compile(r'k">(.*)</a>')
# 公司名称
findName = re.compile(r'</span> (.*?)                </li>')
# 公司地址
findAddress = re.compile(r'<span class="jj-cassette__icon icon--place"></span>(.*? .*)\r')
# 公司薪资
findSalary = re.compile(r'</span>(.*?) RMB')
# 公司宣语
findInfo = re.compile(r'<p class="jj-cassette__comment">(.*)</p>')


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(1, 16):  # 调用获取页面信息的函数，15次
        # url =baseurl
        url = baseurl + str(i)
        html = askURL(url)  # 保存获取到的网页源码
        # print(html)

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div',class_="jj-cassette"):  # 查找符合要求的字符串，形成列表 <div class="e">
            # print(item)   #测试：查看招聘e的全部信息
            data = []  # 保存一条招聘的所有信息
            item = str(item)    #数据转化，便于使用正则规则选择
        #
            # 职位详情的链接
            link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定的字符串
            print(link)
            data.append(link)  # 添加链接
            Job = re.findall(findJob, item)[0]
            print(Job)
            data.append(Job)
            # data.append(rating)  # 添加评分
            Name = re.findall(findName, item)[0]  # 获取对应职务
            print(Name)
            data.append(Name)
            Address = re.findall(findAddress, item)[0] #获得公司地址
            print(Address)
            data.append(Address)
            Salary = re.findall(findSalary, item)    #获得工资有些工资是面议
            if Salary:
                pass
            else:
                Salary = "面议"
            print(Salary)
            Salary = "".join(Salary)
            data.append(Salary)
            Info = []
            Info = re.findall(findInfo, item)   #获得公司介绍
            print(Info)
            if Info:
                pass
            else:
                Info.append("暂无介绍")   #考虑到爬取的网页中，并非所有公司都有介绍，避免数据库库空留，添加字符串占据位置
            Info = Info[0]        #转化数据格式伪字符串，便于数据库存储
            print(type(Info))
            # Info.replace( "'", "" ) #（已解决）无法去除单引号和括号？---------------------------------------------------------------------
            print(Info)
            data.append(Info)

            datalist.append(data)  # 把处理好的一条招聘信息放入datalist
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveDatadb(datalist, dbpath):
    print("--------------------------------------------------------------")
    print(datalist)
    for data in datalist:
        print(data[0],"--------------------------------------------------")
        for index in range(len(data)):
            data[index] = '"' +data[index]+'"' #将每个数据的前后都加上双引号

    test = r".\joblist.db"  #使用相对路径获得数据库的位置
    if os.path.exists(test):    #通过判断数据库是否存在选择更新或新建数据库
        i = 1
        conn = sqlite3.connect(dbpath)
        cur = conn.cursor()
        for data in datalist:
            sql ='''
                update joblist
                set link=%s,job=%s,name=%s,address=%s,salary=%s,info=%s
                where id=%s;
                '''%(data[0],data[1],data[2],data[3],data[4],data[5],i)
            i += 1
            print(sql)
            cur.execute(sql)
            conn.commit()
    else:
        init_db(dbpath)
        conn = sqlite3.connect(dbpath)
        cur = conn.cursor()
        for data in datalist:
            sql = '''
                    insert into joblist (
                    link,job,name,address,salary,info) 
                    values(%s)''' % ",".join(data)
            print(sql)
            cur.execute(sql)
            conn.commit()
    cur.close()
    conn.close()
print("We can do next")


def init_db(dbpath):
    sql = '''
        create table joblist(
        id integer primary key AUTOINCREMENT,
        job text not null,
        name text not null,
        address char(30),
        salary real,
        info text,
        link text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()



if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    # init_db("joblist.db")
    print("爬取完毕！")