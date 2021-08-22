class posicion:

    def __init__(self, indexX, indexY, gasolina):
        self.indexX = indexX
        self.indexY = indexY
        self.gasolina = gasolina

    #metodos getter y setter
    def getIndexX(self):
        return self.indexX
    
    def getIndexY(self):
        return self.indexY
    
    def getGasolina(self):
        return self.gasolina
    
    def setIndexX(self, indexX):
        self.indexX = indexX
    
    def setIndexY(self, indexY):
        self.indexY = indexY
    
    def setGasolina(self, gasolina):
        self.gasolina = gasolina