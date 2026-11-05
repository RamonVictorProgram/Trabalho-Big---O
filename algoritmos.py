from time import perf_counter
import matplotlib.pyplot as plt

tamanhos_n = (1000, 5000, 10000, 20000)

def constante_o1(lista):
    return lista[0]

def linear_on(lista):
    soma = 0 

    for numero in lista:
        soma += numero
    return soma


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        elif lista[meio] < alvo:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1

def quadratica_on2(lista):
    contador = 0

    for i in lista:

        for j in lista:
            contador += 1

    return contador


tempos_o1 = []
tempos_ologn = []
tempos_on = []
tempos_on2 = []

print("Iniciando as medições de tempo...\n")


for n in tamanhos_n:
    print(f"Testando para N = {n}...")
    
    
    lista = list(range(n))

    
    t_inicio = perf_counter()
    constante_o1(lista)
    t_fim = perf_counter()
    tempos_o1.append(t_fim - t_inicio)

    
    t_inicio = perf_counter()
    busca_binaria(lista, -1)
    t_fim = perf_counter()
    tempos_ologn.append(t_fim - t_inicio)

  
    t_inicio = perf_counter()
    linear_on(lista)
    t_fim = perf_counter()
    tempos_on.append(t_fim - t_inicio)

    
    t_inicio = perf_counter()
    quadratica_on2(lista)
    t_fim = perf_counter()
    tempos_on2.append(t_fim - t_inicio)

print("\nMedições concluídas com sucesso!")


print("Gerando os gráficos comparativos...")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


ax1.plot(tamanhos_n, tempos_o1, marker='o', label="O(1) - Constante")
ax1.plot(tamanhos_n, tempos_ologn, marker='s', label="O(log n) - Busca Binária")
ax1.plot(tamanhos_n, tempos_on, marker='^', label="O(n) - Linear")
ax1.plot(tamanhos_n, tempos_on2, marker='d', label="O(n^2) - Quadrático", color='red')
ax1.set_title("Comparação Geral (Todas as Curvas)")
ax1.set_xlabel("Tamanho da Entrada (N)")
ax1.set_ylabel("Tempo de Execução (segundos)")
ax1.legend()
ax1.grid(True)


ax2.plot(tamanhos_n, tempos_o1, marker='o', label="O(1) - Constante")
ax2.plot(tamanhos_n, tempos_ologn, marker='s', label="O(log n) - Busca Binária")
ax2.plot(tamanhos_n, tempos_on, marker='^', label="O(n) - Linear", color='green')
ax2.set_title("Zoom nos Mais Rápidos: O(1), O(log n) e O(n)")
ax2.set_xlabel("Tamanho da Entrada (N)")
ax2.set_ylabel("Tempo de Execução (segundos)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig("grafico_complexidade.png", dpi=300)
print("Gráfico salvo como 'grafico_complexidade.png'!")


