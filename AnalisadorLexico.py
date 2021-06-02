import Tabela_Codigo_morse
import AnalisadorSintatico
class AnalisadorLexico:

    def __init__(self, palavra):
         self.palavra=palavra

    def resultado(self):
     traduz=""
     inicio=Tabela_Codigo_morse
     for umpalavra in self:
          pega =inicio.Tabela_Codigo_morse.codigo_morse(umpalavra)
          if pega != '**':
               traduz=traduz+pega+" "
          else:
               verifica=AnalisadorSintatico
               pega2=verifica.resposta_do_sintatico(umpalavra)
               if pega2 !='*':
                    pega =inicio.Tabela_Codigo_morse.codigo_morse(pega2)
                    traduz=traduz+pega+" "
               else:
                    print("O  CONTEUDO "+ umpalavra + " É DISCONHECIDO")
        
     return traduz



    