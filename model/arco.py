from dataclasses import dataclass

from model.artObject import ArtObject


@dataclass
class Arco: #nodi sono oggetti interi
    o1 : ArtObject
    o2 : ArtObject
    peso : int