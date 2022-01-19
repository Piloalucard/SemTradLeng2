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

class Lexico:
    _fuente = ""
    _ind = 0
    _simb=""
    _lista=[]

    def __init__(self,f):
        self._fuente=f+"$"

    def setFuente(self,f):
        self._ind=0
        self._fuente=f

    def obtLexico(self):
        auxcad="Nombre\tSimbolo\tTipo\tExtra\n"
        auxcad+="-----------------------------------\n"
        for i in self._lista:
            auxcad+=i.toString()+"\n"
        return auxcad

    def __tipoSimb(self,tipo):
        simbologia=["Ident.","Entero","Real"]
        cadena=simbologia[tipo]
        return  cadena
    
    def leerSimb(self):
        for i in self._fuente:
            if self.__verLetra(i) or self.__verNum(i) or ord(i)==46:
                self._simb+=i
            else:
                self.__obtIdentif()
                
                self._simb=i
                if i == "$":
                    newValor = Valor(self._simb,self._simb,23,"")
                    self._lista.append(newValor)
                    del newValor

                self.__resetSimb()

        

                

    def __obtIdentif(self):
        try:
            int(self._simb)
            tipo=self.__tipoSimb(1)
            newValor = Valor(self._simb,tipo,1,"")
            self._lista.append(newValor)
            del newValor
            self.__resetSimb()
        except:
            try:
                float(self._simb)
                tipo=self.__tipoSimb(2)
                newValor = Valor(self._simb,tipo,2,"")
                self._lista.append(newValor)
                del newValor
                self.__resetSimb()
            except:
                tipo=self.__tipoSimb(0)
                newValor = Valor(self._simb,tipo,0,"")
                self._lista.append(newValor)
                del newValor
                self.__resetSimb()



    def __resetSimb(self):
        self._simb=""

    
    def __verLetra(self,i):
        if ord(i) >= 65 and ord(i) <= 122:
            return True
        else:
            return False
    
    def __verNum(self,i):
        if ord(i) >= 48 and ord(i) <= 57:
            return True
        else:
            return False
    




