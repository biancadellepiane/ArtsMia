import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()

        numNodi, numArchi = self._model.getGraphDetails()

        #stampo
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {numNodi} e Numero di archi: {numArchi}"))

        self._view.update_page()

    def handleCompConnessa(self,e):
        idOggetto = self._view._txtIdOggetto.value

       #controllo correttezza dell'inserimento
        #se vuoto
        if idOggetto == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Nessun valore inserito", color="red"))
            self._view.update_page()
            return

        #se non contertibile a int
        try:
            id = int(idOggetto)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Valore inserito non valido, inserisci un numero", color="red"))
            self._view.update_page()
            return

        #valore da stampare che indica il num di vertici della componente connessa
        sizeCC = self._model.getComponenteConnessa(id)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa contenente il nodo {id} ha dimensione: {sizeCC} "))
        self._view.update_page()



