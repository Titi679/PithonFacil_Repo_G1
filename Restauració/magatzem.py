# magatzem.py

magatzem = {
    "frigo": {},
    "despensa": {}
}


def inicialitzar_magatzem():
    """Inicialitza els prestatges"""
    # Configuració frigorífic (4*4) ¿?
    for x in range(4):
        for y in range(4):
            magatzem["frigo"][(x, y)] = {
                "categoria": None,
                "productes": [],
                "capacitat": 50
            }

    # Configuració despensa (12*4) ¿?
    for x in range(12):
        for y in range(4):
            magatzem["despensa"][(x, y)] = {
                "categoria": None,
                "productes": [],
                "capacitat": 50
            }
    return magatzem


def afegir_producte(producte, es_fred):
    """Afegeix un producte al magatzem"""
    zona = "frigo" if es_fred else "despensa"
    categoria = producte["categoria"]

    # Cerca posició
    for pos, detalls in magatzem[zona].items():
        if detalls["categoria"] == categoria and len(detalls["productes"]) < detalls["capacitat"]:
            detalls["productes"].append(producte)
            return True
        elif detalls["categoria"] is None:
            detalls["categoria"] = categoria
            detalls["productes"].append(producte)
            return True
    return False


def obtenir_unitats(pos, es_fred):
    """Retorna unitats disponibles d'una pos"""
    zona = "frigo" if es_fred else "despensa"
    return len(magatzem[zona][pos]["productes"]) if pos in magatzem[zona] else 0