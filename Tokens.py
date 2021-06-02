class Tokens:
    def __init__(self,gravar_resultado):
        self.gravar_resultado=gravar_resultado
    def gravar_informacao(self):
        lista=[]
        v=""
        lista.append(self)
        for list in lista:
            v=v+list
        return v
        