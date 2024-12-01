#!/usr/bin/env python
# coding=utf-8
import pygame
import time
from pygame.locals import *
from sys import exit
#Read Image Unit
pygame.init()
Game_Screen = pygame.display.set_mode((800,800),0,32)
Image_Help = pygame.image.load("source/help.png").convert()
Image_Box_Inplace = pygame.image.load("source/box_yes.png").convert()
Image_Box_Outplace = pygame.image.load("source/box_no.png").convert()
Game_Success = pygame.image.load("source/Success.jpg").convert()
Image_Player = pygame.image.load("source/player.png").convert()
Image_Goal = pygame.image.load("source/power.png").convert()
Image_Wall = pygame.image.load("source/wall.png").convert()
Image_Help = pygame.transform.scale(Image_Help,(800,800))
Image_Box_Inplace = pygame.transform.scale(Image_Box_Inplace,(64,64))
Image_Box_Outplace = pygame.transform.scale(Image_Box_Outplace,(64,64))
Image_Player = pygame.transform.scale(Image_Player,(64,64))
Image_Wall= pygame.transform.scale(Image_Wall,(64,64))
Image_Goal = pygame.transform.scale(Image_Goal,(64,64))

#Debug Map
def Debug_Map(alist):
    for i in alist:
        print( i)
#Debug Map Done


#Global Vara
Game_font = pygame.font.SysFont("arial",32)
Game_Map_Source = []
Game_Step = 0
Player_Pos=[0,0]
Game_Level = 1
Game_Map = []
Map_Wide = 0
Map_Deepth = 0
Game_Path = []
Dir = ((-1,0),(1,0),(0,-1),(0,1))

#Global Var Done

#Read Map Unit
def Map_Reader(Mission):
    global Game_Map
    global Map_Deepth
    global Map_Wide
    File_Name ="map/"+ str(Mission) +'.dat'
    file = open(File_Name,'r')
    Map_Deepth,Map_Wide = map(int,file.readline().split())
    for i in range(Map_Deepth):
        Game_Map.append(file.readline()[:Map_Wide])
    file.close()
#Read Map Unit Done

#Undo Unit
def Undo():
    global Game_Screen
    global Game_Map
    global Game_Path
    if Game_Path:
        Game_Map = Game_Path[-1][:]
        del Game_Path[-1]
        print( Game_Map)
        Display_refresh(Game_Screen)
    else:
        print( "You can't forback")
#Undo Unit Done

#Redo Unit
def Redo():
    global Game_Map_Source
    global Game_Map
    global Game_Screen
    Game_Map = Game_Map_Source[:]
    Display_refresh(Game_Screen)

#Map P = Player W = Wall B = Box G=Goal A=achieve N = Way or NULL

#Draw Map Unit
def Display_refresh(Game_Screen):
    global Game_Level
    global Game_Step
    global Game_Map
    global Map_Deepth
    global Map_Wide
    global Player_Pos
    Game_Screen.fill((255,255,255))
    for i in range(Map_Deepth):
        for j in range(Map_Wide):
            pos = [j*64,i*64]
            if Game_Map[i][j]=='P':
                Game_Screen.blit(Image_Player,pos)
                Player_Pos[0]=i
                Player_Pos[1]=j
            elif  Game_Map[i][j]=='W':
                Game_Screen.blit(Image_Wall,pos)
            elif  Game_Map[i][j]=='B':
                Game_Screen.blit(Image_Box_Outplace,pos)
            elif  Game_Map[i][j]=='A':
                Game_Screen.blit(Image_Box_Inplace,pos)
            elif  Game_Map[i][j]=='G':
                Game_Screen.blit(Image_Goal,pos)
    pygame.display.set_caption("Mission "+str(Game_Level))
    #Game_Screen.blit(Game_font.render("space to redo",True,(0,0,0)),(0,Map_Deepth*64-32)) 
    pygame.display.update()
#Draw Map Unit Done

#Check Unit
def Check_Win():
    num = 0
    global Game_Map
    global Map_Wide
    global Map_Deepth
    for i in range(Map_Deepth):
        for j in range(Map_Wide):
            if Game_Map[i][j]=='B':
                return False
    return True
#Check Win Unit 

#Defult Unit
def Defult():
    global Game_Map
    global Game_Level
    global Map_Wide
    global Map_Deepth
    global Game_Path
    global Game_Map_Source
    global Player_Pos
    Game_Path = []
    Game_Map = []
    Map_Reader(Game_Level)
    Game_Map_Source = Game_Map[:]
    pygame.display.set_caption("Mission %s   Step %s" % (str(Game_Level),str(Game_Step)))
    pygame.display.update()
    return pygame.display.set_mode((Map_Wide*64,Map_Deepth*64),0,32)
#Defult Unit Done

#Map Change Unit
def Change_Map(x,y,object):
    global Game_Map
    Game_Map[x] = Game_Map[x][:y]+object+Game_Map[x][y+1:]
#Map Change Done

