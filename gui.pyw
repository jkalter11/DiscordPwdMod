## Import Internal modules
import pwd as pword ## Handles Password Functions
## Import External Modules
import pygame as pg
from pygame.locals import *
import csv
import os
import time
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (760, 465)
pg.init()
pg.font.init()
screen = pg.display.set_mode((400, 250), pg.NOFRAME)
pg.display.set_caption('Discord Login')
grey = 153,170,181

def setup():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 180)
    screen = pg.display.set_mode((1280, 720))
    pg.display.set_caption('Discord Setup')
    font = pg.font.SysFont('segoeuisymbol', 16)
    bogfont = pg.font.SysFont('segoeuisymbol', 18)
    bfont = pg.font.SysFont('microsoftjhengheimicrosoftjhengheiui', 32)
    sans = pg.font.Font('Uni-Sans-Thin.ttf', 18)
    bsans = pg.font.Font('UniSansHeavy.ttf', 12)
    clock = pg.time.Clock()
    screen.fill((44,47,51))
    input_box = pg.Rect(465, 100, 100, 30)
    pg.display.set_caption('Discord Login')
    color_inactive = pg.Color(153,170,181)
    color_active = pg.Color(103,170,181)
    color = color_inactive
    tcolor = 255,255,255
    active = False
    text = ''
    htext = ''
    done = False
    winbanner = pg.image.load('winbanner.PNG').convert()
    close = pg.image.load('close.PNG').convert()
    maxi = pg.image.load('maximize.PNG').convert()
    mini = pg.image.load('minimize.PNG').convert()
    closeN = pg.image.load('closeN.PNG').convert()
    welback = pg.image.load('welback.PNG').convert()
    logo = pg.image.load('disclogo.png').convert()
    correct = pg.image.load('pwdcorrect.png').convert()
    nextbtn = pg.image.load('next.PNG').convert()
    line = pg.Rect(465,125,350,1)
    nextbtnr = pg.Rect(700,140,114,31)
    pwdTrue = pword.pwd_unhash()
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                os._exit(0)
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = True
                else:
                    active = True
                    # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.MOUSEBUTTONDOWN:
                if nextbtnr.collidepoint(event.pos):
                    csv.writer(open('usersettings.csv', "w"), lineterminator='\n').writerows([["setup?", "1"],[r"discord_path", text]])
                    done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill((44,47,51))
        # Render the current text.
        txt_surface = font.render(text, True, (255,255,255))
        txt_surf = bsans.render('Please List the Path of your Discord.exe INCLUDING ARGUMENTS.', True, (255,255,255))
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(nextbtn, (700, 140))
        screen.blit(welback, (565,30))
        screen.blit(txt_surface, (input_box.x, input_box.y))
        screen.blit(txt_surf, (input_box.x, input_box.y-20))
        pg.draw.rect(screen, color, line, 2)
        pg.draw.rect(screen, color, nextbtnr, 2)
        pg.display.flip()
        clock.tick(30)
    done = False
    text = ""
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                os._exit(0)
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = True
                else:
                    active = True
                    # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.MOUSEBUTTONDOWN:
                if nextbtnr.collidepoint(event.pos):
                    pwd = pword.enAES256(text)
                    csv.writer(open("pwdInternal.csv", "w"), lineterminator='\n').writerows([[pwd[0], pwd[1]]])
                    os._exit(0)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill((44,47,51))
        # Render the current text.
        txt_surface = font.render(text, True, (255,255,255))
        txt_surf = bsans.render('Enter A Password. Remember This is Client Based and not Shared.', True, (255,255,255))
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(nextbtn, (700, 140))
        screen.blit(welback, (565,30))
        screen.blit(txt_surface, (input_box.x, input_box.y))
        screen.blit(txt_surf, (input_box.x, input_box.y-20))
        pg.draw.rect(screen, color, line, 2)
        pg.draw.rect(screen, color, nextbtnr, 2)
        pg.display.flip()
        clock.tick(30)


def readCSV():
    settings = []
    for line in csv.reader(open("usersettings.csv", "r"), delimiter=','):
        settings.append(line[1])
    return settings

