import pygame as pg
from pygame.constants import KEYDOWN, KEYUP
import serial
import random
import sys
import time
from media import *
from sprites import *
from os import path
    
class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

        # Se a variável 'self.keyboard' for falsa, o jogo utilizará um arduino
        # caso contrário, o jogo pode ser jogado apenas com o teclado

        self.keyboard = True
        if not self.keyboard:
            self.ser = serial.Serial("COM5", 115200, timeout=0.01)
            self.FPS = 60
        self.FPS = 30

        self.load_data()
        self.projectiles = []
        self.itens = []
        self.holding = False
    
    # Carrega a pontuação máxima
    def load_data(self):
        self.dir = path.dirname(__file__)
        self.file_exist = 'r+' if path.isfile(path.join(self.dir, SCORE_FILE)) else 'w'
        with open(path.join(self.dir, SCORE_FILE), self.file_exist) as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def new_game(self):
        self.new_hs = False
        if self.keyboard:
            self.player = Player(330, 175, 5)
        else:
            self.player = Player(330, 175)
        
        self.projectile_timer = 0
        self.item_timer = 0

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            self.events()
            self.update_game_screen()

    def quit(self):
        pg.quit()
        sys.exit()

    def update_game_screen(self):
        self.screen.blit(BGIMAGE, [0, 0])
        self.screen.blit(hearts[0], [500, 15])
        # map_draw_group.draw(self.screen)
        self.player.update(self.screen)
        for projectile in self.projectiles:
            projectile.update(self.screen)
        for item in self.itens:
            item.update(self.screen)


        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            print(self.holding)
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEMOTION:
                self.x = pg.mouse.get_pos()[0]
                self.y = pg.mouse.get_pos()[1]

            if event.type == KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.start_time = time.time()
                    print(self.start_time)
            
            if event.type == KEYUP:
                if event.key == pg.K_SPACE:
                    self.elapsed_time = time.time() - self.start_time
                    if self.elapsed_time > 4:
                        self.holding = True
                # print(f"({self.x}, {self.y})")
                # print(self.hover_check(self.player.hitbox))

        if self.keyboard:
            self.check_keys()
        elif not self.keyboard:
            self.Arduino()
        # self.spawn_projectile()
        self.spawn_item()
        
        if self.player.life_cont == 0:
            self.playing = False


    def spawn_item(self):
        now = pg.time.get_ticks()
        if now - self.item_timer > ITEM_FREQ + random.choice([-500, 0, 500]):
            self.item_timer = now
            if len(self.itens) < MAX_NUM_ITEM:
                self.itens.append(Item())

        for item in self.itens:
            if item.hitbox[1] < self.player.hitbox[1] + self.player.hitbox[3] and item.hitbox[1] + item.hitbox[3] > self.player.hitbox[1]:
                if item.hitbox[0] + item.hitbox[2] > self.player.hitbox[0] and item.hitbox[0] < self.player.hitbox[0] + self.player.hitbox[2]:
                    if self.holding:
                        self.player.get_item()
                        self.itens.pop(self.itens.index(item))
                        self.holding = False

    def spawn_projectile(self):
        now = pg.time.get_ticks()
        if now - self.projectile_timer > PROJECTILE_FREQ + random.choice([-2000, -1000, -500, 0, 500, 1000, 2000]):
            self.projectile_timer = now
            if len(self.projectiles) < MAX_NUM_PROJECTILE:
                self.projectiles.append(Projectile())
        for projectile in self.projectiles:

                if projectile.hitbox[1] < self.player.hitbox[1] + self.player.hitbox[3] and projectile.hitbox[1] + projectile.hitbox[3] > self.player.hitbox[1]:
                    if projectile.hitbox[0] + projectile.hitbox[2] > self.player.hitbox[0] and projectile.hitbox[0] < self.player.hitbox[0] + self.player.hitbox[2]:
                        self.projectiles[self.projectiles.index(projectile)].hit()
                        self.player.hit()
                        self.projectiles.pop(self.projectiles.index(projectile))

                if projectile.x < WIDTH and projectile.x > 0:
                    if self.keyboard:
                        projectile.x += projectile.dx
                    if not self.keyboard:
                        projectile.x += 2*projectile.dx
                else:
                    self.projectiles.pop(self.projectiles.index(projectile))

    def hover_check(self,img):
        return img.rect.collidepoint(pg.mouse.get_pos())

    def check_keys(self):
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_a] and self.player.x > self.player.vel + 15:
            self.player.left = True
            self.player.right = False
            self.player.up = False
            self.player.down = False
            self.player.x -= self.player.vel

        elif self.keys[pg.K_d] and self.player.x + self.player.width < WIDTH - 80:
        # elif self.keys[pg.K_d] and self.player.x + self.player.width < WIDTH - 16:
            self.player.left = False
            self.player.right = True
            self.player.up = False
            self.player.down = False
            self.player.x += self.player.vel

        elif self.keys[pg.K_w] and self.player.y > self.player.vel + 15:
            self.player.left = False
            self.player.right = False
            self.player.up = True
            self.player.down = False
            self.player.y -= self.player.vel

        elif self.keys[pg.K_s] and self.player.y < HEIGHT - 86:
            self.player.left = False
            self.player.right = False
            self.player.up = False
            self.player.down = True
            self.player.y += self.player.vel

        else:
            self.player.left = False
            self.player.right = False
            self.player.up = False
            self.player.down = False
            self.player.walk_count = 0
        # print(self.player.x, self.player.y)

    def Arduino(self):
        self.serial = self.ser.readline()
        self.serial_conv = self.serial.decode()
        self.command = self.serial_conv[0:3]
        if self.command == "ESQ" and self.player.x > self.player.vel + 15:
            self.player.left = True
            self.player.right = False
            self.player.up = False
            self.player.down = False
            self.player.x -= self.player.vel
        elif self.command == "DIR" and self.player.x + self.player.width < WIDTH - 96:
            self.player.left = False
            self.player.right = True
            self.player.up = False
            self.player.down = False
            self.player.x += self.player.vel
        elif self.command == "CIM" and self.player.y > self.player.vel + 15:
            self.player.left = False
            self.player.right = False
            self.player.up = True
            self.player.down = False
            self.player.y -= self.player.vel
        elif self.command == "BAI" and self.player.y < HEIGHT - 70:
            self.player.left = False
            self.player.right = False
            self.player.up = False
            self.player.down = True
            self.player.y += self.player.vel
        elif self.command == "lll":
        # else:
            self.player.left = False
            self.player.right = False
            self.player.up = False
            self.player.down = False
            self.player.walk_count = 0
    
    def main_menu(self):
        self.jacquin1 = (380, 294, 60, 106)
        self.jacquin2 = (312, 360, 68, 40)
        self.jacquin3 = (470, 216, 80, 134)
        self.jacquin4 = (441, 350, 138, 50)
        self.jacquin5 = (580, 294, 60, 106)
        self.jacquin6 = (640, 360, 68, 40)
        pg.mixer.music.play()
        self.menu_loop = True
        while self.menu_loop:
            screen.blit(BGMENU,[0, 0])

            mm_draw_group1.draw(screen)

            if self.hover_check(start_btn1):
                mm_start.draw(screen)
            elif self.hover_check(option_btn1):
                mm_option.draw(screen)
            elif self.hover_check(inst_btn1):
                mm_inst.draw(screen)
            elif self.hover_check(exit_btn1):
                mm_quit.draw(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                elif event.type == pg.MOUSEMOTION:
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]
                    # print(x, y)
                elif (event.type == pg.MOUSEBUTTONDOWN):
                    # Start
                    if x >= 60 and x <= 260 and y >= 80 and y <= 130:
                        click_snd.play()
                        screen.blit(start_btn3,[60, 80])
                        pg.display.update()
                        pg.time.wait(400)
                        screen.fill(BLACK)
                        door_snd.play()
                        pg.display.update()
                        pg.time.wait(3000)
                        self.menu_loop = False
                    
                    # Options
                    elif x >= 60 and x <= 260 and y >= 140 and y <= 190:
                        click_snd.play()
                        screen.blit(option_btn3,[60, 140])
                        pg.display.update()
                        pg.time.wait(400)
                        self.option_screen()
                    
                    # Instructions
                    elif x >= 60 and x <= 260 and y >= 200 and y <= 250:
                        click_snd.play()
                        screen.blit(inst_btn3,[60, 200])
                        pg.display.update()
                        pg.time.wait(400)
                        self.instruction_screen()

                    # Quit
                    elif x >= 60 and x <= 260 and y >= 260 and y <= 310:
                        click_snd.play()
                        screen.blit(exit_btn3,[60, 260])
                        pg.display.update()
                        pg.time.wait(400)
                        self.quit()
                    
                    elif x >= 380 and x <= 440 and y >= 60 and y <= 400 or x >= 312 and x <= 380 and y >= 360 and y <= 400:
                        cala_snd.stop()
                        cala_snd.play()

                    elif x >= 441 and x <= 579 and y >= 350 and y <= 400 or x >= 470 and x <= 550 and y >= 216 and y <= 350:
                        profission_snd.stop()
                        profission_snd.play()
                    
                    elif x >= 580 and x <= 640 and y >= 294 and y <= 400 or x >= 640 and x <= 708 and y >= 360 and y <= 400:
                        cala_snd.stop()
                        cala_snd.play()

            pg.display.update()

    def instruction_screen(self):
        self.instrucao = True
        while self.instrucao:
            screen.fill(WHITE)
            inst_draw_group.draw(screen)
            close_draw_group.draw(screen)

            if (self.hover_check(close_btn1)):
                close_hover.draw(screen)

            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    self.quit()
                elif (event.type == pg.MOUSEBUTTONDOWN):
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]
                    if (x >= 670 and x <= 720 and y >= 17 and y <= 67):
                        click_snd.play()
                        pg.time.wait(400)
                        self.instrucao = False
            
            pg.display.update()

    def option_screen(self):
        self.vol = 0.5
        self.vol_msc = 0.05
        self.options = True
        self.snd_state = 1

        while self.options:
            screen.fill(WHITE)
            option_draw_group.draw(screen)
            close_draw_group.draw(screen)
            # print(self.snd_state,self.vol, self.vol_msc)

            if self.hover_check(close_btn1):
                close_hover.draw(screen)
            if self.hover_check(snd_add):
                snd_add_hover.draw(screen)
            if self.hover_check(snd_minus):
                snd_minus_hover.draw(screen)
            if self.snd_state == 1:
                snd_on_button.draw(screen)
                if self.hover_check(snd_on):
                    snd_on_hover.draw(screen)
            if self.snd_state == 0:
                snd_off_button.draw(screen)
                if self.hover_check(snd_mute):
                    snd_off_hover.draw(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.MOUSEMOTION:
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]
                    # print(x, y)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]
                    # Quit
                    if (x >= 670 and x <= 720 and y >= 17 and y <= 67):
                        click_snd.play()
                        pg.time.wait(400)
                        self.options = False

                    # Minus
                    elif (x >= (WIDTH/2)-125 and x <= (WIDTH/2)-75 and y >= (HEIGHT/2) and y <= (HEIGHT/2)+50):
                        click_snd.play()
                        screen.blit(snd_minus_c, [(WIDTH/2)-125, (HEIGHT/2)])
                        pg.display.update()
                        pg.time.wait(200)
                        if self.vol > 0 and self.vol_msc > 0:
                            self.vol -= 0.1
                            self.vol_msc -= 0.01
                            click_snd.set_volume(self.vol)
                            pg.mixer.music.set_volume(self.vol_msc)
                            hit_snd[0].set_volume(self.vol)
                            hit_snd[1].set_volume(self.vol)
                            item_snd.set_volume(self.vol)
                            if self.vol <= 0.1 and self.vol_msc <= 0.01:
                                self.snd_state = 0
                    
                    # Plus
                    elif (x >= (WIDTH/2)+75 and x <= (WIDTH/2)+125 and y >= (HEIGHT/2) and y <= (HEIGHT/2)+50):
                        click_snd.play()
                        screen.blit(snd_add_c, [(WIDTH/2)+75, (HEIGHT/2)])
                        pg.display.update()
                        pg.time.wait(200)
                        self.vol += 0.1
                        self.vol_msc += 0.01
                        click_snd.set_volume(self.vol)
                        pg.mixer.music.set_volume(self.vol_msc)
                        hit_snd[0].set_volume(self.vol)
                        hit_snd[1].set_volume(self.vol)
                        item_snd.set_volume(self.vol)
                        if self.vol > 0 and self.vol_msc > 0:
                            self.snd_state = 1

                    # On
                    elif self.snd_state == 1:
                        if (x >= (WIDTH/2)-25 and x <= (WIDTH/2)+25 and y >= (HEIGHT/2) and y <= (HEIGHT/2)+50):
                            click_snd.play()
                            screen.blit(snd_on_c, [(WIDTH/2)-25, (HEIGHT/2)])
                            pg.display.update()
                            pg.time.wait(200)
                            self.vol = 0
                            self.vol_msc = 0
                            click_snd.set_volume(self.vol)
                            pg.mixer.music.set_volume(self.vol_msc)
                            hit_snd[0].set_volume(self.vol)
                            hit_snd[1].set_volume(self.vol)
                            item_snd.set_volume(self.vol)
                            self.snd_state = 0

                    # Off
                    elif self.snd_state == 0:
                        if (x >= (WIDTH/2)-25 and x <= (WIDTH/2)+25 and y >= (HEIGHT/2) and y <= (HEIGHT/2)+50):
                            click_snd.play()
                            screen.blit(snd_mute_c, [(WIDTH/2)-25, (HEIGHT/2)])
                            pg.display.update()
                            pg.time.wait(200)
                            self.vol = 0.5
                            self.vol_msc = 0.05
                            click_snd.set_volume(self.vol)
                            pg.mixer.music.set_volume(self.vol_msc)
                            hit_snd[0].set_volume(self.vol)
                            hit_snd[1].set_volume(self.vol)
                            item_snd.set_volume(self.vol)
                            self.snd_state = 1

            pg.display.update()

    def go_screen(self):
        self.score_font = pg.font.SysFont("Segoe UI Black", 28)
        pg.mixer.music.stop()
        screen.fill(BLACK)
        fall_snd.play()
        pg.display.flip()
        pg.time.wait(2000)
        ds3_snd.play()
        screen.blit(GOIMAGE, [0, 0])
        screen.blit(enemy_idle_go, [345, 250])
        pg.display.flip()
        pg.time.wait(4000)
        
        self.go = True
        while self.go:
            # screen.blit(HSIMAGE, [0, 0])
            screen.fill(BLACK)

            if self.player.score_cont > self.highscore:
                self.highscore = self.player.score_cont
                self.new_highscore_text = self.score_font.render(F"NEW HIGH SCORE!", True, WHITE)
                self.new_hs = True
                with open(path.join(self.dir, SCORE_FILE), "w") as f:
                    f.write(str(self.player.score_cont))
            if self.new_hs:
                screen.blit(self.new_highscore_text, [250, 150])
            self.last_score_text = self.score_font.render(f"Score: {self.player.score_cont}", True, WHITE)
            self.highscore_text = self.score_font.render(f"High Score: {self.highscore}", True, WHITE)
            screen.blit(self.last_score_text, [310, 30])
            screen.blit(self.highscore_text, [280, 90])
            
            go_draw_group.draw(screen)


            if self.hover_check(quit_btn1):
                screen.blit(enemy_right_go, [340, 250])
                go_quit.draw(screen)
            elif self.hover_check(retry_btn1):
                screen.blit(enemy_left_go, [360, 250])
                go_retry.draw(screen)
            # if not self.hover_check(quit_btn1) and not self.hover_check(retry_btn1):
            else:
                screen.blit(enemy_idle_go, [345, 250])

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()

                elif event.type == pg.MOUSEMOTION:
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]
                    # print(x, y)

                elif (event.type == pg.MOUSEBUTTONDOWN):
                    if x >= 80 and x <= 280 and y >= 260 and y <= 310:
                        ds3_snd.stop()
                        click_snd.play()
                        screen.blit(retry_btn3,[80, 260])
                        pg.display.update()
                        pg.time.wait(400)
                        self.go = False

                    elif x >= 480 and x <= 680 and y >= 260 and y <= 310:
                        click_snd.play()
                        screen.blit(quit_btn3,[480, 260])
                        pg.display.update()
                        pg.time.wait(400)
                        self.quit()
            
            pg.display.update()
        

g = Game()
while True:
    g.main_menu()
    g.new_game()
    g.run()
    g.go_screen()
