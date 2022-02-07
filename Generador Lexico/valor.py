class Valor:
    cadena=""
    simbolo=""
    tipo=-1
    extra=""

    def __init__(self,c,s,t,e):
        self.cadena=c
        self.simbolo=s
        self.tipo=t
        self.extra=e
    
    def toString(self):
        aux=self.cadena+"\t"+self.simbolo+"\t"+str(self.tipo)+"\t"+self.extra
        return aux
    
    def getCadena(self):
        return self.cadena
    
    def getSimbolo(self):
        return self.simbolo
    
    def getTipo(self):
        return self.tipo
    
    def getExtra(self):
        return self.extra