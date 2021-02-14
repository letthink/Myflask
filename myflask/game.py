# coding=utf-8
import pygame
from pygame.locals import *
import sys
import random

def main():
    file = r'game/Dave Rodgers - Deja Vu.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1,0)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    bg_color = (70, 70, 70)  # 背景颜色
    SCREEN_SIZE = [400, 800]  # 屏幕大小
    car_SIZE = [20, 20]  # 车大小
    ball_SIZE = [15, 30]  # 球的尺寸

    class Game(object):
        auto = 1  # 自动避障速度，与方向，正向左，负向右
        def __init__(self):
            # self.up = 800
            pygame.init()
            self.clock = pygame.time.Clock()  # 定时器
            self.screen = pygame.display.set_mode(SCREEN_SIZE)
            pygame.display.set_caption('智能体避障')  # 设置标题

            # ball 初始位置
            self.ball_pos_x = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 2
            self.ball_pos_y = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 2
            self.ball_pos1_x = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos1_y = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos2_x = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos2_y = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos3_x = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos3_y = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos4_x = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos4_y = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos5_x = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos5_y = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos6_x = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos6_y = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos7_x = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            self.ball_pos7_y = SCREEN_SIZE[0] // 2 - ball_SIZE[0] / 3
            # ball 移动方向
            # self.ball_dir_x = -1 #-1:left 1:right
            self.ball_dir_y = 1  # 1:down 速度
            # self.ball_dir_y1 = 2  # 1:down 速度

            self.ball_pos = pygame.Rect(self.ball_pos_x, self.ball_pos_y, ball_SIZE[0], ball_SIZE[0])
            self.ball_pos1 = pygame.Rect(self.ball_pos1_x, self.ball_pos1_y, ball_SIZE[0], ball_SIZE[0])
            self.ball_pos2 = pygame.Rect(self.ball_pos2_x, self.ball_pos2_y, ball_SIZE[0], ball_SIZE[0])
            self.ball_pos3 = pygame.Rect(self.ball_pos3_x, self.ball_pos3_y, ball_SIZE[0], ball_SIZE[0])
            self.ball_pos4 = pygame.Rect(self.ball_pos4_x, self.ball_pos4_y, ball_SIZE[0], ball_SIZE[0])
            self.ball_pos5 = pygame.Rect(self.ball_pos5_x, self.ball_pos5_y, ball_SIZE[0], ball_SIZE[0])
            self.ball_pos6 = pygame.Rect(self.ball_pos6_x, self.ball_pos6_y, ball_SIZE[0], ball_SIZE[0])
            self.ball_pos7 = pygame.Rect(self.ball_pos7_x, self.ball_pos7_y, ball_SIZE[0], ball_SIZE[0])

            #主角的控制
            self.score = 0
            self.car_pos_x = SCREEN_SIZE[0] // 2 - car_SIZE[0] // 2
            self.car_pos_y = SCREEN_SIZE[0]
            self.car_pos = pygame.Rect(self.car_pos_x, SCREEN_SIZE[1] - car_SIZE[1], car_SIZE[0], car_SIZE[1])
            self.car_pos = pygame.Rect(self.car_pos_y, SCREEN_SIZE[1] - car_SIZE[1], car_SIZE[0], car_SIZE[1])

            # self.car_pos = pygame.Rect(self.car_pos_y, SCREEN_SIZE[1] - car_SIZE[1], car_SIZE[0], ball_SIZE[1])

        def car_move_left(self):  # 左移
            self.car_pos_x = self.car_pos_x - 5

        def car_move_right(self):  # 右移
            self.car_pos_x = self.car_pos_x + 5

        def car_move_up(self):  # 上移
            self.car_pos_y +=  4

        def car_move_down(self):  # 下移
            self.car_pos_y = self.car_pos_y - 4

        def run(self):
            gear = 0
            pygame.mouse.set_visible(1)  # 移动鼠标可见
            car_move_left = False
            car_move_right = False
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:  # 当按下关闭按键
                        pygame.quit()
                        sys.exit()  # 接收到退出事件后退出程序

                    # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 鼠标左键按下
                    #     car_move_left = True
                    # elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # 左键弹起
                    #     car_move_left = False
                    # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 右键
                    #     car_move_right = True
                    # elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:  # 左键弹起
                    #     car_move_right = False

                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.car_pos.x > 0:
                            car_move_left = True
                            # print(self.car_pos_x,"x--x")
                        if (event.key == pygame.K_RIGHT or event.key == K_d) and self.car_pos.x < 400-car_SIZE[1]:
                            # print(self.car_pos_x,"xxx")
                            car_move_right = True
                        if (event.key == pygame.K_UP or event.key == K_w) and self.car_pos.top > 0 and gear>-4:
                            car_move_up = True
                            # print("UP")
                            gear -= 2  #通过普通变量，进行车速挡位调节,注意正反相异
                        if (event.key == pygame.K_DOWN or event.key == K_s) and self.car_pos.bottom < 800 and gear<4:
                            gear += 2
                            # print("DOWN")
                    if event.type == pygame.KEYUP:
                        car_move_right = False
                        car_move_left = False
                        # gear = 0
                if self.car_pos.top < 100:  #避免智能体自己太靠前
                    gear += 1

                if car_move_left == True and car_move_right == False:
                    self.car_move_left()
                if car_move_left == False and car_move_right == True:
                    self.car_move_right()
                if self.car_pos.bottom >800 :  #碰撞反弹效果
                    gear = -1
                    # print("出现啦")
                if self.car_pos.top < 0 :
                    gear = 1
                if self.car_pos.left < 0:       #地图围栏
                    self.car_pos_x = 0
                if self.car_pos.left > 400:
                    self.car_pos_x = 380
                    # print("OVER")
                # print("right",self.car_pos.right)
                # if car_move_up == True and car_move_down == False:
                #     self.car_move_up()
                # if car_move_down == False and car_move_up == True:
                #     self.car_move_down()

                # 自动避障
                if (-car_SIZE[0] < self.car_pos.left - self.ball_pos.left < ball_SIZE[0] and -car_SIZE[0] - ball_SIZE[
                    0] < self.car_pos.top - self.ball_pos.bottom < 100) \
                        or (
                        -car_SIZE[0] < self.car_pos.left - self.ball_pos1.left < ball_SIZE[0] and -car_SIZE[0] - ball_SIZE[
                    0] < self.car_pos.top - self.ball_pos1.bottom < 100) \
                        or (
                        -car_SIZE[0] < self.car_pos.left - self.ball_pos2.left < ball_SIZE[0] and -car_SIZE[0] - ball_SIZE[
                    0] < self.car_pos.top - self.ball_pos2.bottom < 100) \
                        or (
                        -car_SIZE[0] < self.car_pos.left - self.ball_pos3.left < ball_SIZE[0] and -car_SIZE[0] - ball_SIZE[
                    0] < self.car_pos.top - self.ball_pos3.bottom < 100) \
                        or (
                        -car_SIZE[0] < self.car_pos.left - self.ball_pos4.left < ball_SIZE[0] and -car_SIZE[0] - ball_SIZE[
                    0] < self.car_pos.top - self.ball_pos4.bottom < 100) \
                        or (
                        -car_SIZE[0] < self.car_pos.left - self.ball_pos5.left < ball_SIZE[0] and -car_SIZE[0] - ball_SIZE[
                    0] < self.car_pos.top - self.ball_pos5.bottom < 100) \
                        or (
                        -car_SIZE[0] < self.car_pos.left - self.ball_pos6.left < ball_SIZE[0] and -car_SIZE[0] - ball_SIZE[
                    0] < self.car_pos.top - self.ball_pos6.bottom < 100) \
                        or (
                        -car_SIZE[0] < self.car_pos.left - self.ball_pos7.left < ball_SIZE[0] and -car_SIZE[0] - ball_SIZE[
                    0] < self.car_pos.top - self.ball_pos7.bottom < 100):
                    if self.car_pos.left <100:  #当智能体过于靠近左端，开始向右端进行
                        self.auto *= -1
                    if self.car_pos.left >300:  #当智能体过于靠近右端，开始向左端进行
                        self.auto *= -1


                    # print(self.auto,"===========")
                    if gear < 3:
                        gear += 1  #左右避障同时向后撤，当障碍越近向后的速度越快


                    self.car_pos_x -= self.auto #智能体默认向左端进行
                    # print("自动避障",self.car_pos.left)

                self.screen.fill(bg_color)
                self.car_pos.left = self.car_pos_x
                self.car_pos.bottom += gear
                # gear = 0
                pygame.draw.rect(self.screen, BLACK, self.car_pos)


                ## 球移
                self.ball_pos.bottom += self.ball_dir_y * random.randint(3,6)
                pygame.draw.rect(self.screen, WHITE, self.ball_pos)
                self.ball_pos1.bottom += self.ball_dir_y * random.randint(0,5)
                pygame.draw.rect(self.screen, WHITE, self.ball_pos1)
                self.ball_pos2.bottom += self.ball_dir_y * random.randint(0,5)
                pygame.draw.rect(self.screen, WHITE, self.ball_pos2)
                self.ball_pos3.bottom += self.ball_dir_y * random.randint(0,5)
                pygame.draw.rect(self.screen, WHITE, self.ball_pos3)
                self.ball_pos4.bottom += self.ball_dir_y * random.randint(0,5)
                pygame.draw.rect(self.screen, WHITE, self.ball_pos4)
                self.ball_pos5.bottom += self.ball_dir_y * random.randint(0,5)
                pygame.draw.rect(self.screen, WHITE, self.ball_pos5)
                self.ball_pos6.bottom += self.ball_dir_y * random.randint(0,5)
                pygame.draw.rect(self.screen, WHITE, self.ball_pos6)
                self.ball_pos7.bottom += self.ball_dir_y * random.randint(0,5)
                pygame.draw.rect(self.screen, WHITE, self.ball_pos7)
                # self.ball_pos.bottom += self.ball_dir_y2 * 3
                # pygame.draw.rect(self.screen, WHITE, self.ball_pos)

                #多个球
                ## 判断是否碰撞
                # if  (-600 < (self.car_pos.left**2+self.car_pos.top**2) - (self.ball_pos.left**2+self.ball_pos.bottom**2) <= 600) or (
                #         -600 < (self.car_pos.left ** 2 + self.car_pos.top ** 2) - (
                #         -600 < (self.car_pos.right**2+self.car_pos.top**2) -self.ball_pos.right ** 2 + self.ball_pos.bottom ** 2) <= 600
                # ) or (-600 < (self.car_pos.left**2+self.car_pos.top**2) - (self.ball_pos1.left**2+self.ball_pos1.bottom**2) <= 600) or (
                #         -600 < (self.car_pos.left ** 2 + self.car_pos.top ** 2) - (
                #         -600 < (self.car_pos.right**2+self.car_pos.top**2) -self.ball_pos1.right ** 2 + self.ball_pos1.bottom ** 2) <= 600
                # ) :
                # print("x:",self.car_pos_x,"top.y",self.car_pos.top)
                # print("z == x",self.car_pos.left)
                # print("ball.left:",self.ball_pos.left,"ball.bottom",self.ball_pos.bottom)
                if (-car_SIZE[0] < self.car_pos.left - self.ball_pos.left < ball_SIZE[0] and -car_SIZE[0]-ball_SIZE[0] < self.car_pos.top - self.ball_pos.bottom < 1) \
                        or (-car_SIZE[0] < self.car_pos.left - self.ball_pos1.left < ball_SIZE[0] and -car_SIZE[0]-ball_SIZE[0] < self.car_pos.top - self.ball_pos1.bottom < 1) \
                        or (-car_SIZE[0] < self.car_pos.left - self.ball_pos2.left < ball_SIZE[0] and -car_SIZE[0]-ball_SIZE[0] < self.car_pos.top - self.ball_pos2.bottom < 1) \
                        or (-car_SIZE[0] < self.car_pos.left - self.ball_pos3.left < ball_SIZE[0] and -car_SIZE[0]-ball_SIZE[0] < self.car_pos.top - self.ball_pos3.bottom < 1) \
                        or (-car_SIZE[0] < self.car_pos.left - self.ball_pos4.left < ball_SIZE[0] and -car_SIZE[0]-ball_SIZE[0] < self.car_pos.top - self.ball_pos4.bottom < 1) \
                        or (-car_SIZE[0] < self.car_pos.left - self.ball_pos5.left < ball_SIZE[0] and -car_SIZE[0]-ball_SIZE[0] < self.car_pos.top - self.ball_pos5.bottom < 1) \
                        or (-car_SIZE[0] < self.car_pos.left - self.ball_pos6.left < ball_SIZE[0] and -car_SIZE[0]-ball_SIZE[0] < self.car_pos.top - self.ball_pos6.bottom < 1) \
                        or (-car_SIZE[0] < self.car_pos.left - self.ball_pos7.left < ball_SIZE[0] and -car_SIZE[0]-ball_SIZE[0] < self.car_pos.top - self.ball_pos7.bottom < 1) :

                    # self.score += 1
                    # print("Score: ", self.score, end='\r')
                # elif self.car_pos.top <= self.ball_pos.bottom and (
                #         self.car_pos.left > self.ball_pos.right or self.car_pos.right < self.ball_pos.left):
                    print("智能体得分（躲避的障碍物数量）: ", self.score)
                    pygame.mixer.music.stop()
                    return self.score

                ## 更新球下落的初始位置
                if 800 <= self.ball_pos.bottom:
                        self.ball_pos_x = random.randint(0, SCREEN_SIZE[0] - ball_SIZE[0])
                        self.ball_pos_y = random.randint(0,5)
                        self.ball_pos = pygame.Rect(self.ball_pos_x, self.ball_pos_y, ball_SIZE[0], ball_SIZE[1])
                        self.score += 1
                if 800 <= self.ball_pos1.bottom:
                        self.ball_pos1_x = random.randint(0, SCREEN_SIZE[0] - ball_SIZE[0])
                        self.ball_pos1_y = 0
                        self.ball_pos1 = pygame.Rect(self.ball_pos1_x, self.ball_pos1_y, ball_SIZE[0], ball_SIZE[1])
                        self.score += 1
                if 800 <= self.ball_pos2.bottom:
                        self.ball_pos2_x = random.randint(0, SCREEN_SIZE[0] - ball_SIZE[0])
                        self.ball_pos2_y = 0
                        self.ball_pos2 = pygame.Rect(self.ball_pos2_x, self.ball_pos2_y, ball_SIZE[0], ball_SIZE[1])
                        self.score += 1
                if 800 <= self.ball_pos3.bottom:
                        self.ball_pos3_x = random.randint(0, SCREEN_SIZE[0] - ball_SIZE[0])
                        self.ball_pos3_y = 0
                        self.ball_pos3 = pygame.Rect(self.ball_pos3_x, self.ball_pos3_y, ball_SIZE[0], ball_SIZE[1])
                        self.score += 1
                if 800 <= self.ball_pos4.bottom:
                        self.ball_pos4_x = random.randint(0, SCREEN_SIZE[0] - ball_SIZE[0])
                        self.ball_pos4_y = -5
                        self.ball_pos4 = pygame.Rect(self.ball_pos4_x, self.ball_pos4_y, ball_SIZE[0], ball_SIZE[1])
                        self.score += 1
                if 800 <= self.ball_pos5.bottom:
                        self.ball_pos5_x = random.randint(0, SCREEN_SIZE[0] - ball_SIZE[0])
                        self.ball_pos5_y = -10
                        self.ball_pos5 = pygame.Rect(self.ball_pos5_x, self.ball_pos5_y, ball_SIZE[0], ball_SIZE[1])
                        self.score += 1
                if 800 <= self.ball_pos6.bottom:
                        self.ball_pos6_x = random.randint(0, SCREEN_SIZE[0] - ball_SIZE[0])
                        self.ball_pos6_y = -15
                        self.ball_pos6 = pygame.Rect(self.ball_pos6_x, self.ball_pos6_y, ball_SIZE[0], ball_SIZE[1])
                        self.score += 1
                if 800 <= self.ball_pos7.bottom:
                        self.ball_pos7_x = random.randint(0, SCREEN_SIZE[0] - ball_SIZE[0])
                        self.ball_pos7_y = -20
                        self.ball_pos7 = pygame.Rect(self.ball_pos7_x, self.ball_pos7_y, ball_SIZE[0], ball_SIZE[1])
                        self.score += 1


                pygame.display.update()  # 更新软件界面显示
                self.clock.tick(60)

    game = Game()
    game.run()  # 启动

