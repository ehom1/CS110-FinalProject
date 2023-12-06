import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, img = "assets/doodle.jpg"):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.width = 30
        self.height = 45
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x 
        self.rect.y = y
        self.rect.center = (x, y)
        self.velocity_y = 0
        self.scroll_threshold = 200
        self.scroll = 0

        pygame.display.flip()
        
    def update_jump(self, gravity):
        self.scroll = 0 
        self.dx = 0
        self.dy = 0
        
        self.w, self.h = pygame.display.get_window_size()
        
        self.velocity_y += gravity
        self.dy += self.velocity_y
        
        if self.rect.bottom + self.dy > self.h:
            self.dy = 0
            self.velocity_y = -20
        
        if self.rect.top <= self.scroll_threshold:
            if self.velocity_y < 0:
                self.scroll = -self.dy  
        
        self.rect.x += self.dx
        self.rect.y += self.dy + self.scroll
        
        return self.scroll
        
    def wrap_around(self, screen_width):
        if self.rect.x > screen_width:
            self.rect.x = -self.rect.width
        elif self.rect.x < -self.rect.width:
            self.rect.x = screen_width