from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, img_name, x, y, w, h, speed):
        super().__init__()
        self.pic = transform.scale(image.load(img_name), (w,h))
        self.rect = self.pic.get_rect()
        self.rect.x, self.rect.y = x, y
        self.speed = speed
    
    def reset(self):
        window.blit(self.pic, (self.rect.x, self.rect.y))
    
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >= 1:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <= win_w - 80:
            self.rect.x += self.speed

win_w, win_h = 700,500
window = display.set_mode((win_w, win_h))
crocc = Player("croc.jpg",  win_w- 390, win_h-100, 80, 80, 5 )
back = transform.scale(image.load("fon.jpg"), (700,500))

mixer.init()
mixer.musik.load("название музыки")

mixer.musik.play()



timer = time.Clock()
FPS = 60

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(back, (0,0))
        crocc.update()
        crocc.reset()
        display.update()
    timer.tick(FPS)