from functools import reduce

class Quiosc:
    def _init_(self, magatzem):
        self.magatzem = magatzem
        self.usuaris = {}
        self.encarrecs = []
        self.ventes = []

    # def registrar_usuari(self, usuari_id):
    #     self.usuaris[usuari_id] = []

    # def consultar_categories(self, es_fred):
    #     categories = set()
    #     prestatges = self.magatzem.prestatges_fred if es_fred else self.magatzem.prestatges_despensa
    #     for prestatge in prestatges:
    #         for nivell in prestatge.nivells:
    #             if nivell.categoria:
    #                 categories.add(nivell.categoria)
    #     return list(categories)

    def realitzar_encarrec(self, usuari_id, productes):
        if usuari_id in self.usuaris:
            self.encarrecs.append((usuari_id, productes))
            self.usuaris[usuari_id].append(productes)
        else:
            print("Error: Usuari no registrat.")


class Magatzem:
  def __init__(self):
    self.espai = []
  
  def get_p(self, pos):
    for prestatge in self.espai:
      if prestatge.get_pos() == pos:
        return prestatge
  
  def get_espai(self):
    return self.espai

  #def organitzar(self, Producte):
    # Codi 
  
  def add(self, Contenidor, pos):
    #pos = self.organitzar(Contenidor.get_pr(Producte))
    Contenidor.set(pos)
    for prestatge in self.espai:
      if prestatge.get_pos() == pos:
        prestatge.add(Contenidor)
  
  def delete(self, Contenidor):
    pos = Contenidor.get_pos
    i = 0
    end = False
    while i < len(self.espai) and not end:
      if self.espai(i).get_pos() == pos:
        end = True
    self.espai(i).get_cont().delete(0)

class Despensa(Magatzem):
  def __init__(self):
    super().__init__()
    x = 0
    for x in range (0,4):
      for y in range (0,12):
        prestatge = Prestatge((x,y))
        self.espai.append(prestatge)

class Frigo(Magatzem):
  def __init__(self):
    super().__init__()
    for x in range (0,4):
      for y in range (0,4):
        prestatge = Prestatge((x,y))
        self.espai.append(prestatge)

class Prestatge:
  def __init__(self, pos):
    self.pos = (pos[0], pos[1])
    self.quantitat = 0
    self.continguts = []
  
  def getq(self):
    return reduce(lambda acc, contingut: acc + contingut.get_q(), self.continguts, 0)
  
  def get_pos(self):
    return self.pos

  def get_cont(self):
    return self.continguts

  def add(self, Contenidor):
    self.quantitat = self.quantitat + Contenidor.get_q()
    i = len(self.continguts)
    self.continguts.append(Contenidor)
    while i > 0:
      self.continguts[i] = self.continguts[i-1]
    self.continguts[0] = Contenidor
  
  def __str__(self):
    txt = ''
    for contenidor in self.continguts:
      nom = contenidor.get_pr().get_nom()
      preu = contenidor.get_pr().get_preu()
      categoria = contenidor.get_pr().get_cat()
      txt =  txt + f"\nNom: {nom} \nPreu: {preu} \nCategoria: {categoria} \nFred: Si \nSafates: {self.quantitat} \nPosició: {self.pos}"
    return txt

class Contenidor:
  def __init__(self, quantitat, producte):
    self.quantitat = quantitat
    self.producte = producte
  
  def get_pr(self):
    return self.producte

  def get_q(self):
    return self.quantitat
  
  def set(self, pos):
    self.pos = pos


class Producte:
  def __init__(self, id, nom, preu, categoria, fred):
    self.id = id
    self.nom = nom
    self.preu = preu
    self.categoria = categoria
    self.vendas = 0
    self.fred = fred

  def get_nom(self):
    return self.nom

  def get_preu(self):
    return self.preu

  def get_cat(self):
    return self.categoria

  def __str__(self):
    if self.fred:
      return f"\nID: {self.id} \nNom: {self.nom} \nPreu: {self.preu} \nCategoria: {self.categoria} \nFred: Si"
    else:
      return f"\nID: {self.id} \nNom: {self.nom} \nPreu: {self.preu} \nCategoria: {self.categoria} \nFred: No"
  
  def fred(self):
    if self.fred:
      return True
    else:
      return False

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
