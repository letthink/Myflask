# Author: Lishiyao
# CreatTime: 2020/11/2 21 52
# FileName: testMyself 
# Description: Simple introductiong of the code

import jieba #分词
from matplotlib import  pyplot as plt #绘图
from wordcloud import WordCloud #词云
from PIL import Image   #图片处理
import numpy as np      #矩阵运算
import sqlite3          #数据库

def main():
     #准备词云所需要的文字（词语）
    con = sqlite3.connect('joblist.db')
    cur = con.cursor()
    sql = 'select info from joblist'
    data = cur.execute(sql)
    text = ""
    for item in data:
        text += item[0]
    #    print(item[0])
    #print(text)

    cur.close()
    con.close()

    cut = jieba.cut(text)
    string = ' '.join(cut)
    print(len(string))

    img = Image.open(r'.\static\assets\img\name.png')
    img_array = np.array(img)
    wc = WordCloud(
        background_color='white',
        mask = img_array,
        font_path = "simsun.ttc"              #字体位置：C:\Windows\Fonts

    )
    wc.generate_from_text(string)

    #绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off') #选择是否显示坐标轴

    flt = plt.gcf() #注意，此处应该先抓取图片，或者放在show（）之前，因为shou会产生一个空白图片，会导致存储一个空白图片文件
    plt.show()      #也可以考虑将show放在save之后

    #输出词云图片到文件
    flt.savefig(r'.\static\assets\img\wordcloud.jpg',dpi=1600)

main()