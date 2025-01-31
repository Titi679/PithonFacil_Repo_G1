import Magatzem


class Quiosc:
    def __init__(self, magatzem):
        self.magatzem = magatzem
        self.usuaris = {}
        self.encarrecs = []
        self.ventes = []

    def registrar_usuari(self, usuari_id):
        if usuari_id not in self.usuaris:
            self.usuaris[usuari_id] = []
            print(f"Usuari '{usuari_id}' registrat correctament.")
        else:
            print(f"Usuari '{usuari_id}' ja està registrat.")

    def consultar_categories(self, es_fred):
        categories = set()
        prestatges = (
            self.magatzem.prestatges_fred if es_fred else self.magatzem.prestatges_despensa
        )
        for prestatge in prestatges:
            for nivell in prestatge.nivells:
                if nivell.categoria:
                    categories.add(nivell.categoria)
        return list(categories)

    def consultar_productes_categoria(self, categoria):
        productes = []
        prestatges = self.magatzem.prestatges_fred + self.magatzem.prestatges_despensa
        for prestatge in prestatges:
            for nivell in prestatge.nivells:
                if nivell.categoria == categoria:
                    productes.extend(nivell.productes)
        return productes

    def realitzar_encarrec(self, usuari_id, productes):
        if usuari_id in self.usuaris:
            self.encarrecs.append((usuari_id, productes))
            self.usuaris[usuari_id].append(productes)
            print(f"Encàrrec realitzat per l'usuari '{usuari_id}'.")
        else:
            print("Error: Usuari no registrat.")

    def consultar_encarrecs(self, usuari_id):
        if usuari_id in self.usuaris:
            return self.usuaris[usuari_id]
        else:
            print("Error: Usuari no registrat.")
            return None

    def consultar_catalog_preu(self):
        prestatges = self.magatzem.prestatges_fred + self.magatzem.prestatges_despensa
        productes = []
        for prestatge in prestatges:
            for nivell in prestatge.nivells:
                productes.extend(nivell.productes)
        return sorted(productes, key=lambda producte: producte.preu)


def interficie():
    """
    Interfície del Quiosc:
    Permet interactuar amb el sistema a través d'un menú d'opcions.
    """
    magatzem = Magatzem() 
    quiosc = Quiosc(magatzem)

    while True:
        print("\n--- Benvingut al Quiosc ---")
        print("1. Registrar-se al sistema.")
        print("2. Consultar les categories disponibles.")
        print("3. Consultar els productes d’una categoria.")
        print("4. Consultar el catàleg de productes per preu.")
        print("5. Consultar els encàrrecs realitzats per un usuari.")
        print("6. Realitzar un encàrrec.")
        print("7. Sortir.")
        opcio = input("Escull una opció: ")

        if opcio == "1":
            usuari_id = input("Introdueix el teu ID d'usuari: ")
            quiosc.registrar_usuari(usuari_id)

        elif opcio == "2":
            tipus = input("Vols consultar categories de fred (sí/no)? ").lower() == "sí"
            categories = quiosc.consultar_categories(tipus)
            print(f"Categories disponibles: {categories}")

        elif opcio == "3":
            categoria = input("Introdueix la categoria a consultar: ")
            productes = quiosc.consultar_productes_categoria(categoria)
            print(f"Productes a la categoria '{categoria}': {productes}")

        elif opcio == "4":
            catalog = quiosc.consultar_catalog_preu()
            print("Catàleg de productes ordenat per preu:")
            for producte in catalog:
                print(producte)

        elif opcio == "5":
            usuari_id = input("Introdueix el teu ID d'usuari: ")
            encarrecs = quiosc.consultar_encarrecs(usuari_id)
            print(f"Encàrrecs realitzats per l'usuari '{usuari_id}': {encarrecs}")

        elif opcio == "6":
            usuari_id = input("Introdueix el teu ID d'usuari: ")
            productes = input("Introdueix els productes (separats per comes): ").split(",")
            quiosc.realitzar_encarrec(usuari_id, productes)

        elif opcio == "7":
            print("Gràcies per utilitzar el Quiosc. Fins aviat!")
            break

        else:
            print("Opció incorrecta. Si us plau, escull una opció vàlida.")


interficie()
