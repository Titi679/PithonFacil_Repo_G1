from Magatzem import Magatzem
from Quiosc import Quiosc
from Cuina import Cuina

def main():
    magatzem = Magatzem()
    quiosc = Quiosc(magatzem)
    cuina = Cuina()

    print("Benvingut")
    while True:
        print("\nSelecciona una opció:")
        print("1. Registrar un usuari al Quiosc.")
        print("2. Consultar categories disponibles.")
        print("3. Consultar productes d'una categoria.")
        print("4. Consultar catàleg de productes ordenat per preu.")
        print("5. Realitzar un encàrrec al Quiosc.")
        print("6. Consultar els encàrrecs d'un usuari.")
        print("7. Afegir comanda a la Cuina.")
        print("8. Preparar la següent comanda de la Cuina.")
        print("9. Consultar comandes en preparació.")
        print("10. Consultar historial de comandes preparades.")
        print("11. Sortir.")
        opcio = input("Introdueix el número de l'opció: ")

        if opcio == "1":
            usuari_id = input("Introdueix l'ID de l'usuari: ")
            quiosc.registrar_usuari(usuari_id)
            print(f"Usuari {usuari_id} registrat amb èxit.")

        elif opcio == "2":
            es_fred = input("Vols consultar categories de fred? (sí/no): ").lower() == "sí"
            categories = quiosc.consultar_categories(es_fred)
            print(f"Categories disponibles: {categories}")

        elif opcio == "3":
            categoria = input("Introdueix la categoria: ")
            productes = magatzem.consultar_productes_categoria(categoria)
            print(f"Productes de la categoria {categoria}: {productes}")

        elif opcio == "4":
            productes = magatzem.consultar_cataleg_productes()
            print("Catàleg de productes ordenat per preu:")
            for producte in productes:
                print(producte)

        elif opcio == "5":
            usuari_id = input("Introdueix l'ID de l'usuari: ")
            productes = input("Introdueix els productes separats per comes: ").split(",")
            quiosc.realitzar_encarrec(usuari_id, productes)
            print(f"Encàrrec realitzat per l'usuari {usuari_id}.")

        elif opcio == "6":
            usuari_id = input("Introdueix l'ID de l'usuari: ")
            encarrecs = quiosc.consultar_encarrecs(usuari_id)
            if encarrecs:
                print(f"Encàrrecs de l'usuari {usuari_id}: {encarrecs}")

        elif opcio == "7":
            comanda_id = input("Introdueix l'ID de la comanda: ")
            detalls_comanda = input("Introdueix els detalls de la comanda: ")
            cuina.afegir_comanda({"id": comanda_id, "detalls": detalls_comanda})

        elif opcio == "8":
            comanda_preparada = cuina.preparar_comanda()
            if comanda_preparada:
                print(f"Comanda preparada: {comanda_preparada}")

        elif opcio == "9":
            comandes = cuina.consultar_comandes_preparacio()
            print("Comandes en preparació:")
            for comanda in comandes:
                print(comanda)

        elif opcio == "10":
            historial = cuina.consultar_historial_comandes()
            print("Historial de comandes preparades:")
            for comanda in historial:
                print(comanda)

        elif opcio == "11":
            print("Sortint.")
            break

        else:
            print("Opció no vàlida. Introdueix un número de l'1 a l'11.")

if __name__ == "__main__":
    main()
