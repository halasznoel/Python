class HíresFilm:
    def __init__(self, címe, hossz, nemzet):
        self.cím = címe
        self.hossz = hossz
        self.nemzet = nemzet
    def orszag(self):
        if self.nemzet == "USA":
            return "Amerikai"
        elif self.nemzet == "GB":
            return "Angol"