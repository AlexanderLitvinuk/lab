from utils import to_number, to_word, to_int

types_list = ("каменная","газовый гигант", "ледяной гигант")

class Planet:
    def __init__(self, name, radius, mass, length, typep, idp):
        self.set_id(idp)
        self.set_name(name)
        self.set_radius(radius)
        self.set_mass(mass)
        self.set_length(length)
        self.set_type(typep)
        self.set_id(idp)
        
        
    
    def set_name(self, name):
        self.name = to_word(name)
        
    def set_radius(self, radius):
        _n = to_number(radius)
        if _n > 0:
            self.radius = _n
        else:
            self.radius = 0
            
    def set_mass(self, mass):
        _n = to_number(mass)
        if _n > 0:
            self.mass = _n
        else:
            self.mass = 0
            
    def set_length(self, length):
        _n = to_number(length)
        if _n > 0:
            self.length = _n
        else:
            self.length = 0
    def set_type(self, typep):
        _s = to_word(typep.lower())
        if _s in types_list:
            self.typep = _s
        else:
            self.typep = "не установлено"
            
    def set_id(self, idp):
        _n = to_int(idp)
        if idp > 0:
            self.idp = _n
        else:
            self.idp = 0
            
            
    
    def get_name(self):
        return self.name

    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_length(self):
        return self.length
    
    def get_type(self):
        return self.typep
    
    def get_id(self):
        return self.idp
    
    
    def __str__(self):
        s = []
        s.append("ID: " + str(self.idp))
        s.append("Название: " + self.name)
        s.append("Радиус: " + str(self.radius) + " м^6")
        s.append("Масса: " + str(self.mass) + " кг^6")
        s.append("Расстояние до Солнца: " + str(self.length) + "м^6")
        s.append("Тип: " + str(self.typep))
        full_s = "\n".join(s)
        return full_s

nig = Planet("[", "1fas12", "dsa12", "dadsajj3223,32.", "23", 13.2)
print(nig)