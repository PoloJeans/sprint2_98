class Button():
    def __init__(self, image, pos, textIn, font):
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.textIn = textIn
        self.text = font.render(self.textIn, True, "black")
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.textRect = self.text.get_rect(center=(self.x, self.y))

    def update(self,screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

    def checkInput(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False

    def changeColour(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.textIn, True, "white")
        else:
            self.text = self.font.render(self.textIn, True, "black")

