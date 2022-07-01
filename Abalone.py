import pygame as pg
from Board import Board
import math
import random
import Colors
from Value import state_value
from Node import Node
import sys
from button import Button
import time
import pygame

pg.init()

# SOLO = False
LEVEL = 3
LEVEL_BOOL = False


# self.boardState = [[9,9,9,9,9,9],
#                           [9,2,2,2,2,2,9],
#                          [9,2,2,2,2,2,2,9],
#                         [9,0,0,2,2,2,0,0,9],
#                        [9,0,0,0,0,0,0,0,0,9],
#                       [9,0,0,0,0,0,0,0,0,0,9],
#                        [9,0,0,0,0,0,0,0,0,9],
#                         [9,0,0,1,1,1,0,0,9],
#                          [9,1,1,1,1,1,1,9],
#                           [9,1,1,1,1,1,9],
#                            [9,9,9,9,9,9]]



def ok(SOLO = False):

    global LEVEL, LEVEL_BOOL

    MAX, MIN = 10000, -10000

    size = (1440, 920)
    # size = (900, 900)

    board_center = (int(size[0]/2 - 250), int(size[1]/2))
    # board_center = (int(size[0]/2 ), int(size[1]/2))

    print("BOARD CENTER : ", board_center)

    # ball_r = 32
    ball_r = 32

    gap = ball_r/2
    dims = [ball_r, gap]
    board_lenght = 11*ball_r + 6*gap
    current_ball = 0
    white_turn = True


    print("BALL_RADIUS : ", ball_r)
    print("GAP : ", gap)
    print("DIMENSIONS : ", dims)
    print("BOARD LENGTH : ", board_lenght)

    screen = pg.display.set_mode(size)
    pg.display.set_caption("Abalone")

    ended = False
    clock = pg.time.Clock()

    # screen.fill(Colors.WHITE)
    screen.fill(Colors.BLACK)



    GOOD = True


    # time.sleep(5)

    board = Board(board_center, board_lenght, screen, dims)
    board.initialize()
    board.draw(current_ball)



    root = Node(board.boardState, [], 0, []) # grid, move, value, children


    while not ended:





        if white_turn:
            screen.fill(pygame.Color("black"))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            PLAY_NEW = Button(image=None, pos=(1200, 100), 
                                text_input="New Game", font=get_font(35), base_color="White", hovering_color="Green")
            PLAY_BACK = Button(image=None, pos=(1200, 200), 
                                text_input="BACK", font=get_font(35), base_color="White", hovering_color="Green")    
            PLAY_QUIT = Button(image=None, pos=(1200, 300), 
                                text_input="QUIT", font=get_font(35), base_color="White", hovering_color="Green")                      
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_NEW.changeColor(PLAY_MOUSE_POS)
            PLAY_QUIT.changeColor(PLAY_MOUSE_POS)

            PLAY_BACK.update(screen)
            PLAY_NEW.update(screen)
            PLAY_QUIT.update(screen)


            TXT = ""
            if LEVEL == 3:
                TXT += "GAME-LEVEL : EASY"
            else:
                TXT += "GAME-LEVEL : HARD"

            OPTIONS_TEXT = get_font(25).render(TXT, True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(1200, 600))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            PLAY_TURN = Button(image=None, pos=(1200, 700), 
                                text_input="TURN : WHITE", font=get_font(25), base_color="White", hovering_color="Green")  
            PLAY_TURN.update(screen)
            # pygame.display.update()

            pygame.draw.line(screen, "Gray", (950, 0), (950, 920))

            
            for event in pg.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_NEW.checkForInput(PLAY_MOUSE_POS):
                        ok(SOLO)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        # pg.quit()        
                        screen.fill(Colors.BLACK)
                        
                        main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_QUIT.checkForInput(PLAY_MOUSE_POS):
                        pg.quit()        


                if event.type == pg.QUIT:
                    ended = True

                if GOOD :
                    if event.type == pg.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos # get the mouse click position
                        for i in range(9):
                            for j in range(len(board.grid[i])):
                                if board.grid[i][j].collidepoint(mouse_pos): # dekhe je grid oi point e click hoise kina
                                    if current_ball == 0 and board.boardState[i+1][j+1] == 1:
                                        current_ball = [i, j] # position ta current_ball value te shift hoy
                                        print("CURRENT BALL VALUE : ", current_ball)
                                        break
                                    elif [i, j] == current_ball: 
                                        current_ball = 0 # move cancellation... mane select_position = curren_ball position hole move cancel
                                        break
                                    elif not board.boardState[i+1][j+1] == 2:
                                        result = board.check_move(current_ball, [i, j]) # check moves if any move need to do or any coin deleted(need more checking)
                                        # def check_move(self, coords1, coords2):
                                        if result[0]:
                                            board.make_move(result[2]) # Do the move and update if any point achieved
                                            white_turn = False
                                            current_ball = 0
                                            break
                                    else:
                                        print("YOU CAN'T MOVE BLACK")

        if not white_turn:
            screen.fill(pygame.Color("black"))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            PLAY_NEW = Button(image=None, pos=(1200, 100), 
                                text_input="New Game", font=get_font(35), base_color="White", hovering_color="Green")
            PLAY_BACK = Button(image=None, pos=(1200, 200), 
                                text_input="BACK", font=get_font(35), base_color="White", hovering_color="Green")    
            PLAY_QUIT = Button(image=None, pos=(1200, 300), 
                                text_input="QUIT", font=get_font(35), base_color="White", hovering_color="Green")                      
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_NEW.changeColor(PLAY_MOUSE_POS)
            PLAY_QUIT.changeColor(PLAY_MOUSE_POS)

            PLAY_BACK.update(screen)
            PLAY_NEW.update(screen)
            PLAY_QUIT.update(screen)


            TXT = ""
            if LEVEL == 3:
                TXT += "GAME-LEVEL : EASY"
            else:
                TXT += "GAME-LEVEL : HARD"

            OPTIONS_TEXT = get_font(25).render(TXT, True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(1200, 600))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            

            PLAY_TURN = Button(image=None, pos=(1200, 700), 
                                text_input="TURN : Black", font=get_font(25), base_color="White", hovering_color="Green")

            PLAY_TURN.update(screen)

            pygame.draw.line(screen, "Gray", (950, 0), (950, 920))
            
            

            if SOLO:
                board.draw(current_ball)
                pg.display.flip()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        ended = True

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_NEW.checkForInput(PLAY_MOUSE_POS):
                            ok(SOLO)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                            screen.fill(Colors.BLACK)
                            main_menu()                  
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_QUIT.checkForInput(PLAY_MOUSE_POS):
                            pg.quit()  

                    if GOOD:

                        if event.type == pg.MOUSEBUTTONDOWN:
                            mouse_pos = event.pos # get the mouse click position
                            for i in range(9):
                                for j in range(len(board.grid[i])):
                                    if board.grid[i][j].collidepoint(mouse_pos): # dekhe je grid oi point e click hoise kina
                                        if current_ball == 0 and board.boardState[i+1][j+1] == 2:
                                            current_ball = [i, j] # position ta current_ball value te shift hoy
                                            print("CURRENT BALL VALUE : ", current_ball)
                                            break
                                        elif [i, j] == current_ball: 
                                            current_ball = 0 # move cancellation... mane select_position = curren_ball position hole move cancel
                                            break
                                        elif not board.boardState[i+1][j+1] == 1:
                                            result = board.check_move(current_ball, [i, j]) # check moves if any move need to do or any coin deleted(need more checking)
                                            # def check_move(self, coords1, coords2):
                                            if result[0]:
                                                board.make_move(result[2]) # Do the move and update if any point achieved
                                                white_turn = True
                                                current_ball = 0
                                                break
                                        else:
                                            print("YOU CAN'T MOVE WHITE")

            else:
                if GOOD:
                    board.draw(current_ball)
                    pg.display.flip()
                    # new_move = board.minimax(3, root, False, float('-inf'),float('inf')).move
                    new_move = board.minimax(LEVEL, root, LEVEL_BOOL, float('-inf'),float('inf')).move

                    # new_move = board.minimax(4, root, True, float('-inf'),float('inf')).move
                    board.make_move(new_move)
                    root.grid = board.boardState
                    root.children = []
                    board.turn_counter += 1
                    white_turn = True

        if board.deleted == 1 or board.deleted == 2:
            board.deleted = 0
        if board.scorewhite == 6:
            print('White won!')
            OPTIONS_TEXT = get_font(40).render("WHITE WON!!!", True, "Green")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(1200, 450))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            # ended = True
            GOOD = False
        if board.scoreblack == 6:
            print('Black won!')
            OPTIONS_TEXT = get_font(40).render("BLACK WON!!!", True, "Green")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(1200, 450))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            # ended = True
            GOOD = False
        board.draw(current_ball)
        #board.generate_moves(board.boardState, 2)
        pg.display.flip()

        clock.tick(60)

