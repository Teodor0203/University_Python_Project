import pygame
class Cursor():

    def __init__(self, cale_imagine, ecran, latime, inaltime):
        self.imagine = pygame.image.load(cale_imagine)
        self.imagine = pygame.transform.scale(self.imagine, (latime, inaltime))
        self.ecran = ecran
        self.width = latime
        self.height = inaltime
        pygame.mouse.set_visible(False)

    def update(self):
        self.pos =pygame.mouse.get_pos()
        self.ecran.blit(self.imagine, self.pos)


