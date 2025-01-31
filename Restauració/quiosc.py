# quiosc.py
import magatzem #already imported in the main file

class Usuari:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.encarrecs = []

    def set_enc(self, encarrec):
        self.encarrecs.append(encarrec)

class Quiosc:
    def __init__(self):
        self.usuaris = {}
        self.encarrecs = []
        self.productes = []
        despensa = magatzem.Despensa()
        frigo = magatzem.Frigo()
        self.magatzem = [despensa, frigo]

    def get_usuaris(self):
        return self.usuaris

    def obtenir_productes_per_categoria(self, categoria):
        """Filtra productes per categoria"""
        return [p for p in self.productes if p.get_cat() == categoria]
    
    def obtenir_categories(self):
        """Retorna llista de categories"""
        return list({p.get_cat() for p in self.productes})
    
    def registrar_usuari(self, usuari_id, name):
        """nou usuari"""
        if usuari_id not in self.usuaris:
            usuari = Usuari(usuari_id, name)
            self.usuaris[usuari_id] = usuari #correct dictionary assignment
            return True
        else:
            return False

    def planificar_encarrec(self):
        """Treu el primer encàrrec de la llista"""
        if self.encarrecs: #check if the list is empty
            return self.encarrecs.pop(0)
        return None

    def top_vendes(self):
        """Retorna top productes venuts"""
        return sorted(self.productes, key=lambda x: x.get_vendas(), reverse=True) #access get_vendas method
    
    def realitzar_encarreg(self, usuari_id, productes_encarrec): #added self parameter
        """Gestiona un nou encàrrec"""
        for producte in productes_encarrec:
            producte.set_vendas(1)
            if producte.fred():
                espai = self.magatzem[1]
                correct = espai.set_vendas(producte, 1) #changed set_venda to set_vendas
                if correct:
                    self.encarrecs.append({"usuari": usuari_id, "productes": productes_encarrec}) #added self
                    self.usuaris
            return False

    def planificar_encarrec(self):
        """Treu el primer encàrrec de la llista"""
        if self.encarrecs[0] != None:
            return self.encarrecs.pop(0)
        return None

    def top_vendes(self):
        """Retorna top productes venuts"""
        if len(self.productes) != 0:
            return sorted(self.productes.items(), key=lambda x: x.get_preu(), reverse=True)
        else:
            return None
    
    def realitzar_encarreg(usuari_id, productes_encarrec):
        """Gestiona un nou encàrrec"""
        for producte in productes_encarrec:
            producte.set_vendas(1)
            if producte.fred():
                espai = self.magatzem[1]
                correct = espai.set_venda(producte, 1)
                if correct:
                    encarrecs.append({"usuari": usuari_id, "productes": productes_encarrec})
                    self.usuaris.get(usuari_id).set_enc({"productes": productes_encarrec})
                    return True
        else:
            return False

    def add_contenidor(self, Contenidor):
        producte = Contenidor.get_pr()
        if producte.fred():
            self.magatzem[1].add(Contenidor)
        else:
            self.magatzem[0].add(Contenidor)
        if producte not in self.productes:
            self.productes.append(producte)

