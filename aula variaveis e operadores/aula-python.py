print("oii")

print(7+4)
print("7 + 4")
print("7" + "4") # CONCATENAÇÃO DE STRINGS
-----------------------------------------------------------------
# variáveis
nome = "júlia" #str
print(nome)
idade = 18 # int
peso = 51 # float
print(nome ,idade , peso)

print(f"oiiii, {nome}!!!")

#INPUT - SIMULAÇÃO DE FORMS NO CMD
nome = input("Digite o seu nome:")
idade = input("Digite sua idade")

print(nome,idade)

ano_nascimento = 2007
ano_atual = 2026
idade = ano_atual - ano_nascimento
--------------------------------------------------------
#algoritimo que recebe numero inteiro positivo N
#imprime na tela todos os numeros de 1 a n.

n = int(input("Digite um num inteiro n: "))

cont = 1

while cont <= n:
    print(cont)
    cont += 1
--------------------------------------------------
# while
notaA =  float(input("Digite a primeira nota: "))
while notaA < 0 or notaA > 10:
    print("A nota deve estar entre 0 e 10")
    notaA = float(input("Digite novamente:"))



notaB = float(input("Digite a segunda nota:"))
while notaB < 0 or notaB > 10:
    print("A nota deve estar entre 0 e 10::")
    notaB = float(input("Digite a nota novamente:"))

media = (notaA + notaB) / 2
print(media)

# função 

def verificar_nota(nota):
 while nota < 0 or nota > 10:
     print("A noa deve estar eentre 0 e 10:")
     nota = float(input("Digite a nota novamente;"))
     return nota
------------------------------------------------------------------

# ATIVIDADE 3

qtd_musica = int(input("Quantas musicas vc tem na playlist (db): "))

for i in range(qtd_musica):
    print(f"Música {i}")

# laços alinhados

for i in range(0, 4):
    for j in range(0, 3, 2):
        print(f"i:{i},j:{j}")








