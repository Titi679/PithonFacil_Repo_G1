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

  def add(self, Contenidor, pos): #added pos parameter
    #pos = self.organitzar(Contenidor.get_pr(Producte)) #removed this line
    Contenidor.set(pos)
    for prestatge in self.espai:
      if prestatge.get_pos() == pos:
        prestatge.add(Contenidor)

  def delete(self, Contenidor):
    pos = Contenidor.get_pos() #added ()
    i = 0
    end = False
    while i < len(self.espai) and not end:
      if self.espai[i].get_pos() == pos: #changed self.espai(i) to self.espai[i]
        end = True
    self.espai[i].get_cont().remove(Contenidor) #changed .delete(0) to .remove(Contenidor)

  def set_vendas(self, producte, num):
    end = False
    for prestatge in self.espai:
      if prestatge.get_cont(): #added if condition to check if the list is empty
          contenidor = prestatge.get_cont()[0]
          if contenidor.get_pr().get_nom() == producte.get_nom():
              correcte = prestatge.get_cont()[0].set_vendas(num)
              if correcte and prestatge.get_cont()[0].get_q() == 0:
                  contenidor = prestatge.get_cont()[0] #added [0] to access the first element
                  self.delete(contenidor)
              return correcte
    return False

class Despensa(Magatzem):
  def __init__(self):
    super().__init__()
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
    from functools import reduce #added import
    return reduce(lambda acc, contingut: acc + contingut.get_q(), self.continguts, 0)

  def get_pos(self):
    return self.pos

  def get_cont(self):
    return self.continguts

  def add(self, Contenidor):
    self.quantitat = self.quantitat + Contenidor.get_q()
    self.continguts.append(Contenidor) #simplified add function

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
    self.pos = None #initialize pos

  def get_pr(self):
    return self.producte

  def get_q(self):
    return self.quantitat

  def set(self, pos):
    self.pos = pos
  
  def get_pos(self): #added get_pos method
      return self.pos

  def set_vendas(self, num):
    if self.quantitat - num >= 0:
      self.quantitat = self.quantitat - num
      return True
    else:
      return False

class Producte:
  def __init__(self, id, nom, preu, categoria, fred):
    self.id = id
    self.nom = nom
    self.preu = preu
    self.categoria = categoria
    self.vendas = 0
    self.fred = fred

  def get_id(self):
    return self.id
    
  def get_nom(self):
    return self.nom

  def get_preu(self):
    return self.preu

  def get_cat(self):
    return self.categoria
  
  def get_vendas(self): #added get_vendas
      return self.vendas

  def set_vendas(self, num):
    self.vendas = self.vendas + num

  def __str__(self):
    if self.fred:
      return f"\nID: {self.id} \nNom: {self.nom} \nPreu: {self.preu} \nCategoria: {self.categoria} \nFred: Si"
    else:
      return f"\nID: {self.id} \nNom: {self.nom} \nPreu: {self.preu} \nCategoria: {self.categoria} \nFred: No"

  def fred(self):
    return self.fred #simplified fred function
