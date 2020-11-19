'''
Um homem chamado José é o responsável por ligar e desligar as luzes de um corredor. Cada lâmpada tem seu próprio interruptor que liga e a desliga. 
Inicialmente todas as lâmpadas estão desligadas.
José faz uma coisa peculiar: se existem n lâmpadas no corredor, ele caminha até o fim do corredor e volta n vezes. 
Na iésima caminhada, ele aperta apenas os interruptores aos quais sua posição é divisível por i. 
Ele não aperta nenhum interruptor na volta à sua posição inicial, apenas na ida. A iésima caminhada é definida como ir ao fim do corredor e voltar.
Determine qual é o estado final de cada lâmpada. Está ligada ou desligada?

Link do desafio -> https://dojopuzzles.com/problems/lampadas-no-corredor/
'''

n = int(input('Quantos corredores tem?: '))
def corredor(n):
    lampadas = [True] * n
    for i in range(2, n + 1):
        for j in range(n):
            if (j + 1) % i == 0:
                lampadas[j] = not lampadas[j]
                
    print(lampadas)
    return lampadas

corredor(n)