"""
利用pygame制作坦克大战游戏
pygame官方文档网址：https://www.pygame.org/docs/

"""
import pygame

pygame.init()

HEIGHT = 600
WIDTH = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption('tank game-1.0')


class MainGame:

    def __init__(self):
        pass

    def startGame(self):
        while True:
            screen.fill(pygame.Color(200, 200, 200))
            pygame.display.flip()
            clock.tick(60)

            self.runEvent()

    def runEvent(self):
        eventList = pygame.event.get()
        for e in eventList:
            if e.type == pygame.QUIT:
                self.endGame()
            if e.type == pygame.KEYDOWN:
                k = e.key
                if e.key == pygame.K_LEFT:
                    print('tank left move')
                elif k == pygame.K_RIGHT:
                    print('tank right move')
                elif k == pygame.K_UP:
                    print('tank up move')
                elif k == pygame.K_DOWN:
                    print('tank down move')

        def eventKey():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                print('www')
        eventKey()

    def endGame(self):
        exit()


class Entity:
    def __init__(self):
        pass

    def dispaly(self):
        pass


class Tank(Entity):
    def __init__(self):
        pass

    def shot(self):
        pass

    def move(self):
        pass


class MyTank(Tank):
    def __init__(self):
        pass


class EnemyTank(Tank):
    def __init__(self):
        pass


class Bullet(Entity):
    def __init__(self):
        pass

    def move(self):
        pass


class Explode(Entity):
    def __init__(self):
        pass


class Wall(Entity):
    def __init__(self):
        pass


class Music:
    def __init__(self):
        pass

    def playMusic(self):
        pass


MainGame().startGame()
