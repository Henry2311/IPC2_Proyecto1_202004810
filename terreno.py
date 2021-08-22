
class terreno:

    def __init__(self,nombre,dimM,dimN,iniciox,inicioy,finx,finy,nodos):
        self.nombre = nombre
        self.dimM = dimM
        self.dimN = dimN
        self.iniciox = iniciox
        self.inicioy = inicioy
        self.finx = finx
        self.finy = finy
        self.nodos = nodos
    
    def getNombre(self):
        return self.nombre
    
    def getDimM(self):
        return self.dimN
    
    def getDimN(self):
        return self.dimN
    
    def getIniciox(self):
        return self.iniciox
    
    def getInicioy(self):
        return self.inicioy 
    
    def getFinx(self):
        return self.finx
    
    def getFiny(self):
        return self.finy
    
    def getNodos(self):
        return self.nodos