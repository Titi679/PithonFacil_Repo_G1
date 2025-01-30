# quiosc.py

usuaris = {}
encarrecs = []

# Productes inicials
productes = [
    {"id": "cc-zero", "nom": "Coca-Cola Zero", "preu": 2, "categoria": "beguda", "fred": True},
    {"id": "cc", "nom": "Coca-Cola", "preu": 2.1, "categoria": "beguda", "fred": True},
    {"id": "fanta", "nom": "Fanta", "preu": 1.5, "categoria": "beguda", "fred": True},
    {"id": "oli1", "nom": "Oli verge extra", "preu": 20, "categoria": "olis", "fred": False},
]


def obtenir_productes_per_categoria(categoria):
    """Filtra productes per categoria"""
    return [p for p in productes if p["categoria"] == categoria]


def obtenir_categories():
    """Retorna llista de categories"""
    return list({p["categoria"] for p in productes})


def registrar_usuari(usuari_id):
    """nou usuari"""
    if usuari_id not in usuaris:
        usuaris[usuari_id] = []
        return True
    return False


def realitzar_encarreg(usuari_id, productes_encarrec):
    """Gestiona un nou encàrrec"""
    if usuari_id in usuaris:
        encarrecs.append({"usuari": usuari_id, "productes": productes_encarrec})
        return True
    return False