#Variaveis globais 
Livros = []
Alunos = []
Bibliotecas = []

#Luiz define as classes: Livro , Aluno , Biblioteca. Afonso programa a classe Livro , João : Aluno , Isaac : Biblioteca Miguel faz o menu.
class Aluno:
    def __init__(self, nome, matricula, lista_de_livros_emprestados = []):
        self.nome = nome
        self.matricula = matricula
        self.lista_de_livros_emprestados = lista_de_livros_emprestados

#Isaac
class Biblioteca:
    def __init__(self , nome): #Inicialização
        self.nome = nome
        
    #Variaveis da classe , o catalogo de livros vai conter os livros adicionados apartir de uma função dentro desta classe , mesmo para os alunos.
    catalogoDeLivros = [] 
    cadastroDeAlunos = []
    
    def consultarLivros(self):
        for livro in self.catalogoDeLivros:
            print("Titulo do livro: " , livro.titulo , " , Autor do livro: " , livro.autor , " , Codigo do livro: " , livro.codigo_do_livro , ", Disponibilidade: " , livro.disponibilidade)
            
    def consultarAlunos(self):
        for aluno in self.cadastroDeAlunos:
            print("Nome do aluno: " , aluno.nome , " , Matricula do aluno" , aluno.matricula , " , Livros emprestados: ")
            for livro in aluno.lista_de_livros_emprestados:
                print(livro.titulo)

    def cadastrarAluno(self , pAluno): #Leva um aluno como parametro e adiciona-o no cadastroDeAlunos
        self.cadastroDeAlunos.append(pAluno)
        
    def adicionarLivro(self , pLivro): #Adiciona um livro ao catalogo de livros da biblioteca , que um aluno pode pegar emprestado.
        self.catalogoDeLivros.append(pLivro)
        
    def emprestarLivro(self , pAluno , pLivro):
        if pLivro.disponibilidade == True:
            if len(pAluno.lista_de_livros_emprestados) < 3:
                pLivro.disponibilidade = False
                pAluno.lista_de_livros_emprestados.append(pLivro)
        else:
            print("O livro não esta disponivel.")
            
        
#Afonso , e luiz define as propriedades
class Livro:
    def __init__(self, titulo, autor, codigo_do_livro):
        self.titulo = titulo
        self.autor = autor
        self.codigo_do_livro = codigo_do_livro
        self.disponibilidade = True #disponibilidade , true = emprestado , false = disponivel.
    
def registarLivro(): #para registar um objeto da Class Livro
    nomelivro = input("Qual o nome do livro?: ")
    autor = input("Qual o nome do autor?: ")
    codigo_do_livro = int(input("Escreva o codigo do livro"))
    livro = Livro(nomelivro, autor, codigo_do_livro)
    Livros.append(livro)

#João
def registarAluno():
    nomealuno = input("Qual o nome do aluno: ")
    Matricula = input("Qual a sua matricula: ")
    print("O aluno é o ", nomealuno, "e sua matricula é ", Matricula)
    AlunoCriado = Aluno(nomealuno , Matricula)
    Alunos.append(AlunoCriado)
    
def consultarLivros():
    for livro in Livros:
        print("titulo:", livro.titulo)
        print(" , autor:", livro.autor)
        print(" , codigo do livro:", livro.codigo_do_livro)
        print(" , disponibilidade:", livro.disponibilidade)
 
def consultarAlunos():
    for aluno in Alunos:
        print("Nome : ", aluno.nome , " , Matricula : " , aluno.matricula)
        print("Livros emprestados : ")
        for livro in aluno.lista_de_livros_emprestados:
            print("Titulo do livro: " , livro.titulo) #ez fix
            
def mostrarRelatorio():
    print("--- RELATORIO ---")
    print("TODOS OS LIVROS EMPRESTADOS :")
    for aluno in Alunos:
        for livro in aluno.lista_de_livros_emprestados:
            print("TITULO : " , livro.titulo , "," , "AUTOR : " , livro.autor , "CODIGO DO LIVRO : " , "," , livro.codigo_do_livro , "DISPONIBILIDADE : " , livro.disponibilidade , "," , "EMPRESTADO A : " , aluno.nome)
            
#Operações automaticas do programa.
#Criações principais
BibliotecaDaEscola = Biblioteca("Biblioteca da escola")
Bibliotecas.append(BibliotecaDaEscola)
Metro2033 = Livro("Metro 2033" , "Dmitry Glukhovsky" , 2345295725125)
APeste = Livro("A Peste" , "Albert Camus" , 78217603014928)
Livros.append(Metro2033)
Livros.append(APeste)
IgorRamos = Aluno("Igor Ramos" , "ATEC" , list() )
JoaquimLeao = Aluno("Joaquim Leandro" , "EPBJC" , list() )
Alunos.append(IgorRamos)
Alunos.append(JoaquimLeao)

#Da biblioteca da escola
BibliotecaDaEscola.cadastrarAluno(JoaquimLeao)
BibliotecaDaEscola.adicionarLivro(APeste)


#Miguel #Façam função de criar biblioteca
while True:
    print("-----Menu-----") #Placeholder asf
    print("Criar novo Aluno - 1 , Cadastrar Aluno Biblioteca - 2")
    print("Criar novo Livro - 3 , Adicionar Livro ao Catalogo Biblioteca - 4")
    print("Consultar Livros Criados - 5 , Consultar Livros no catalogo - 6")
    print("Consultar Alunos Criados - 7 , Consultar Alunos cadastrados - 8")
    print("Pegar livro emprestado - 9")
    print("Sair - 0")
    op=input()
    if op == "1":
        registarAluno()
    elif op == "2":
        
        index = 0
        for aluno in Alunos:
            print("Nome : " , aluno.nome , "Numero : " , index)
            index = index + 1
        print("Entre o numero do aluno que quer cadastrar na biblioteca da escola :")
        numero = int(input())
        
        
        BibliotecaDaEscola.cadastrarAluno(Alunos[numero])
        
    elif op == "3":
        registarLivro()
    elif op == "4":
           
        index = 0
        for livro in Livros:
            print("Nome : " , livro.titulo , "Numero : " , index)
            index = index + 1
        print("Entre o numero do livro que quer adicionar ao catalogo da biblioteca :")
        numero = int(input())
        
        
        BibliotecaDaEscola.adicionarLivro(Livros[numero])
           
    elif op == "5":
        consultarLivros()
    elif op == "6":
        BibliotecaDaEscola.consultarLivros() 
    elif op == "7":
        consultarAlunos()
    elif op == "8":
        BibliotecaDaEscola.consultarAlunos()
    elif op == "9":
        
        index = 0
        for aluno in BibliotecaDaEscola.cadastroDeAlunos:
            print("Nome : " , aluno.nome , "Numero : " , index)
            index = index + 1
        print("Entre o numero do aluno que quer que pegue um livro emprestado :")
        numero = int(input())
        
        indexl = 0
        for livro in BibliotecaDaEscola.catalogoDeLivros:
            print("Titulo : " , livro.titulo , "Disponibilidade : " , livro.disponibilidade , "Numero : " , indexl)
            indexl = indexl + 1
        print("Entre o numero do livro que voce quer que o aluno pegue emprestado : ")
        numerol = int(input())
        
        BibliotecaDaEscola.emprestarLivro(BibliotecaDaEscola.cadastroDeAlunos[numero] , BibliotecaDaEscola.catalogoDeLivros[numerol])
        
    elif op =="0":
        mostrarRelatorio()
        input()
        break 