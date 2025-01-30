# Quiosc.py
from Clases.Magatzem import Producte

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



def afegir_venda(id_producte):
    # --tODO: Implementar la funció afegir_venda quan s'acabi el magatzem

    """
    Actualiza la seguent classe amb la funció afegir_venda:
    """
print(Producte)
