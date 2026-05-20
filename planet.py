from utils import to_number, to_word, to_int

types_list = ("каменная","газовый гигант", "ледяной гигант")

class Planet:
    def __init__(self, name, radius, mass, length, typep, idp):
        self.idp = idp
        self.name = name
        self.radius = radius
        self.mass = mass
        self.length = length
        self.typep = typep
        print("Создана планета " + self.name + " с ID " + str(self.idp))
        
    @property
    def name(self):
        return self._name
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def mass(self):
        return self._mass
    
    @property
    def length(self):
        return self._length
    
    @property
    def typep(self):
        return self._typep
    
    @property
    def idp(self):
        return self._idp
        
    @name.setter
    def name(self, name):
        self._name = to_word(name)
    
    @radius.setter
    def radius(self, radius):
        _n = to_number(radius)
        if _n > 0:
            self._radius = _n
        else:
            self._radius = 0
    
    @mass.setter
    def mass(self, mass):
        _n = to_number(mass)
        if _n > 0:
            self._mass = _n
        else:
            self._mass = 0
    
    @length.setter
    def length(self, length):
        _n = to_number(length)
        if _n > 0:
            self._length = _n
        else:
            self._length = 0
    
    @typep.setter
    def typep(self, typep):
        _s = to_word(typep)
        if _s.lower() in types_list:
            self._typep = _s
        else:
            self._typep = "не установлено"
    
    @idp.setter 
    def idp(self, idp):
        _n = to_int(idp)
        if _n > 0:
            self._idp = _n
        else:
            self._idp = 0

    def __repr__(self):
        s = []
        s.append(str(self.idp))
        s.append(self.name)
        s.append(str(self.radius))
        s.append(str(self.mass))
        s.append(str(self.length))
        s.append(str(self.typep))
        full_s = ";".join(s)
        return full_s

    def __str__(self):
        s = []
        s.append("ID: " + str(self.idp))
        s.append("Название: " + self.name)
        s.append("Радиус: " + str(self.radius) + " м^6")
        s.append("Масса: " + str(self.mass) + " кг^6")
        s.append("Расстояние до Солнца: " + str(self.length) + " м^6")
        s.append("Тип: " + str(self.typep))
        full_s = "\n".join(s)
        return full_s
    
    def __lt__(self, other): # <
        return self.length < other.length
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __del__(self):
        print("Удалена планета " + self.name + " с ID " + str(self.idp))
