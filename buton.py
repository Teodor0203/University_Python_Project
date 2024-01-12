class Buton():
        def __init__(self, imagine, pos, text_input, font, culoare_baza, culoare_activare):
            self.imagine = imagine
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.font = font
            self.culoare_baza = culoare_baza
            self.culoare_activare = culoare_activare
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.culoare_baza)
            if self.imagine is None:
                self.imagine = self.text
            self.rect = self.imagine.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self, ecran):
            if self.imagine is not None:
                ecran.blit(self.imagine, self.rect)

            ecran.blit(self.text, self.text_rect)

        def verificaInput(self, positie):
            if positie[0] in range(self.rect.left, self.rect.right) and positie[1] in range(self.rect.top, self.rect.bottom):
                return True
            else:
                return False

        def schimbaCuloare(self, positie):
            if positie[0] in range(self.rect.left, self.rect.right) and positie[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.culoare_activare)
            else:
                self.text = self.font.render(self.text_input, True, self.culoare_baza)
