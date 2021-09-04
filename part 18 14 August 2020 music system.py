# TODAY I MAKE SOME SNAKE GAME
# I AM MOVING MY SNAKE
# THIS IS THE FAVORITE PART

#Made food
#in this program i m using game over
# Today  IM USING high score
# I MUSING THE CHEAT CODE
import pygame
import random
import os
#music effects in background
pygame.mixer.init()


#import time
pygame.init()
# define colour
# rgb value 255
# it shows fill colour
red = (255, 0, 0)
black = (0, 0, 0)
white = (211, 211, 211)
blue = (135,206,235)

screen_width = 900
screen_height = 634
# create window
gamewindow = pygame.display.set_mode((screen_width,screen_height))
#background image
bgimg=pygame.image.load("baaaa.PNG")
bging=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
#by using convert alpha it making resize the screen
# title Shows
pygame.display.set_caption("Snake game")
pygame.display.update()
# clock Loop
clock = pygame.time.Clock()
# Show scoring
font = pygame.font.SysFont(None, 55)

def text_screen (text,color,x,y):
    screen_text=font.render(text,True,color)# anti aliging
    gamewindow.blit(screen_text,[x,y])

# Game loop
def plot_snake(gamewindow,color,snake_list,snake_size):
    #print(snake_list)
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])
#Welcome Screen
def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill(blue)
        text_screen("WELCOME TO SNAKES GAME", black, 180, 200)
        #a=text_screen("WELCOME TO SNAKES GAME",black,180,200)
        #text_screen("Press the enter button", black, 232, 150)
        #a=time.sleep(4)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(30)



def gameloop():
    # generate some food
    food_x = random.randint(15, screen_width / 2)
    food_y = random.randint(15, screen_height / 2)
    food_size = 20
    # snake lenght
    snake_list = []
    snake_lenght = 1
    # game specific variable
    exit_game = False
    game_over = False
    # define the coordiantes
    snake_x = 10
    snake_y = 10
    snake_size = 20
    # velocity
    init_velocity = 5
    # scroing the point
    # 0 is  used for initial value
    score = 0
    # fps is frame per second
    fps = 30
    # giving velocity of the snake
    velocity_x = 0
    velocity_y = 0
    #Check if high score file exist
    if not os.path.exists("high.txt"):
        with open("high.txt", "w") as f:
            f.write("0")


    with open("high.txt","r") as f:
        high = f.read()
    while not exit_game:
        #Part 2 ----Displaying the game over on screen
        if game_over:
            with open("high.txt","w") as f:
                f.write(str(high))
            gamewindow.fill(white)
            text_screen("Game Over!\nPlease Enter To Continue ",red,120,257)
            #it is used for exit screen
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                # it is used for re join the game by press enter key
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # snake_x=snake_x+10
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        # snake_x=snake_x-10
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        # snake_y=snake_y-10
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        # snake_y=snake_y+10
                        velocity_y = init_velocity
                        velocity_x = 0
                    # Cheat code
                    if event.key==pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            # it is used for food position and scoring
            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<6:
                score +=10
                #print("Score:", score)

                food_x = random.randint(10, screen_width / 2)
                food_y = random.randint(10, screen_height / 2)
                snake_lenght += 3
                #print(hiscore)
                if score>int(high):
                    high=score

            gamewindow.fill(white)
            gamewindow.blit(bgimg,(0,0))
            text_screen("Score:" + str(score)+" High Score:"+str(high),red,5,5)
            pygame.draw.rect(gamewindow, red, [snake_x, snake_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            #it shows coordiante
            if len(snake_list)>snake_lenght:
                del snake_list[0]
            #it is used for "head touch its body then game_over
            # in this :1 is 'all -1'
            if head in snake_list[:-1]:
                game_over=True


            #Part 1 :Display game over -----------
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                #print("Game Over")

            pygame.draw.rect(gamewindow, red, [food_x, food_y, food_size, food_size])
            plot_snake(gamewindow,black,snake_list,snake_size)
        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()
welcome()