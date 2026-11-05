from time import perf_counter

def gerar_subconjuntos(lista):
    resultado = [[]]
    for elemento in lista:
        novos = [sub + [elemento] for sub in resultado]
        resultado.extend(novos)
    return resultado

print("=" * 65)
print("DESAFIO EXTRA: Algoritmo O(2^n) - Gerar Todos os Subconjuntos")
print("=" * 65)
print(f"{'Tamanho N':<12} | {'Subconjuntos Gerados (2^n)':<28} | {'Tempo Gasto':<15}")
print("-" * 65)

tamanhos_teste = [5, 10, 15, 20, 22, 24]

for n in tamanhos_teste:
    dados = list(range(n))
    
    t_inicio = perf_counter()
    subconjuntos = gerar_subconjuntos(dados)
    t_fim = perf_counter()
    
    tempo = t_fim - t_inicio
    qtd = len(subconjuntos)
    
    print(f"{n:<12} | {qtd:<28,d} | {tempo:<10.5f} s")

print("-" * 65)
print("\n[ONDE ELE SE TORNA INVIÁVEL?]")
print("1. Para N = 24, já foram criados mais de 16 MILHÕES de subconjuntos na memória RAM!")
print("2. Para N = 30, seriam gerados mais de 1 BILHÃO de subconjuntos (exigiria ~30 GB de RAM, travando a máquina).")
print("3. Para N = 1.000 (o que usamos no O(1) e O(n)), 2^1000 é maior que o número de átomos no universo visível!")
