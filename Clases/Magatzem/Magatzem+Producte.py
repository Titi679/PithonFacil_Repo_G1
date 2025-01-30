class Espai:
  def init(self)
    self.espai = []
  
  def add(self, Contenidor): #En el main es diferencia si la funció s'aplica sobre el magatzem o al frigorífic
    pos = self.organitzar(Contenidor)
    self.espai[pos] = 
  
  def organitzar(self, Contenidor)

class Magatzem(Espai):
  def init(self):
    super().init()

class Contenidor:
  def init(self, quantitat, pos, producte)
    self.quantitat = quantitat
    self.pos = pos
    self.producte = producte

class Producte:
  def init(self, id, nom, preu, categoria, vendas, fred):
    self.id = id
    self.nom = nom
    self.preu = preu
    self.categoria = categoria
    self.vendas = vendas
    self.fred = fred

  def str(self):
    return f"id: {self.id} nom: {self.nom} preu: {self.preu} categoria: {self.categoria}"