#Move Unit
def Move(dir):
    global Game_Screen
    global Game_Map
    global Player_Pos
    global Game_Step
    global Game_Path
    global Game_Map_Source
    global Map_Wide
    global Map_Deepth
    Player_Stand = Game_Map[Player_Pos[0]][Player_Pos[1]]
    Temp_x = Player_Pos[0] + Dir[dir][0]
    Temp_y = Player_Pos[1] + Dir[dir][1]
    print( Temp_x,Temp_y)
    print( Game_Map[Temp_x][Temp_y])
    #If there is a Box
    if Game_Map[Temp_x][Temp_y] in ('A','B'):
        print( "there is a box")
        if Game_Map[Temp_x+Dir[dir][0]][Temp_y+Dir[dir][1]] in ('N','G'):
            #Move Box 
            Game_Path.append(Game_Map[:])
            if Game_Map[Temp_x+Dir[dir][0]][Temp_y+Dir[dir][1]]=='G':
                Change_Map(Temp_x+Dir[dir][0],Temp_y+Dir[dir][1],'A')
            else:
                Change_Map(Temp_x+Dir[dir][0],Temp_y+Dir[dir][1],'B')
            #Debug_Map(Game_Map) 
            #print( Game_Map)
            #Change Box to Play
            Change_Map(Temp_x,Temp_y,'P')
            #print( Game_Map)
            #Debug_Map(Game_Map) 
            #Change Player to what he use to stand;
            if Game_Map_Source[Player_Pos[0]][Player_Pos[1]]=='G':
                Change_Map(Player_Pos[0],Player_Pos[1],"G")
            else:
                Change_Map(Player_Pos[0],Player_Pos[1],"N")
            #print( Game_Map)
            #Update Player_Pos
            #Debug_Map(Game_Map) 
            Player_Pos[0] = Temp_x
            Player_Pos[1] = Temp_y
            #print( Game_Map)
            #Debug_Map(Game_Map) 
            Display_refresh(Game_Screen)
            return
    #if there is nothing
    if Game_Map[Temp_x][Temp_y] in ("N","G"):
        print( "do it")
        Change_Map(Temp_x,Temp_y,'P')
        if Game_Map_Source[Player_Pos[0]][Player_Pos[1]]=='G':
            Change_Map(Player_Pos[0],Player_Pos[1],"G")
        else:
            Change_Map(Player_Pos[0],Player_Pos[1],"N")
        Player_Pos[0] = Temp_x
        Player_Pos[1] = Temp_y
    #else do nothing
    Display_refresh(Game_Screen)

# Function to create the start menu
def start_menu():
    global Game_Screen
    button_width = 200
    button_height = 50
    play_button = pygame.Rect(300, 250, button_width, button_height)  # Centered
    help_button = pygame.Rect(300, 320, button_width, button_height)  # Centered
    quit_button = pygame.Rect(300, 390, button_width, button_height)  # Centered

    while True:
        Game_Screen.fill((255, 255, 255))  # Clear the screen
        pygame.draw.rect(Game_Screen, (0, 0, 0), play_button)  # Draw Play button
        pygame.draw.rect(Game_Screen, (0, 0, 0), help_button)  # Draw Help button
        pygame.draw.rect(Game_Screen, (0, 0, 0), quit_button)  # Draw Quit button

        play_label = Game_font.render('Play Game', True, (255, 255, 255))
        help_label = Game_font.render('Help', True, (255, 255, 255))
        quit_label = Game_font.render('Quit', True, (255, 255, 255))

        Game_Screen.blit(play_label, (play_button.x + (play_button.width / 2 - play_label.get_width() / 2), 
                                       play_button.y + (play_button.height / 2 - play_label.get_height() / 2)))
        Game_Screen.blit(help_label, (help_button.x + (help_button.width / 2 - help_label.get_width() / 2), 
                                       help_button.y + (help_button.height / 2 - help_label.get_height() / 2)))
        Game_Screen.blit(quit_label, (quit_button.x + (quit_button.width / 2 - quit_label.get_width() / 2), 
                                       quit_button.y + (quit_button.height / 2 - quit_label.get_height() / 2)))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return  # Start the game
                if help_button.collidepoint(event.pos):
                    # Display help (you can implement this)
                    print("Help section not implemented yet.")
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

# Main execution
if __name__ == "__main__":
    start_menu()  # Call the start menu instead of displaying the welcome screen
    Game_Screen = Defult()
    Display_refresh(Game_Screen)
    print( Player_Pos)
    print( Game_Map)
    while True:
        for event in pygame.event.get():
            if event.type  ==KEYDOWN:
                if event.key == K_w:
                    Move(0)
                elif event.key == K_s:
                    Move(1)
                elif event.key == K_a:
                    Move(2)
                elif event.key == K_d:
                    Move(3)
                elif event.key == K_q:
                    Undo()
                elif event.key == K_e:
                    Redo()
                elif event.key == 27:
                    pygame.display.quit()
                    exit()
            elif event.type == QUIT:
                pygame.display.quit()
                exit()
        if (Check_Win()):
            print( "you win")
            time.sleep(1)
            if Game_Level < 3:
                Game_Level += 1
                Defult()
                Display_refresh(Game_Screen)
            else:
                Game_Screen = pygame.display.set_mode((572,416),0,32)
                Game_Screen.blit(Game_Success,(0,0))
                pygame.display.update()
                time.sleep(5)
                pygame.display.quit()
                exit()
