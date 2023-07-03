import random

pergunta = int(input("Quantas senhas você quer que sejam geradas?"))
#Aqui o usuário vai ser perguntado quantos senhas ele quer gerar.
if (pergunta >= 1):
#Aqui vai fazer uma verificação, caso o valor seja igual ou maior que 1 o programa vai executar se não o programa vai mostrar uma mensagem de erro.
    for i in range(pergunta):
    #Aqui o laço vai gerar a quantidade de perguntas que ele quer e mostrar na tela uma por uma.
        caracteres_especias = random.choices('!@#$%&*')
        #A função random.choices vai escolher aleatoriamente entre esses caracteres e vai escolher um deles para compor a senha ou senhas.
        numeros = str(random.randint(0, 1000))
        #A função random.randint vai gerar um número aleátorio entre 0 a 1000 para compor a senha ou senhas.
        letras = random.choices('abcdefghijklmnopqrstuvwxyz', k=5)
        #A função random.choices vai escolher aleatoriamente entre esses caracteres e vai escolher cinco deles para compor a senha ou senhas.
        password = ''.join(list(numeros) + letras + list(caracteres_especias))
        #Aqui vai concatenar todos caracteres em uma única string, que vai ser a senha ou senhas.
        print(password)
        #Aqui vai printar a senha ou senhas na telas.
else:
    print("Erro! infelismente não foi possível executar o programa")

