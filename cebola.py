#!/bin/python3

pepino = "Isso é uma string"
idade = 12
dolar = 3.88

alho = ["arroz", "feijão", "pão", "pate", "churrasco", "hotdog", "feijoada", "parmegiana"]
#alho.pop()
# print("o segundo elemento é {}".format(alho[2]))
# print("o terceiro elemento é {}".format(alho[3]))
# del(alho[2])
# print("o segundo elemento é {}".format(alho[2]))
# print("o terceito elemento é {}".format(alho[3]))
# print(type("oi"))
#print(alho[>= começo: < final:passo])

cachorro_list = [['Totó', 'Fubá', 'Pulguinha', 'Cleiton', 'Godofredo', 'Astolfo'],
    ['Vira lata', 'Pastor alemao', 'Pug', 'salsicha', 'labrador']]

cachorro_dict_str = {
    "Nome": ['Totó', 'Fubá', 'Pulguinha', 'Cleiton', 'Godofredo', 'Astolfo'],
    "Raça": ['Vira lata', 'Pastor alemao', 'Pug', 'salsicha', 'labrador']
    }

cachorro_dict_int = {
    0: ['Totó', 'Fubá', 'Pulguinha', 'Cleiton', 'Godofredo', 'Astolfo'],
    1: ['Vira lata', 'Pastor alemao', 'Pug', 'salsicha', 'labrador']
}
# print(cachorro_list[0])
# print(cachorro_dict_int[0])
# print(cachorro_dict_str["Nome"])

# print(cachorro_dict_str.get('Raça'))
# print(cachorro_dict_str.clear())
# print(cachorro_dict_str.keys())
# print(cachorro_dict_str.values())

# for i in cachorro:
#    print(i)
# for i in cachorro_dict_str["Nome"]:
#     for j in cachorro_dict_str["Raça"]:
#         print("O dog {} é da raça {}".format(i,j))

# Mostrar for com zip()
# for i, j in zip(cachorro_dict_str["Nome"], cachorro_dict_str["Raça"]):
#     print("O dog {} é da raça {}".format(i,j))


# idade = 15

# if idade > 18:
#     print('Maior de idade')
# elif idade == 18:
#     print('18 anos')
# else:
#     print('Menor')

# while(idade < 20):
#     print('Menor')
#     idade += 1

nome = 'João'
n_trab = 412
valor_hora = 10.25

#Escreva um programa que leia o nome de um funcionário,
#seu número de horas trabalhadas, o valor que recebe por hora
#e calcula o salário desse funcionário.
#A seguir, mostre o nome e o salário do funcionário. Se o valor for
#maior que 998,00 imprimir a quantidade de salarios minimos que ele
#ganha Ex: 1.23 salários mínimos

# if n_trab*valor_hora > 998:
#     print("O funcionário {} ganha {} salários {} mínimos.".format(
#         nome, round(n_trab*valor_hora/998, 2), "oláaaa"))

# for i in range(100):
#     print(i)



# class Sala():
#     def __init__(self, nome, capacidade):
#         self.nome = nome
#         self.capacidade = capacidade
    
#     def retorna_capacidade(self):
#         return "A sala {} comporta {} pessoas.".format(self.nome, self.capacidade)

# sala1 = Sala("1A", 200)

# print(sala1.retorna_capacidade())

# function nome_da_minha_funcao(param1, param2){
#     //codigo
# }

# def minha_funcao(param1, param2):
#     print(param1, param2)

# #minha_funcao("OI, ", "Eric")


# usuario_corr = "Eric"
# senha_corr = 1234
# contador = 0

# while contador != 3:
#     usuario = input("Digite o usuario: ")
#     senha = input("Digite a senha: ")
#     if usuario == usuario_corr:
#         if int(senha) == senha_corr:
#             print("Usuário autenticado")
#         else:
#             print("Senha incorreta")
#     else:
#         print("Dados incorretos")
#     contador += 1

# if contador == 3:
#     print("Você excedeu as tentativas")

# USUÁRIO INSERE UM USUÁRIO E SENHA
# SE USUÁRIO E SENHA ESTIVEREM CORRETOS, IMPRIMIR “PASSOU!”
# SE ESTIVER ERRADO, IMPRIMIR “ERRADO” E PEDIR OS DADOS NOVAMENTES
# PERMITIR NO MÁXIMO 3 TENTATIVAS
# SE EXCEDER AS 3 TENTATIVAS IMPRIMIR “EXCEDEU NÚMERO DE TENTATIVAS”

# diferente é != 
# and e or ou


#virtualenv

#criar virtualenv:
# virtualenv banana (windows 'talvez')
# python -m venv banana (linux e mac)

#ativar virtualenv:
# source banana/Scripts/activate (windows 'talvez')
# source banana/bin/activate (linux e mac)

#instalar django (depois de ativar a banana):
# pip install django

class Animal():
    olho = True

    def andar(self):
        print("Sou um animal feliz e estou andando...")

    def __init__(self, nome, perna, especie):
        self.nome = nome
        self.perna = perna
        self.especie = especie

gato = Animal("Bichano", 4, "Felino")

class Gato(Animal):
    def __init__(self, nome, perna, especie, bigode, tamanho):
        super().__init__(nome, perna, especie)
        self.bigode = bigode
        self.tamanho = tamanho

    def miar(self):
        print("Miau")

gatinho = Gato("Garfield", 4, "Felino", 6, "grande")
gatinho.miar()
gatinho.andar()

class PetShop():
    def __init__(self, preco_banho, preco_tosa):
        self.preco_banho = preco_banho
        self.preco_tosa = preco_tosa
    
    def banho(self, animal):
        if animal.especie == "cachorro":
            print("O valor do banho para um {} é {}".format(animal.especie, self.preco_banho))
        else:
            print("não damos banho no seu bicho")
    
    def tosa(self, animal):
        if animal.especie == "cachorro":
            print("O valor da tosa para um {} é {}".format(animal.especie, self.preco_tosa))
        else:
            print("não tosamos o seu bicho")

dog = Animal("Totó", 4, "cachorro")
obichaofeliz = PetShop(30, 40)
print(obichaofeliz.banho(dog))
print(obichaofeliz.tosa(dog))