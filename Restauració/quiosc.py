# quiosc.py
import magatzem

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
        despensa = Despensa()
        frigo = Frigo()
        self.magatzem = [despensa, frigo]

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
            self.usuaris.append((usuari_id: usuari))
            return True
        else:
            return False
    
    def realitzar_encarreg(usuari_id, productes_encarrec):
        """Gestiona un nou encàrrec"""
        if usuari_id in usuaris:
            for producte in productes_encarrec:
                if producte not in self.productes:
                    return False
                else:
                    producte.set_vendas(1)
                    if producte.fred():
                        espai = self.magatzem[1]
                        correct = espai.set_venda(producte, 1)
                        if correct:
                            encarrecs.append({"usuari": usuari_id, "productes": productes_encarrec})
                            self.usuaris.get(usuari_id).set_enc("productes": productes_encarrec))
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

# test
#despensa = Despensa()
frigo = Frigo()
#magatzem = [despensa, frigo]

producte1 = Producte("oli5", "oli verge extra", 32, "olis", False)
producte2 = Producte("wine1", "Blanc Pescador",  10, "begudes", False)
producte3 = Producte("wine2", "Albariño", 14, "begudes", False)

contenidor11 = Contenidor(50, producte1)
contenidor12 = Contenidor(25, producte1)
contenidor2 = Contenidor(75, producte2)
contenidor3 = Contenidor(50, producte3)

frigo.add(contenidor11, (0,0))
frigo.add(contenidor12, (0,1))
frigo.add(contenidor2, (1,1))
frigo.add(contenidor3, (2,1))

print(producte1)
print(producte2)
print(producte3)

for prestatge in frigo.get_espai():
  if prestatge.getq() != 0:
    print(prestatge)
