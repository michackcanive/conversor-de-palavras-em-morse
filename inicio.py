import AnalisadorLexico
import os
import Tokens


n= AnalisadorLexico
i="S" 
iniciotokens=Tokens
m=""
k=""
total=""
lista=[]
while i=="S":
    os.system("cls")
    
    palavra=input("\nDIGITE A PALAVRA OU LETRA PARA TRADUZIR : ").upper()
    pega=n.AnalisadorLexico.resultado(palavra)
    m=iniciotokens.Tokens.gravar_informacao(pega)
    k=palavra
    total="PALAVRA INSERIDA "+k+" -------- EM CODIGO MORSE = "+m +"\n"
    q="PALAVRA INSERIDA "+k+" -------- TRADUÇÃO EM MORSE = "+m +"\n"
    lista.append(total) 
    
    print( "      ____________TOKENS_____________\n \n")
    for list in lista:
         print(list)
    
    print("__________________________________________")    
    print(q)
        
        
        
        
        
        
        
        
        
    print("\nAINDA PRENTENDES FAZER A CONVERSÃO ?")
    s=input("\n  S-SIM       N-NÃO ").upper()
    i=s
    
