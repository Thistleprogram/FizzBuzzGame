#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys
import button
import time
import os

SCR_RECT=pygame.Rect(0,0,960,720)

aqua0 = (153, 217, 234)
aqua1 = (121, 206, 227)
aqua2 = (102, 199, 223)

def button_from_text(text, color_n, color_a, color_o, font_size, rect, text_size):
    sysfont = pygame.font.SysFont(None, font_size)
    s = sysfont.render(text, True, (0,0,0))
    normal = pygame.Surface(rect.size)
    normal.fill(color_n)
    normal.blit(s, text_size)
    above = pygame.Surface(rect.size)
    above.fill(color_a)
    above.blit(s, text_size)
    onclick = pygame.Surface(rect.size)
    onclick.fill(color_o)
    onclick.blit(s, text_size)
    return button.Button(normal, above, onclick, rect)

def main():
    pygame.init()
    screen=pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption("FizzBuzzGame")
    
    SceneName="TitleScene"
    
    clock = pygame.time.Clock()
    
    #Title Scene
    sysfont = pygame.font.SysFont(None, 130)
    title = sysfont.render("FizzBuzzGame", True, (0,0,0))
    goto_play = button_from_text("Play Game!!", aqua0, aqua1, aqua2, 80, pygame.Rect(160, 400, 640, 100), (170, 25))
    goto_rules = button_from_text("Watch Rules!!", aqua0, aqua1, aqua2, 80, pygame.Rect(160, 550, 640, 100), (140, 25))
    sysfont = pygame.font.SysFont(None, 40)
    lisence = sysfont.render("Made by Thistle", True, (0,0,0))
    
    #Play Scene
    sysfont = pygame.font.SysFont(None, 300)
    num = 0
    number = "0"
    shownum = sysfont.render("0", True, (0,0,0))
    
    timefont = pygame.font.SysFont(None, 120)
    showtime = timefont.render("1", True, (0,0,0))
    
    fizz_button = button_from_text("Fizz", aqua0, aqua1, aqua2, 80, pygame.Rect(80, 480, 240, 100), (65,25))
    buzz_button = button_from_text("Buzz", aqua0, aqua1, aqua2, 80, pygame.Rect(360, 480, 240, 100), (50,25))
    num_button = button_from_text("10", aqua0, aqua1, aqua2, 80, pygame.Rect(640, 480, 240, 100), (80,25))
    fizzbuzz_button = button_from_text("FizzBuzz", aqua0, aqua1, aqua2, 80, pygame.Rect(290, 600, 400, 100), (65, 25))
    quit_button = button_from_text("Quit Game", (255,0,0), (235,0,0), (215,0,0), 30, pygame.Rect(670,40,300,40), (10,10))
    
    #Result Scene
    plus = 0
    titlefont = pygame.font.SysFont(None, 100)
    result_title = titlefont.render("Result", True, (0,0,0))
    scorefont = pygame.font.SysFont(None, 70)
    Time = scorefont.render("10", True, (0,0,0))
    WA = scorefont.render("10", True, (0,0,0))
    score = scorefont.render("10", True, (0,0,0))
    base = os.path.dirname(os.path.abspath(__file__))
    name = os.path.normpath(os.path.join(base, 'text.txt'))
    with open(name) as f:
        list = [float(s.strip()) for s in f.readlines()]
    ranknames = ["1st", "2nd", "3rd", "4th", "5th", "6th",]
    
    #Watch Scene
    back_button = button_from_text("Back to Title", (255,0,0), (235,0,0), (215,0,0), 30, pygame.Rect(670,40,300,40), (10,10))
    base = os.path.dirname(os.path.abspath(__file__))
    name = os.path.normpath(os.path.join(base, 'rule.png'))
    rule = pygame.image.load(name).convert()
    
    while True:
        clock.tick(60)
        screen.fill((255,255,255))
        
        #event run
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if SceneName == "PlayScene":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x,y = event.pos
                    if fizz_button.contains(x,y):
                        if num%3==0 and num%5!=0:
                            num+=1
                        else: 
                            plus+=5
                    if buzz_button.contains(x,y):
                        if num%3!=0 and num%5==0:
                            num+=1
                        else:
                            plus+=5
                    if num_button.contains(x,y):
                        if num%3!=0 and num%5!=0:
                            num+=1
                        else:
                            plus+=5
                    if fizzbuzz_button.contains(x,y):
                        if num%3==0 and num%5==0:
                            num+=1
                        else:
                            plus+=5
                    if quit_button.contains(x,y):
                        pygame.quit()
                        sys.exit()
            if SceneName == "TitleScene":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x,y = event.pos
                    if goto_play.contains(x,y):
                        SceneName = "PlayScene"
                        t1=time.time()
                    if goto_rules.contains(x,y):
                        SceneName = "WatchScene"
            if SceneName == "WatchScene":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x,y=event.pos
                    if back_button.contains(x,y):
                        SceneName = "TitleScene"
            if SceneName == "ResultScene":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x,y=event.pos
                    if quit_button.contains(x,y):
                        pygame.quit()
                        sys.exit()
                            
        #foreach scenes
        if SceneName == "TitleScene":
            screen.blit(title, (150,160))
            goto_play.update()
            goto_rules.update()
            goto_play.draw(screen)
            goto_rules.draw(screen)
            screen.blit(lisence, (700, 290))
            
            
        elif SceneName == "PlayScene":
            
            quit_button.update()
            quit_button.draw(screen)
            number = str(num)
            
            shownum = sysfont.render(number, True, (0,0,0))
            screen.blit(shownum, (480-len(number)*60, 150))
            num_button = button_from_text(number, aqua0, aqua1, aqua2, 80, pygame.Rect(640, 480, 240, 100), (125-len(number)*17,25))
            
            fizz_button.update()
            buzz_button.update()
            num_button.update()
            fizzbuzz_button.update()
            
            fizz_button.draw(screen)
            buzz_button.draw(screen)
            num_button.draw(screen)
            fizzbuzz_button.draw(screen)
            
            t2 = time.time()
            showtime = timefont.render(str(round(t2-t1, 4)), True, (0,0,0))
            screen.blit(showtime, (590, 100))
            if num == 50:
                Time = scorefont.render("Time : "+str(round(t2-t1, 4)), True, (0,0,0))
                WA = scorefont.render("Uncorrect : "+str(round(plus/5)), True, (0,0,0))
                score = scorefont.render("Score : "+str((round(t2-t1, 4))+plus), True, (0,0,0))
                list.append(round((t2-t1), 4)+plus)
                list.sort()
                stlist = []
                for i in range(6):
                    stlist.append(str(list[i]))
                base = os.path.dirname(os.path.abspath(__file__))
                name = os.path.normpath(os.path.join(base, 'text.txt'))
                with open(name, mode="w") as f:
                    f.write('\n'.join(stlist))
                SceneName = "ResultScene"
            
        elif SceneName == "ResultScene":
            quit_button.update()
            quit_button.draw(screen)
            screen.blit(result_title, (60, 45))
            screen.blit(Time, (120, 150))
            screen.blit(WA, (120, 200))
            screen.blit(score, (120, 250))
            scores = [scorefont.render((str(list[i]) if list[i]!=10000 else "None"), True, (0,0,0)) for i in range(6)]
            ranks = [scorefont.render(ranknames[i], True, (0,0,0)) for i in range(6)]
            for i in range(3):
                screen.blit(ranks[i], (100, 350+i*70))
                screen.blit(scores[i], (200, 350+i*70))
            for i in range(3):
                screen.blit(ranks[i+3], (550, 350+i*70))
                screen.blit(scores[i+3], (650, 350+i*70))
                
        else:
            screen.blit(rule, (0,0))
            back_button.update()
            back_button.draw(screen)
            
        pygame.display.update()
                
if __name__ == "__main__":
    main()
