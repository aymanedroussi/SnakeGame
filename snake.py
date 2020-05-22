
import pygame
from pygame.locals import *
import random


pygame.init()

class snake():
    def __init__(self,fenetre,green,x_position,y_position,x_snake,y_snake,w,h,A,List_snake):
        self.fenetre=fenetre
        self.green=green
        self.x_snake=x_snake
        self.y_snake=y_snake
        self.x_position=x_position
        self.y_position=y_position
        self.w=w
        self.h=h
        self.A=A
        self.List_snake=List_snake


        
    def afficher(self,x_position,y_position):
        if x_position<self.w and y_position<self.h:
            
            pygame.draw.rect(self.fenetre,self.green,[x_position,y_position,self.x_snake,self.y_snake])
            pygame.display.flip()

    




    

def cube(fenetre,red,x_cube,y_cube,x_snake,y_snake):
    pygame.draw.rect(fenetre,red,[x_cube,y_cube,x_snake,y_snake])
    pygame.display.flip()
    


def screen_text(fenetre,message,color_message,size,xtext_position,ytext_position):
    
    smallfont=pygame.font.SysFont(None,size)
    text=smallfont.render(message,True,color_message)
    fenetre.blit(text,[xtext_position,ytext_position])
    
    


def display(w,h,fenetre,black,white,x_snake,y_snake):
    fenetre.fill(black)
    row=h//(x_snake)
    y=0
    z=0
    
    for i in range(row+1):
        pygame.draw.line(fenetre,white,(0,y),(w,y))
        pygame.draw.line(fenetre,white,(z,0),(z,h))
        y+=(y_snake)
        z+=(x_snake)
    pygame.display.flip()



def main():
    global snake
    quit_game=1
    A=[]
    List_snake=[]
    w=320
    h=480
    black=(0,0,0)
    red=(255,0,0)
    white=(255,255,255)
    green=(0,255,0)
    snake_lengthen=1
    fenetre=pygame.display.set_mode((w,h))
    x_snake=20
    y_snake=20
    x_position=random.randrange(0,w,x_snake)
    y_position=random.randrange(0,h,y_snake)
    
    x_change=0
    y_change=0
    x_cube=random.randrange(0,w,x_snake)
    y_cube=random.randrange(0,h,y_snake)


    
    #home
    home=0
    while home==0:
        snake_home=pygame.image.load("snake_home.png").convert()
        fenetre.blit(snake_home,(0,0))
        screen_text(fenetre,"Press A to Play or Space To Quit !! ",white,20,50,300)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                        quit()
                    
                elif event.key==113:
                        
                    home=1
                    
                        
    
    display(w,h,fenetre,black,white,x_snake,y_snake)
    Snake=snake(fenetre,green,x_position,y_position,x_snake,y_snake,w,h,A,List_snake)
    Snake.afficher(x_position,y_position)
    cube(fenetre,red,x_cube,y_cube,x_snake,y_snake)
    direction=None
    continuer=0
    while continuer==0:
        pygame.time.Clock().tick(10)
       
        
        
        for event in pygame.event.get():
            if event.type==QUIT:
                quit()
                
                
                
            elif event.type==KEYDOWN:
                if event.key==K_UP and direction!="down":
                    direction="up"
                    x_change=0
                    y_change=-y_snake

                elif event.key==K_DOWN and direction!="up":
                    direction="down"
                    x_change=0
                    y_change=+y_snake

                elif event.key==K_RIGHT and direction!="left":
                    direction="right"
                    x_change=+x_snake
                    y_change=0
                    

                elif event.key==K_LEFT and direction !="right":
                    direction="left"
                    x_change=-x_snake
                    y_change=0

                elif direction=="right" and event.key==K_LEFT:
                    x_change=+x_snake
                    y_change=0

                elif direction=="left" and event.key==K_RIGHT:
                    x_change=-x_snake
                    y_change=0

                elif direction=="up" and event.key==K_DOWN:
                    x_change=0
                    y_change=-y_snake
                elif direction=="down" and event.key==K_UP:
                    x_change=0
                    y_change=+y_snake





                
        x_position+=x_change
        y_position+=y_change
        display(w,h,fenetre,black,white,x_snake,y_snake)
        
        cube(fenetre,red,x_cube,y_cube,x_snake,y_snake)

        if x_position>=w :
            
            x_position=0
        elif y_position>=h:
            y_position=0
        elif x_position<0:
            x_position=w
        elif y_position<0:
            y_position=h
            
            
        List_position=[]
        List_position.append(x_position)
        List_position.append(y_position)
       
        List_snake.append(List_position)
        if len(List_snake)>snake_lengthen:
            del List_snake[0]
        for xny in List_snake:
            Snake.afficher(xny[0],xny[1])




        #Score
        screen_text(fenetre,"Score : " + str(snake_lengthen -1),white,40,0,0)
        pygame.display.flip()

        
        for xny in List_snake[:-1]:
            if List_position==xny:
                fenetre.fill(white)
                screen_text(fenetre,"GAME OVER",black,30,100,200)
                screen_text(fenetre,"Press A to Go Home or Space To Quit ! ",red,20,60,240)
                screen_text(fenetre,"Score :" + str(snake_lengthen -1),green,30,80,260)
                pygame.display.flip()
                quit_game=0
                continuer=1
               
                break
        
          
       
        

        if x_position>=x_cube and x_position<x_cube+x_snake and y_position>=y_cube and y_position<y_cube+y_snake:
            x_cube=random.randrange(0,w,x_snake)
            y_cube=random.randrange(0,h,y_snake)
            snake_lengthen+=1
        
       

            
        while quit_game==0:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_SPACE:
                        quit()
                    
                    elif event.key==113:
                        
                        main()
                        
                        
                        
            
            
            
        
        
main()

