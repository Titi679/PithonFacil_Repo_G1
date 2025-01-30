class Espai:
  def __init__(self):
    self.espai = []
  
  def add(self, Contenidor): #En el main es diferencia si la funció s'aplica sobre el magatzem o al frigorífic
    pos = self.organitzar(Contenidor)
    self.espai[pos] = 
  
  def organitzar(self, Contenidor):


class Magatzem(Espai):
  def __init__(self):
    super().init()


class Contenidor:
  def __init__(self, quantitat, pos, producte)
    self.quantitat = quantitat
    self.pos = pos
    self.producte = producte

class Producte:
  def __init__(self, id, nom, preu, categoria, vendas, fred):
    self.id = id
    self.nom = nom
    self.preu = preu
    self.categoria = categoria
    self.vendas = vendas
    self.fred = fred

  def __str__(self):
    return f"id: {self.id} nom: {self.nom} preu: {self.preu} categoria: {self.categoria}"
