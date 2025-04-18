import pygame
import random
from entity.Entity import Entity

class Sparc(Entity):
    def __init__(self, x, y, prev, next):
        super().__init__(x, y, prev, next)
        if random.random() < 0.5:
            self.direction = "right"
        else:
            self.direction = "left"
        self.horizontal = True
        self.sprite = pygame.image.load("./entity/assets/sparx.png")
        self.sparcSurface = pygame.Surface((32, 32))

    def draw(self, screen):
        self.sparcSurface.blit(self.sprite, (0, 0))
        #Sparc Mask
        sparc_mask = pygame.mask.from_surface(self.sparcSurface)
        screen.blit(self.sparcSurface, (self.x-20,self.y-20))
        
    def setPrevNext(self, prev, next):
        #This is mainly used to reset prev,next for sparc when game ends to avoid out-of-bounds error
        self.prev = prev
        self.next = next

    def sparc_movement(self, board_mask):
        
        #Sparc Mask
        newSparc = self.sprite.convert_alpha()
        sparc_mask = pygame.mask.from_surface(newSparc)
        sparc_image = sparc_mask.to_surface()

    #Handles board edge movement - modified from Player class
    def edgeMove(self, board):
        length = len(board.coords)
        
        # Intial pos before movement
        pos = self.getPos()
        
        #Logic for player reaching corner in the clockwise direction
        if self.getPos() == board.coords[self.prev]:
            #If prev-1 point is above the prev point, allow upwards movement, or allow movement to previous edge            
            if board.coords[(self.prev - 1) % length][1] < board.coords[self.prev][1]:
                if self.direction == "up":
                    self.y -= 5
                    self.prev = (self.prev - 1) % length
                    self.next = (self.next - 1) % length
                    
                elif board.coords[self.next][0] > self.getPos()[0]:
                    if self.direction == "right":
                        self.x += 5
                elif board.coords[self.next][0] < self.getPos()[0]:
                    if self.direction == "left":
                        self.x -= 5
            #If prev-1 point is below prev point
            elif board.coords[(self.prev - 1) % length][1] > board.coords[self.prev][1]:
                if self.direction == "down":
                        self.y += 5
                        self.prev = (self.prev - 1) % length
                        self.next = (self.next - 1) % length
                elif board.coords[self.next][0] > self.getPos()[0]:
                    if self.direction == "down":
                        self.x += 5
                elif board.coords[self.next][0] < self.getPos()[0]:
                    if self.direction == "left":
                        self.x -= 5
            #If prev-1 is to the left of prev
            elif board.coords[(self.prev - 1) % length][0] < board.coords[self.prev][0]:
                if self.direction == "left":
                        self.x -= 5
                        self.prev = (self.prev - 1) % length
                        self.next = (self.next - 1) % length
                elif board.coords[self.next][1] > self.getPos()[1]:
                    if self.direction == "down":
                        self.y += 5
                elif board.coords[self.next][1] < self.getPos()[1]:
                    if self.direction == "up":
                        self.y -= 5
            #If prev-1 is to the right of prev
            elif board.coords[(self.prev - 1) % length][0] > board.coords[self.prev][0]:
                if self.direction == "right":
                        self.x += 5
                        self.prev = (self.prev - 1) % length
                        self.next = (self.next - 1) % length
                elif board.coords[self.next][1] > self.getPos()[1]:
                    if self.direction == "down":
                        self.y += 5
                elif board.coords[self.next][1] < self.getPos()[1]:
                    if self.direction == "up":
                        self.y -= 5

        #Logic for player reaching corner in counter clockwise direction
        elif self.getPos() == board.coords[self.next]:
            if board.coords[(self.next +1) % length][1] < board.coords[self.next][1]:
                if self.direction == "up":
                    self.y -= 5
                    self.prev = (self.prev + 1) % length
                    self.next = (self.next + 1) % length
                elif board.coords[self.prev][0] > self.getPos()[0]:
                    if self.direction == "right":
                        self.x += 5
                elif board.coords[self.prev][0] < self.getPos()[0]:
                    if self.direction == "left":
                        self.x -= 5

            elif board.coords[(self.next +1) % length][1] > board.coords[self.next][1]:
                if self.direction == "down":
                        self.y += 5
                        self.prev = (self.prev + 1) % length
                        self.next = (self.next + 1) % length
                elif board.coords[self.prev][0] > self.getPos()[0]:
                    if self.direction == "right":
                        self.x += 5
                elif board.coords[self.prev][0] < self.getPos()[0]:
                    if self.direction == "left":
                        self.x -= 5
                
            elif board.coords[(self.next +1) % length][0] < board.coords[self.next][0]:
                if self.direction == "left":
                        self.x -= 5
                        self.prev = (self.prev + 1) % length
                        self.next = (self.next + 1) % length
                elif board.coords[self.prev][1] > self.getPos()[1]:
                    if self.direction == "down":
                        self.y += 5
                elif board.coords[self.prev][1] < self.getPos()[1]:
                    if self.direction == "up":
                        self.y -= 5

            elif board.coords[(self.next +1) % length][0] > board.coords[self.next][0]:
                if self.direction == "right":
                        self.x += 5
                        self.prev = (self.prev + 1) % length
                        self.next = (self.next + 1) % length
                elif board.coords[self.prev][1] > self.getPos()[1]:
                    if self.direction == "down":
                        self.y += 5
                elif board.coords[self.prev][1] < self.getPos()[1]:
                    if self.direction == "up":
                        self.y -= 5

        #Base movement, keeps player on edge and stops from running off board
        elif board.coords[self.prev][0] == board.coords[self.next][0] and ((self.y > board.coords[self.prev][1] and self.y < board.coords[self.next][1]) or (self.y < board.coords[self.prev][1] and self.y > board.coords[self.next][1])):
            if self.direction == "up":
                self.y -= 5
            elif self.direction == "down":
                self.y += 5
                
        elif board.coords[self.prev][1] == board.coords[self.next][1] and ((self.x > board.coords[self.prev][0] and self.x < board.coords[self.next][0]) or (self.x < board.coords[self.prev][0] and self.x > board.coords[self.next][0])):
            if self.direction == "left":
                self.x -= 5
            elif self.direction == "right":
                self.x += 5

        # Stuck at a corner try a different direction
        if pos[1] == self.getPos()[1] and pos[0] == self.getPos()[0]:
            if self.horizontal:
                if random.random() < 0.5:
                    self.direction = "down"
                else:
                    self.direction = "up"
                self.horizontal = False
            else:
                if random.random() < 0.5:
                    self.direction = "left"
                else:
                    self.direction = "right"
                self.horizontal = True