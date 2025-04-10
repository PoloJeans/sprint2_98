import pygame

class Player():
    def __init__(self, x, y, prev, next):
        self.health = 50
        self.x = x
        self.y = y
        self.prev = prev
        self.next = next
        
        

    def setHealth(self, health):
        self.health = health

    def getHealth(self):
        return self.health
    
    def getPos(self):
        return (self.x, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), 20)

    def move(self, board):
        pass

    def reset(self):
        self.health = 50
        self.x
        self.y

    """
    Base edge movement implementation
    3----------2
    |          |
    |          |
    |          |
    0----------1
    Prev = 0
    Next = 1

    The board is drawn from a list of the form [(x,y)], representing 
    the vertices of the board. When the player reaches a vertice, they have the option 
    to move either onto the next edge and increment prev and next pointers, restricting their 
    movement to the new edge, or back to the previous edge, and restricting to that edge. 

    All movement must occur in 10 units per frame.
    """

    #This abomination works and is bulletproof when it does
    #Add your points to the board.coords in the correct order 
    #and it'll handle edge movement automagically
    def edgeMove(self, board, keys):
        length = len(board.coords)

        #Logic for player reaching corner in the clockwise direction
        if self.getPos() == board.coords[self.prev]:
            #If prev-1 point is above the prev point, allow upwards movement, or allow movement to previous edge            
            if board.coords[(self.prev - 1) % length][1] < board.coords[self.prev][1]:
                if keys[pygame.K_w]:
                    self.y -= 10
                    self.prev = (self.prev - 1) % length
                    self.next = (self.next - 1) % length
                elif board.coords[self.next][0] > self.getPos()[0]:
                    if keys[pygame.K_d]:
                        self.x += 10
                elif board.coords[self.next][0] < self.getPos()[0]:
                    if keys[pygame.K_a]:
                        self.x -= 10
            #If prev-1 point is below prev point
            elif board.coords[(self.prev - 1) % length][1] > board.coords[self.prev][1]:
                if keys[pygame.K_s]:
                        self.y += 10
                        self.prev = (self.prev - 1) % length
                        self.next = (self.next - 1) % length
                elif board.coords[self.next][0] > self.getPos()[0]:
                    if keys[pygame.K_d]:
                        self.x += 10
                elif board.coords[self.next][0] < self.getPos()[0]:
                    if keys[pygame.K_a]:
                        self.x -= 10
            #If prev-1 is to the left of prev
            elif board.coords[(self.prev - 1) % length][0] < board.coords[self.prev][0]:
                if keys[pygame.K_a]:
                        self.x -= 10
                        self.prev = (self.prev - 1) % length
                        self.next = (self.next - 1) % length
                elif board.coords[self.next][1] > self.getPos()[1]:
                    if keys[pygame.K_s]:
                        self.y += 10
                elif board.coords[self.next][1] < self.getPos()[1]:
                    if keys[pygame.K_w]:
                        self.y -= 10
            #If prev-1 is to the right of prev
            elif board.coords[(self.prev - 1) % length][0] > board.coords[self.prev][0]:
                if keys[pygame.K_d]:
                        self.x += 10
                        self.prev = (self.prev - 1) % length
                        self.next = (self.next - 1) % length
                elif board.coords[self.next][1] > self.getPos()[1]:
                    if keys[pygame.K_s]:
                        self.y += 10
                elif board.coords[self.next][1] < self.getPos()[1]:
                    if keys[pygame.K_w]:
                        self.y -= 10

        #Logic for player reaching corner in counter clockwise direction
        elif self.getPos() == board.coords[self.next]:
            if board.coords[(self.next +1) % length][1] < board.coords[self.next][1]:
                if keys[pygame.K_w]:
                    self.y -= 10
                    self.prev = (self.prev + 1) % length
                    self.next = (self.next + 1) % length
                elif board.coords[self.prev][0] > self.getPos()[0]:
                    if keys[pygame.K_d]:
                        self.x += 10
                elif board.coords[self.prev][0] < self.getPos()[0]:
                    if keys[pygame.K_a]:
                        self.x -= 10

            elif board.coords[(self.next +1) % length][1] > board.coords[self.next][1]:
                if keys[pygame.K_s]:
                        self.y += 10
                        self.prev = (self.prev + 1) % length
                        self.next = (self.next + 1) % length
                elif board.coords[self.prev][0] > self.getPos()[0]:
                    if keys[pygame.K_d]:
                        self.x += 10
                elif board.coords[self.prev][0] < self.getPos()[0]:
                    if keys[pygame.K_a]:
                        self.x -= 10
                
            elif board.coords[(self.next +1) % length][0] < board.coords[self.next][0]:
                if keys[pygame.K_a]:
                        self.x -= 10
                        self.prev = (self.prev + 1) % length
                        self.next = (self.next + 1) % length
                elif board.coords[self.prev][1] > self.getPos()[1]:
                    if keys[pygame.K_s]:
                        self.y += 10
                elif board.coords[self.prev][1] < self.getPos()[1]:
                    if keys[pygame.K_w]:
                        self.y -= 10

            elif board.coords[(self.next +1) % length][0] > board.coords[self.next][0]:
                if keys[pygame.K_d]:
                        self.x += 10
                        self.prev = (self.prev + 1) % length
                        self.next = (self.next + 1) % length
                elif board.coords[self.prev][1] > self.getPos()[1]:
                    if keys[pygame.K_s]:
                        self.y += 10
                elif board.coords[self.prev][1] < self.getPos()[1]:
                    if keys[pygame.K_w]:
                        self.y -= 10

        #Base movement, keeps player on edge and stops from running off board
        elif board.coords[self.prev][0] == board.coords[self.next][0] and ((self.y > board.coords[self.prev][1] and self.y < board.coords[self.next][1]) or (self.y < board.coords[self.prev][1] and self.y > board.coords[self.next][1])):
            if keys[pygame.K_w]:
                self.y -= 10
            elif keys[pygame.K_s]:
                self.y += 10
                
        elif board.coords[self.prev][1] == board.coords[self.next][1] and ((self.x > board.coords[self.prev][0] and self.x < board.coords[self.next][0]) or (self.x < board.coords[self.prev][0] and self.x > board.coords[self.next][0])):
            if keys[pygame.K_a]:
                self.x -= 10
            elif keys[pygame.K_d]:
                self.x += 10