main()
# if 400 < mouse_x < 450 and 125 < mouse_y < 175:
#                     print("SHOW")
#                     screen.blit(heng, (400, 125))
#                 if 570 < mouse_x < 670 and 124 < mouse_y < 175:
#                     print("SHOW")
#                     screen.blit(R2,(570,124))
#                 if 118 < mouse_x < 168 and 256 < mouse_y < 306:
#                     screen.blit(heng, (118, 256))
#                 if 267 < mouse_x < 319 and 256 < mouse_y < 306:
#                     screen.blit(shu,(267,256))
#                 if 120 < mouse_x < 169 and 413 < mouse_y < 513:
#                     screen.blit(R1,(120,413))
#                 if 271 < mouse_x < 318 and 413 < mouse_y < 513:
#                     screen.blit(R1,(271,413))
'''
                if r_flag == 2:
                    if event.key == pygame.K_r:
                        R_1 += 1
                        R_1_str = SHOW_TEXT(R_1)
                        screen.blit(R_1_str,(570,180))
                    if event.key == pygame.K_e:
                        V_1 += 1
                        V_1_str = SHOW_TEXT(V_1)
                        screen.blit(V_1_str,(400,180))
                    if event.key == pygame.K_a:
                        A_1 += 1
                        A_1_str = SHOW_TEXT(A_1)
                        screen.blit(A_1_str,(175,260))
                    if event.key == pygame.K_s:
                        V_2 += 1
                        V_2_str = SHOW_TEXT(V_2)
                        screen.blit(V_2_str,(323,260))
                    if event.key == pygame.K_z:
                        R_2 += 1
                        R_2_str = SHOW_TEXT(R_2)
                        screen.blit(R_2_str,(172,443))
                    if event.key == pygame.K_x:
                        R_3 +=1
                        R_3_str = SHOW_TEXT(R_3)
                        screen.blit(R_3_str,(321,443))
'''