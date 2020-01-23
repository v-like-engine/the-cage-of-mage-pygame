import pygame

from camera_level_mask import CameraLevel
from core.classes.background_sprites import Decoration, Message
from core.classes.door_load import Door
from core.classes.effects import ScreenEffect
from core.levels.level1 import Level1


class PrologueLevel(CameraLevel):
    def __init__(self, width, height, mus, end=False):
        self.save('PrologueLevel')
        self.cam_coord = 640
        self.end_level = end
        if end:
            t = ['freedom.png', 'hall_right.jpg']
        else:
            t = ['hall.jpg']
        super().__init__(width, height, mus, False)
        self.tma_effect = pygame.sprite.Group()
        self.come_on = pygame.sprite.Group()
        self.get_in1 = pygame.sprite.Group()
        self.get_in2 = pygame.sprite.Group()
        self.get_in3 = pygame.sprite.Group()
        self.get_in4 = pygame.sprite.Group()
        self.faster1 = pygame.sprite.Group()
        self.faster2 = pygame.sprite.Group()
        self.faster3 = pygame.sprite.Group()
        self.move_btn = pygame.sprite.Group()
        self.jump_btn = pygame.sprite.Group()
        self.clear_gr = pygame.sprite.Group()
        mess_f1 = Message('messages/faster_white.png', 1000, 30, 320, 300, 60)
        mess_f1.add(self.faster1)
        mess_f2 = Message('messages/faster_light_red.png', 1000, 60, 320, 300, 60)
        mess_f2.add(self.faster2)
        mess_f3 = Message('messages/faster_red.png', 1000, 90, 320, 300, 60)
        mess_f3.add(self.faster3)
        comeon = Message('messages/come_on.png', 1010, 150, 320, 300, 60)
        comeon.add(self.come_on)
        getin1 = Message('messages/get_in.png', 1100 - 100, 180, 20, 300, 60)
        getin2 = Message('messages/get_in.png', 1000 - 100, 300, 70, 200, 40)
        getin3 = Message('messages/get_in.png', 980 - 100, 230, 330)
        getin4 = Message('messages/get_in.png', 1040 - 100, 10, 0, 480, 96)
        getin1.add(self.get_in1)
        getin2.add(self.get_in2)
        getin3.add(self.get_in3)
        getin4.add(self.get_in4)
        self.gets_ins = [self.clear_gr, self.get_in1, self.get_in2, self.get_in3, self.get_in4]
        self.angry_mess = [self.clear_gr, self.faster1, self.faster2, self.faster3, self.come_on]
        move_me = Message('messages/hold_arr_to_move.png', 440, 20)
        jump_me = Message('messages/hold_arr_to_jump.png', 440, 20)
        move_me.add(self.move_btn)
        jump_me.add(self.jump_btn)
        self.moving = False
        self.jumping = False
        self.j_mess = False
        self.m_mess = False
        self.angry = True
        self.get_in = False
        self.angry_num = 0
        self.num_get_in = 0
        self.main_doors = pygame.sprite.Group()
        coordoor = [-2030, -1876]
        door_bg = Decoration('door_frame_fat.png', coordoor[0], 380, 160, 320)
        door_bg.add(self.main_doors)
        self.door = Door(self.main_doors, self.screen, coordoor[1], 380)
        self.door.open()
        self.border_coord = 840
        self.ideal_border_coord = 840
        self.border_space = 120
        tma = ScreenEffect('tma.png', 0, 0)
        tma.add(self.tma_effect)
        self.door_closed = False
        self.ticks_until_level = 20
        self.end = False
        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()
            self.screen.fill(pygame.Color('#383636'))

            self.all_sprites.draw(self.screen)
            self.bottom_border.draw(self.screen)
            self.borders.draw(self.screen)
            self.backgrounds.draw(self.screen)
            self.decor.draw(self.screen)
            self.platforms.draw(self.screen)
            self.mage_group.draw(self.screen)
            self.main_doors.draw(self.screen)
            self.check_message()
            self.tma_effect.draw(self.screen)
            if self.m_mess:
                self.move_btn.draw(self.screen)
            elif self.j_mess:
                self.jump_btn.draw(self.screen)
            if self.angry:
                self.angry_mess[self.angry_num].draw(self.screen)
            if self.get_in:
                for el in self.gets_ins[:self.num_get_in]:
                    el.draw(self.screen)

            self.check_movement()
            self.check_movement()
            self.platforms.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            if self.ticks_until_level <= 0:
                New = Level1(self.width, self.height, pygame.mixer_music.get_pos())
                self.save('Level1')
                self.stop = True
            elif self.end:
                self.ticks_until_level -= 1
            self.render()
        self.terminate()

    def camera_update(self, x):
        if self.cam_coord + self.mage.width // 2 < self.border_coord or x > 0 or\
                self.border_coord < self.ideal_border_coord:
            if self.bg_frames[-1].rect.x + x > 50:
                x = 50 - self.bg_frames[-1].rect.x
            super().camera_update(x)
            if self.cam_coord <= -1940:
                self.end_of_the_prologue()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                New = PrologueLevel(self.width, self.height, pygame.mixer_music.get_pos())
                self.stop = True
            elif not self.end_level and event.key == pygame.K_UP and self.j_mess:
                self.jumping = True
                self.j_mess = False
            elif not self.end_level and event.key in [pygame.K_RIGHT, pygame.K_LEFT] and self.m_mess:
                self.moving = True
                self.m_mess = False

    def check_message(self):
        if self.FPS * 0.3 <= self.ticks <= self.FPS * 11 and not self.moving:
            self.m_mess = True
        if self.FPS * 2 < self.ticks and not self.jumping and self.moving:
            self.j_mess = True
        if self.ticks >= self.FPS * 4:
            if self.cam_coord > -1500:
                self.angry = True
            else:
                self.angry = False
                self.get_in = True
        self.angry_num = int((self.ticks // (self.FPS * 0.3)) % len(self.angry_mess))
        self.num_get_in = int((self.ticks // (self.FPS * 0.5)) % len(self.angry_mess))

    def check_movement(self):
        super().check_movement()

    def end_of_the_prologue(self):
        if not self.door_closed:
            self.door.open()
            self.door_closed = True
        self.border_coord = self.cam_coord + self.mage.width // 2
        self.ideal_border_coord = self.cam_coord + self.mage.width // 2
        self.border_space = 0
        self.mage.velocity_change(0, 0, 0)
        self.end = True
