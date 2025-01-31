from Magatzem import Magatzem
from Quiosc import Quiosc
from Cuina import Cuina

def main():
    magatzem = Magatzem()
    quiosc = Quiosc(magatzem)
    cuina = Cuina()

end = False


print("\n*** UPC Restauració ***")

while not end:
    print("\nMenú Principal:")
    print("1. Registrar usuari")
    print("2. Veure categories")
    print("3. Veure productes per categoria")
    print("4. Fer encàrrec")
    print("5. Consultar top vendes")
    print("6. Sortir")

    opcio = input("Selecciona una opció: ")

    if opcio == "1":
        usuari = input("Introdueix ID d'usuari: ")
        if registrar_usuari(usuari):
            print(f"Usuari {usuari} registrat!")
        else:
            print("[!] Error: L'usuari ja existeix")
    elif opcio == "2":
        print("Categories disponibles:")
        print(obtenir_categories())
    elif opcio == "3":
        print(obtenir_categories())
        categoria = input("Introdueix el nom de la categoria: ")
        productes_categoria = obtenir_productes_per_categoria(categoria)
        if productes_categoria:
            print(f"Productes de la categoria '{categoria}':")
            for p in productes_categoria:
                print(f"ID: {p['id']} | Nom: {p['nom']} | Preu: {p['preu']}€ | Categoria: {p['categoria']}")
        else:
            print("[i] Categoria no trobada")
    elif opcio == "4":
        usuari = input("Introdueix el teu ID d'usuari: ")
        if usuari not in usuaris:
            print("[!] Error: Has de registrar-te abans de fer un encàrrec")
            continue
        productes_encarrec = []
        print("Escull productes (escriu 'fi' per acabar):")
        while True:
            producte_id = input("ID del producte: ")
            if producte_id.lower() == "fi":
                break
            producte = next((p for p in productes if p["id"] == producte_id), None) # https://www.w3schools.com/python/ref_func_next.asp
            if producte:
                productes_encarrec.append(producte)
                ventes[producte_id] = ventes.get(producte_id, 0) + 1
                print(f"Producte afegit: {producte['nom']}")
            else:
                print("ID no valid")
        if productes_encarrec:
            realitzar_encarreg(usuari, productes_encarrec)
            print("[i] Encàrrec realitzat amb exit!")
        else:
            print("[i] Encàrrec buit")
    elif opcio == "5":
        ranking = top_vendes()
        if ranking:
            print("Top productes més venuts:")
            for producte_id, quantitat in ranking:
                producte = next(p for p in productes if p["id"] == producte_id)
                print(f"ID: {producte_id} | Nom: {producte['nom']} | Vendes: {quantitat}")
        else:
            print("[i] Encara no hi ha vendes registrades")
    elif opcio == "6":
        print("Fins aviat!")
        end = True
    else:
        print("[i] Opcio no valida")