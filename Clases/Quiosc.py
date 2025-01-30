# Quiosc.py
import Magatzem

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



def rankingVendas(productes):
  return sorted(productes, key=lambda producte: producte.vendas, reverse=True)