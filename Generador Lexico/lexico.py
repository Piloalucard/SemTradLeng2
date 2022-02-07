import imp
from valor import Valor

class Lexico:
    _fuente = ""
    _ind = 0
    _simb=""
    _lista=[]

    def __init__(self,f):
        self._fuente=f+"$"
        self._ind=0

    def getLista(self):
        return self._lista


    def setFuente(self,f):
        self._ind=0
        self._fuente=f+"$"

    def obtLexico(self):
        auxcad="Nombre\tSimbolo\tTipo\tExtra\n"
        auxcad+="-----------------------------------\n"
        for i in self._lista:
            auxcad+=i.toString()+"\n"
        return auxcad

    def __tipoSimb(self,tipo):
        simbologia=["Ident.","Entero","Real","Cadena","Tipo",
        "Op.Suma","Op.Mul","Op.Rel.","Op.Or","Op.And","Op.Not","Op.Igual"]
        cadena=simbologia[tipo]
        return  cadena
    
    def leerSimb(self):
        for i in self._fuente:
            if self.__verLetra(i) or self.__verNum(i) or ord(i)==46:
                self._simb+=i
            else:
                msc=self._simb
                newValor=Valor("Error","Error",-1,"")
                band = False
                if msc=="int" or msc=="float" or msc=="void" or msc=="double" or msc=="string" or msc=="char":
                    newValor = Valor(self._simb,self.__tipoSimb(4),4," int,float,void")
                    band=True
                elif msc=="if":
                    newValor = Valor(self._simb,self._simb,19,"")
                    band=True
                elif msc=="while":
                    newValor = Valor(self._simb,self._simb,20,"")
                    band=True
                elif msc=="return":
                    newValor = Valor(self._simb,self._simb,21,"")
                    band=True
                elif msc=="else":
                    newValor = Valor(self._simb,self._simb,22,"")
                    band=True
                elif msc=="<=" or msc ==">=":
                    newValor = Valor(self._simb,self.__tipoSimb(7),7,"<,<=,>=,>")
                    band=True
                elif msc=="||":
                    newValor = Valor(self._simb,self.__tipoSimb(8),8,"||")
                    band=True
                elif msc=="&&":
                    newValor = Valor(self._simb,self.__tipoSimb(9),9,"&&")
                    band=True
                elif msc=="==" or msc =="!=":
                    newValor = Valor(self._simb,self.__tipoSimb(11),11,"==,!=")
                    band=True
                else:
                    try:
                        valorAux=self._lista[-1]
                        ant=valorAux.getCadena()
                        if ant=="string" and self._evitarEsp(self._simb):
                            newValor = Valor(self._simb,self.__tipoSimb(3),3,"")
                            band=True
                        elif len(self._simb) > 1:
                            self.__obtIdentif()
                        elif self._evitarEsp(self._simb):
                            self.__obtIdentif()
                    except:
                        if len(self._simb) > 1:
                            self.__obtIdentif()
                        elif self._evitarEsp(self._simb):
                            self.__obtIdentif()
                
                if newValor.getTipo() != -1:
                    self._lista.append(newValor)
                    band=False
               

                self._simb=i
                band2=False

                if band==False:
                    if i == "+" or i =="-":
                        newValor = Valor(self._simb,self.__tipoSimb(5),5,"+,-")
                        band=True
                    elif i == "*" or i =="/":
                        newValor = Valor(self._simb,self.__tipoSimb(6),6,"*,/")
                        band=True
                    elif i=="<" or i ==">":
                        newValor = Valor(self._simb,self.__tipoSimb(7),7,"<,<=,>=,>")
                        band=True
                        band2=True
                    elif i=="!":
                        newValor = Valor(self._simb,self.__tipoSimb(10),10,"!")
                        band=True
                        band2=True
                    elif i == ";":
                        newValor = Valor(self._simb,self._simb,12,"")
                        band=True
                    elif i == ",":
                        newValor = Valor(self._simb,self._simb,13,"")
                        band=True
                    elif i == "(":
                        newValor = Valor(self._simb,self._simb,14,"")
                        band=True
                    elif i == ")":
                        newValor = Valor(self._simb,self._simb,15,"")
                        band=True
                    elif i == "{":
                        newValor = Valor(self._simb,self._simb,16,"")
                        band=True
                    elif i == "}":
                        newValor = Valor(self._simb,self._simb,17,"")
                        band=True
                    elif i == "=":
                        newValor = Valor(self._simb,self._simb,18,"")
                        band=True
                        band2=True
                    elif i == "$":
                        newValor = Valor(self._simb,self._simb,23,"")
                        band=True

                    

                if band2 and self._fuente[self._ind+1]=="=":
                    self._simb+=self._fuente[self._ind+1]
                    pass
                elif band:
                    self._lista.append(newValor)
                    del newValor
                    self.__resetSimb()
                else:
                    self.__resetSimb()

               

                
            self._ind+=1

        
    def _evitarEsp(self,i):  
        try: 
            if self.__verLetra(i) or self.__verNum(i) or ord(i)==46:
                return True
        except:
            pass
        return False
                

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
    




