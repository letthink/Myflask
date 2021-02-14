# Author: Lishiyao
# CreatTime: 2020/11/20 11 21
# FileName: testgame 
# Description: Simple introduction of the code

import sys                                               #(跟键盘进行交互需要用到的头文件)
import pygame
import random
PINGMU_X=1000
PINGMU_Y=600
class Snake(object):
    def jia(self):
        left, top = (0, 0)
        if self.chang:
            left, top = (self.chang[0].left, self.chang[0].top)
        node = pygame.Rect(left, top, 25, 25)
        if self.fangxiang == pygame.K_LEFT:
            node.left -= 25
        if self.fangxiang == pygame.K_RIGHT:
            node.left += 25
        if self.fangxiang == pygame.K_UP:
            node.top -= 25
        if self.fangxiang == pygame.K_DOWN:
            node.top += 25
        self.chang.insert(0, node)
    def __init__(self):
        self.fangxiang= pygame.K_RIGHT
        self.chang=[]                  #创建身体时若建立不同蛇就需要不同长度，所以先制作一个列表
        for x in range (5):
            self.jia()

    def shan(self):
        self.chang.pop()
    def isdead(self):
        if self.chang[0].x not in range(PINGMU_X ):
            return True
        if self.chang[0].y not in range(PINGMU_Y ):
            return True
        if self.chang [0] in self.chang[1:]:
            return True
        return False
    def move(self):
        self.jia()
        self.shan()
    def gaifangxiang(self,anjian):
        shuiping=[pygame.K_RIGHT ,pygame.K_LEFT ]
        shuzhi=[pygame.K_DOWN ,pygame.K_UP ]
        if anjian in shuiping+shuzhi :
            if(anjian in shuiping )and (self.fangxiang in shuiping):
                return
            if(anjian in shuzhi) and (self.fangxiang in shuzhi):
                return
            self.fangxiang =anjian

#定义一个显示字体的函数
def show_text(screen,pos,text,color,font_bold=False ,font_size=60,font_italic=False ):
    #获取字体，设置文字大小
    cur_font=pygame.font.SysFont("宋体",font_size)
    #设置加粗
    cur_font .set_bold(font_bold)
    #设置文字斜体
    cur_font.set_italic(font_italic )
    #设置文字内容
    text_fmt=cur_font .render(text,1,color)
    #绘制文字
    screen.blit(text_fmt ,pos)


class Food:
    def __init__(self):
        self.rect=pygame.Rect (-25,0,25,25)

    def remove(self):
        self.rect.x=-25

    def set(self):
        if self.rect.x==-25:
            shiwu = []
            for pos in range (25,600-25,25):
                shiwu.append(pos)
            self.rect .left =random.choice(shiwu)
            self.rect.top= random.choice(shiwu)
            print(self .rect )


def main():
    pygame.init()
    pingmu_size=(PINGMU_X,PINGMU_Y)
    pingmu =pygame.display.set_mode(pingmu_size)                 #创建屏幕大小
    scores=0
    snake = Snake()
    food = Food()
    pygame.display.set_caption('单泳齐的贪吃蛇')            #设置标题
    clock=pygame.time.Clock()                            #设置帧数
    isdead=False
    file = r'game/Dave Rodgers - Deja Vu.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                sys.exit()
            if event.type==pygame.KEYDOWN:
                snake.gaifangxiang(event.key)
                if event.key==pygame.K_SPACE and isdead :
                    return main()
        pingmu.fill((255,255,255))
        if not isdead:
            snake.move()
        for rect in snake.chang:
            pygame.draw .rect(pingmu ,(20,220,39),rect,0)
        isdead =snake.isdead()

        if isdead:
            show_text(pingmu ,(400,200),"You die!!!",(227,29,18),False ,200)
            show_text(pingmu ,(400,350),'press space to try again...',(0,0,22),False ,30)

        if food.rect ==snake.chang[0]:
            scores+=50
            food.remove()
            snake.jia()

        food.set()
        pygame.draw.rect(pingmu ,(136,0,24),food.rect,0)
        show_text(pingmu ,(50,500),'Scores:'+ str(scores),(54,62,200))
        show_text(pingmu, (100, 400), 'Shan Yongqi ‘s homework', (0,0,0))
        pygame.display.update()
        clock.tick(10)

main()