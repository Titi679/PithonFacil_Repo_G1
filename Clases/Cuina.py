class Cuina:
    def __init__(self):
        self.pedidos_preparacio = []  #
        self.historial_pedidos = []  

    def afegir_comanda(self, comanda):
        self.pedidos_preparacio.append(comanda)
        print(f"Comanda {comanda['id']} afegida a la cuina per preparar.")

    def preparar_comanda(self):
        if self.pedidos_preparacio:
            comanda = self.pedidos_preparacio.pop(0)
            self.historial_pedidos.append(comanda)
            print(f"Comanda {comanda['id']} preparada.")
            return comanda
        else:
            print("No hi ha comandes en preparació.")
            return None

    def consultar_comandes_preparacio(self):
        return self.pedidos_preparacio

    def consultar_historial_comandes(self):
        return self.historial_pedidos
