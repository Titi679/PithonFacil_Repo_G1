# cuina.py
encarrecs_pendents = []  # Llista FIFO d'encàrrecs
ventes = {}  # Registre de vendes per producte

def planificar_encarrec():
    """Treu el primer encàrrec de la llista"""
    if encarrecs_pendents:
        return encarrecs_pendents.pop(0)
    return None

def top_vendes():
    """Retorna top 5 productes més venuts"""
    return sorted(ventes.items(), key=lambda x: x[1], reverse=True)[:5]