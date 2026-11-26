class Equipo:
    def __init__(self):
        self._miembros = []

    def anadir(self, nombre):
        self._miembros.append(nombre)

    def __len__(self):
        return len(self._miembros)

    def __contains__(self, nombre):
        return nombre in self._miembros

    def __iter__(self):
        return iter(self._miembros)

    def __repr__(self):
        return f"Equipo: {self._miembros}"

    def __eq__(self, otro):
        if not isinstance(otro, Equipo):
            return NotImplemented
        return (self._miembros) == (otro._miembros)

    
a = Equipo()
a.anadir("manuel")
a.anadir("antonio")
a.anadir("paco")

print(a)

b = Equipo()
b.anadir("manuel1")

print(a == b)