# ok()

# SCREEN = pygame.display.set_mode((1280, 720))
SCREEN = pygame.display.set_mode((1440, 920))

pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
BG = pygame.transform.scale(BG, (1440,920))
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


  
def options():
    global LEVEL, LEVEL_BOOL

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(65).render("GAME-LEVEL", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(740, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        level_color = "#03fc1c"


        if LEVEL == 3:
            LEVEL_EASY = Button(image=None, pos=(600, 200), 
                                text_input="Easy", font=get_font(35), base_color=level_color, hovering_color="Green")
            LEVEL_HARD = Button(image=None, pos=(850, 200), 
                                text_input="Hard", font=get_font(35), base_color="Black", hovering_color="Green") 
        else:
            LEVEL_EASY = Button(image=None, pos=(600, 200), 
                            text_input="Easy", font=get_font(35), base_color="Black", hovering_color="Green")
            LEVEL_HARD = Button(image=None, pos=(850, 200), 
                            text_input="Hard", font=get_font(35), base_color=level_color, hovering_color="Green") 


        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        for button in [LEVEL_EASY, LEVEL_HARD, OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        # OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        # OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_EASY.checkForInput(OPTIONS_MOUSE_POS):
                    LEVEL = 3
                    LEVEL_BOOL = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_HARD.checkForInput(OPTIONS_MOUSE_POS):
                    LEVEL = 4
                    LEVEL_BOOL = True

        pygame.display.update()




def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(740, 200))

        kk = pygame.image.load("assets/Play Rect.png")
        kk = pygame.transform.scale(kk, (1250,150))

        color = "#03fce3"

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(740, 350), 
                            text_input="PLAY", font=get_font(75), base_color=color, hovering_color="White")
        PLAY_BUTTON_F = Button(image=kk, pos=(740, 500), 
                            text_input="PLAY WITH FRIEND", font=get_font(75), base_color=color, hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(740, 650), 
                            text_input="SETTINGS", font=get_font(75), base_color=color, hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(740, 800), 
                            text_input="QUIT", font=get_font(75), base_color=color, hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, PLAY_BUTTON_F, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ok()
                if PLAY_BUTTON_F.checkForInput(MENU_MOUSE_POS):
                    ok(SOLO = True)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()




pg.quit()
