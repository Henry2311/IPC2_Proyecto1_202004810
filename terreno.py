
class terreno:

    def __init__(self,nombre,dimM,dimN,iniciox,inicioy,finx,finy,nodos,gas,Rx,Ry):
        self.nombre = nombre
        self.dimM = dimM
        self.dimN = dimN
        self.iniciox = iniciox
        self.inicioy = inicioy
        self.finx = finx
        self.finy = finy
        self.nodos = nodos
        self.gas = gas
        self.Rx = Rx
        self.Ry = Ry
    
    def getNombre(self):
        return self.nombre
    
    def getDimM(self):
        return self.dimM
    
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
    
    def getGas(self):
        return self.gas
    
    def getRX(self):
        return self.Rx

    def getRY(self):
        return self.Ry

    def setGas(self, gas):
        self.gas = gas
    
    def setRX(self,Rx):
        self.Rx = Rx
    
    def setRY(self,Ry):
        self.Ry = Ry