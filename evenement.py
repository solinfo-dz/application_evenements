class Evenement:
    def __init__(self, id, titre, date, heure, lieu, description):
        self.__id = id              # privé
        self.titre = titre          # public
        self.date = date            # public
        self.heure = heure          # public
        self.lieu = lieu            # public
        self.description = description  # public

    def afficherInfos(self):
        print("=== Événement ===")
        print(f"ID : {self.__id}")
        print(f"Titre : {self.titre}")
        print(f"Date : {self.date} à {self.heure}")
        print(f"Lieu : {self.lieu}")
        print(f"Description : {self.description}")
        print("----------------------")

class Billet:
    def __init__(self, id, prix, numero):
        self.__id = id          # privé
        self.prix = prix        # public
        self.numero = numero    # public
        self.__estVendu = False # privé

    def vendre(self):
        if not self.__estVendu:
            self.__estVendu = True
            print(f"Billet n°{self.numero} vendu.")
        else:
            print(f"Billet n°{self.numero} déjà vendu.")
class Concert(Evenement):
    def __init__(self, id, titre, date, heure, lieu, description,
                 artiste, genre):
        super().__init__(id, titre, date, heure, lieu, description)
        self.artiste = artiste    # public
        self.genre = genre        # public
        self._billets = []        # "protégé" : liste de Billet

    def ajouterBillet(self, billet):
        self._billets.append(billet)

    def afficherBillets(self):
        print(f"Billets pour le concert {self.titre} :")
        for b in self._billets:
            print(f"- n°{b.numero}, {b.prix} DA")
class Exposition(Evenement):
    def __init__(self, id, titre, date, heure, lieu, description,
                 theme, artistePrincipal):
        super().__init__(id, titre, date, heure, lieu, description)
        self.theme = theme                    # public
        self.artistePrincipal = artistePrincipal  # public
class Conference(Evenement):
    def __init__(self, id, titre, date, heure, lieu, description,
                 sujet, intervenant):
        super().__init__(id, titre, date, heure, lieu, description)
        self.sujet = sujet         # public
        self.intervenant = intervenant  # public
        self._billets = []         # protégé

    def ajouterBillet(self, billet):
        self._billets.append(billet)

    def afficherBillets(self):
        print(f"Billets pour la conférence {self.titre} :")
        for b in self._billets:
            print(f"- n°{b.numero}, {b.prix} DA")

# Créer un concert
Concert1 = Concert(
    10,
    "jazz 2025",
    "14/10/2025",
    "20:00",
    "theatre",
    "culture",
    "clodio",
    "musique"
)

# Créer un billet
b1 = Billet(1, 300, "T007")
b2=Billet(2,300,"T509")# Ajouter le billet au concert
Concert1.ajouterBillet(b1)
Concert1.ajouterBillet(b2)

# Vendre le billet
b1.vendre()
Concert1.afficherBillets()
