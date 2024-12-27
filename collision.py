import pygame 
import random 
pygame.init()
screen_width, screen_height= 500,400
bg=pygame.image.load("bg.png")
background_image=pygame.transform.scale(bg(screen_width,screen_height))
class Sprite(pygame.sprite.Sprite):
    def init__(self,color,height,width):
        super().init__()

    
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color("blue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()

    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change,screen_width-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+y_change,screen_height-self.rect.height),0)

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("sprite collision")
all_sprites=pygame.spprite.Group()


sp1=Sprite(pygame.Color("black"),20,30)
sp1.rect.x=random.randint(0,screen_width-sp1.rect.width)
sp1.rect.y=random.randint(0,screen_height-sp1.rect.height)



sp2=Sprite(pygame.Color("red"),20,30)
sp2.rect.x=random.randint(0,screen_width-sp2.rect.width)
sp1.rect.y=random.randint(0,screen_height-sp2.rect.height)




all_sprites.add(sp2)
running=True
won=False

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
            
            if not won:
                keys=pygame.key.get_pressed()
                x_change=(keys[pygame.K_Right]-keys[pygame.K.Left])*speed
                y_change=(keys[pygame.K_DOWN]-keys[pygame.K.UP])*speed

                sp1.move(x_change,y_change)

                if sp1.rect.colliderect(sp2.rect):
                    all_sprites.remove(sp2)
                    won=True




