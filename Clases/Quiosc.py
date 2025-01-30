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


def interficie():
    """
    Operacions del quiosc:
    ● Registrar-se al sistema.
    ● Consultar les categories disponibles.
    ● Consultar els productes d’una categoria.
    ● Consultar el catàleg de productes (nom, imatge, categoria, preu) ordenat
    ascendentment per preu.
    ● Consultar els encàrrecs que un usuari hagi realitzat prèviament.
    ● Realitzar un encàrrec (que pot estar format per diferents productes i en diferents
    quantitats) per part d’un usuari identificat.
    """

    # "oli5", "oli verge extra", 32, "olis", 0, False
    simulacio_productes = [("oli1", "oli verge extra", 32, "olis", 0, False), ("oli2", "oli verge extra", 32, "olis", 0, False), ("oli3", "oli verge extra", 32, "olis", 0, False), ("oli4", "oli verge extra", 32, "olis", 0, False), ("oli5", "oli verge extra", 32, "olis", 0, False)]

    print("Benvingut!")
    print("Què vols fer?")
    print("1. Registrar-se al sistema.")
    print("2. Consultar les categories disponibles.")
    print("3. Consultar els productes d’una categoria.")
    print("4. Consultar el catàleg de productes per preu.")
    print("5. Consultar els encàrrecs que un usuari hagi realitzat prèviament.")
    print("6. Realitzar un encàrrec.")
    print("7. Sortir.")
    opcio = input("Opció: ")

    while opcio != "7":
        if opcio == "1":
            print("Registrar-se al sistema.")
        elif opcio == "2":
            print("Consultar les categories disponibles.")
        elif opcio == "3":
            print("Consultar els productes d’una categoria.")
        elif opcio == "4":
            print("Consultar el catàleg de productes per preu.")
            print(rankingVendas(simulacio_productes))
        elif opcio == "5":
            print("Consultar els encàrrecs que un usuari hagi realitzat prèviament.")
        elif opcio == "6":
            print("Realitzar un encàrrec.")
        elif opcio == "7":
            print("Sortir.")
        else:
            print("Opció incorrecta.")

        print("Què vols fer?")
        print("1. Registrar-se al sistema.")
        print("2. Consultar les categories disponibles.")
        print("3. Consultar els productes d’una categoria.")
        print("4. Consultar el catàleg de productes per preu.")
        print("5. Consultar els encàrrecs que un usuari hagi realitzat prèviament.")
        print("6. Realitzar un encàrrec.")
        print("7. Sortir.")
        opcio = input("Opció: ")


interficie()