def guiGetPwd():
    screen = pg.display.set_mode((400, 150), pg.NOFRAME)
    font = pg.font.SysFont('segoeuisymbol', 10)
    bogfont = pg.font.SysFont('segoeuisymbol', 18)
    bfont = pg.font.SysFont('microsoftjhengheimicrosoftjhengheiui', 32)
    sans = pg.font.Font('Uni-Sans-Thin.ttf', 18)
    bsans = pg.font.Font('UniSansHeavy.ttf', 12)
    clock = pg.time.Clock()
    input_box = pg.Rect(10, 100, 100, 30)
    pg.display.set_caption('Discord Login')
    color_inactive = pg.Color(153,170,181)
    color_active = pg.Color(153,170,181)
    color = color_inactive
    tcolor = 255,255,255
    active = False
    text = ''
    htext = ''
    done = False
    winbanner = pg.image.load('winbanner.PNG').convert()
    close = pg.image.load('close.PNG').convert()
    maxi = pg.image.load('maximize.PNG').convert()
    mini = pg.image.load('minimize.PNG').convert()
    closeN = pg.image.load('closeN.PNG').convert()
    welback = pg.image.load('welback.PNG').convert()
    logo = pg.image.load('disclogo.png').convert()
    correct = pg.image.load('pwdcorrect.png').convert()


    closeR = pg.Rect(373,0,27,21)
    maxiR = pg.Rect(345,0,28,21)
    miniR = pg.Rect(317,0,28,21)
    line = pg.Rect(10,125,350,1)
    pwdTrue = pword.pwd_unhash()
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = True
                else:
                    active = True
                    # Change the current color of the input box.
                color = color_active if active else color_inactive
                if closeR.collidepoint(event.pos):
                    os._exit(0)
                elif maxiR.collidepoint(event.pos):
                    pg.display.toggle_fullscreen()
                elif miniR.collidepoint(event.pos):
                    pg.display.iconify()
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        try:
                            if pwdTrue == text:
                                htext = 'Success!'
                                screen.fill((44,47,51))
                                # Render the current text.
                                txt_surface = bogfont.render(htext, True, (255,0,0))
                                width = max(200, txt_surface.get_width()+10)
                                input_box.w = width
                                txt_surf = bsans.render('Password:', True, (255,255,255))
                                screen.blit(txt_surf, (input_box.x, input_box.y-20))
                                screen.blit(welback, (125,30))
                                screen.blit(txt_surface, (input_box.x, input_box.y+9))
                                screen.blit(winbanner, (0,0))
                                screen.blit(close, (closeR.x, closeR.y))
                                screen.blit(maxi, (maxiR.x, maxiR.y))
                                screen.blit(mini, (miniR.x, miniR.y))
                                screen.blit(correct, (300,55))
                                pg.display.flip()
                                time.sleep(2)
                                return True
                            else:
                                htext = 'Password Incorrect. Please Try Agian...'.upper()
                                screen.fill((44,47,51))
                                # Render the current text.
                                txt_surface = bsans.render(htext, True, (255,0,0))
                                width = max(200, txt_surface.get_width()+10)
                                input_box.w = width
                                txt_surf = bsans.render('Password:', True, (255,255,255))
                                screen.blit(txt_surf, (input_box.x, input_box.y-20))
                                screen.blit(welback, (125,30))
                                screen.blit(txt_surface, (input_box.x, input_box.y+9))
                                screen.blit(winbanner, (0,0))
                                screen.blit(close, (closeR.x, closeR.y))
                                screen.blit(maxi, (maxiR.x, maxiR.y))
                                screen.blit(mini, (miniR.x, miniR.y))
                                pg.draw.rect(screen, color, line, 2)
                                pg.display.flip()
                                time.sleep(2)
                        except Exception:
                            pass
                        text = ''
                        htext = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                        htext = htext[:-1]
                    else:
                        text += event.unicode
                        htext += '●'

        screen.fill((44,47,51))
        # Render the current text.
        txt_surface = font.render(htext, True, tcolor)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        txt_surf = bsans.render('Password:', True, (255,255,255))
        screen.blit(welback, (125,30))
        screen.blit(txt_surface, (input_box.x, input_box.y+9))
        screen.blit(winbanner, (0,0))
        screen.blit(close, (closeR.x, closeR.y))
        screen.blit(maxi, (maxiR.x, maxiR.y))
        screen.blit(mini, (miniR.x, miniR.y))
        screen.blit(txt_surf, (input_box.x, input_box.y-20))
        pg.draw.rect(screen, color, line, 2)

        pg.display.flip()
        clock.tick(30)


while True:
    settings = readCSV()
    if settings[0] == '0':
        setup()
    elif settings[0] == '1':
        pwdInput = guiGetPwd()
    if pwdInput == True:
        path = "%r"%settings[1]
        path = path[1:-1]
        try:
            os.system(path)
        except Exception:
            print("Invalid Path")
    else:
        os._exit(0)
