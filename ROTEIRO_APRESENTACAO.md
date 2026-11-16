# Grupo 4 — Eficiência e Complexidade de Algoritmos
## Resumo da Lógica do Código e Roteiro Completo de Apresentação

---

# 🧠 PARTE 1: RESUMO DA LÓGICA DO CÓDIGO

### 1. Arquivo `algoritmos.py`

#### A. Função `constante_o1(lista)` — $O(1)$ (Tempo Constante)
* **Código:** `return lista[0]`
* **Lógica:** Como a lista está alocada de forma contígua na memória do computador, o processador calcula o endereço do índice `0` instantaneamente.
* **Complexidade:** $O(1)$. Não importa se a lista tem 10 ou 10 milhões de elementos, a máquina só faz 1 operação direta de leitura e termina.

#### B. Função `linear_on(lista)` — $O(n)$ (Tempo Linear)
* **Código:** Um laço `for numero in lista:` somando `soma += numero` e retornando `soma` no final.
* **Lógica:** Para somar todos os elementos, o computador é obrigado a visitar cada uma das $N$ posições da lista, exatamente uma vez.
* **Complexidade:** $O(n)$. O número de passos e o tempo crescem proporcionalmente ao tamanho da lista.

#### C. Função `busca_binaria(lista, alvo)` — $O(\log n)$ (Tempo Logarítmico)
* **Código:** Usa ponteiros `inicio = 0` e `fim = len(lista) - 1`. Dentro do `while inicio <= fim`, calcula `meio = (inicio + fim) // 2`.
  * Se `lista[meio] == alvo`, achou.
  * Se `lista[meio] < alvo`, descarta o lado esquerdo movendo `inicio = meio + 1`.
  * Se `lista[meio] > alvo`, descarta o lado direito movendo `fim = meio - 1`.
* **Lógica:** Divide o problema ao meio a cada iteração. Para $1.000.000$ de números, resolve em no máximo 20 passos!
* **Pulo do gato nos testes:** O teste busca pelo número `-1` (que não existe na lista). Isso garante que o algoritmo execute todas as divisões possíveis até o fim, medindo o **pior caso real**.

#### D. Função `quadratica_on2(lista)` — $O(n^2)$ (Tempo Quadrático)
* **Código:** Dois laços aninhados: `for i in lista:` e, dentro dele, `for j in lista:` incrementando `contador += 1`.
* **Lógica:** Para cada um dos $N$ itens percorridos no laço externo, o laço interno percorre todos os $N$ itens novamente.
* **Complexidade:** $O(n^2)$. Total de passos: $N \times N = N^2$. Para $N = 20.000$, foram executadas $400.000.000$ de operações!

#### E. Medição de Tempo com `perf_counter`
* **Código:**
  ```python
  t_inicio = perf_counter()
  funcao(lista)
  t_fim = perf_counter()
  tempo = t_fim - t_inicio
  ```
* **Lógica:** `perf_counter` é o relógio de mais alta resolução disponível no Python para medir tempos curtos com precisão de frações de microssegundos.

#### F. Gráficos Comparativos com `matplotlib`
* Cria dois subplots lado a lado (`plt.subplots(1, 2)`):
  * **Gráfico 1 (Geral):** Plota todas as 4 curvas juntas. Mostra como a curva parabólica vermelha do $O(n^2)$ sobe vertiginosamente e "esconde" as demais.
  * **Gráfico 2 (Zoom):** Remove a curva quadrática e foca apenas em $O(1)$, $O(\log n)$ e $O(n)$, evidenciando a reta diagonal do $O(n)$ e a estabilidade das outras duas.
* Salva a imagem final em `grafico_complexidade.png`.

---

### 2. Arquivo `desafio_o2n.py` (Desafio Exponencial)

#### Função `gerar_subconjuntos(lista)` — $O(2^n)$
* **Código:**
  ```python
  resultado = [[]]
  for elemento in lista:
      novos = [sub + [elemento] for sub in resultado]
      resultado.extend(novos)
  ```
* **Lógica:** A cada novo elemento adicionado, pegamos todos os subconjuntos existentes e criamos novas versões com aquele elemento incluído. Isso dobra a quantidade de conjuntos a cada passo ($2^n$).
* **Onde se torna inviável?** Entre **$N = 25$ e $N = 30$**.
  * Com $N = 24$, já gerou mais de 16,7 milhões de listas na RAM em 6 segundos.
  * Com $N = 30$, geraria mais de 1 bilhão de listas, consumindo mais de 30 GB de memória e travando o computador por `MemoryError`.

---

# 🎤 PARTE 2: ROTEIRO DA APRESENTAÇÃO (PASSO A PASSO)

---

### ⏱️ Momento 1: Abertura (30 a 45 segundos)
> *"Boa noite, professor e colegas. Nosso trabalho é sobre o **Grupo 4: Eficiência e Complexidade de Algoritmos**.*  
> *O objetivo principal do projeto foi analisar na prática como o tempo de execução dos algoritmos se comporta à medida que aumentamos a quantidade de dados processados ($N$), correlacionando os testes empíricos com a notação matemática **Big-O**."*

---

### ⏱️ Momento 2: Teoria vs. Prática (1 minuto)
> *"Antes de vermos o código, vale esclarecer uma dúvida clássica: **o que o Big-O mede?**  
> * **Na teoria:** O Big-O não mede segundos de relógio, mas sim a **quantidade de passos lógicos (operações da CPU)** no pior caso. Afinal, medir em segundos dependeria da potência da máquina.  
> * **No nosso projeto:** Usamos o `time.perf_counter` do Python para medir o tempo real em segundos e **comprovar que o relógio da máquina acompanha exatamente as curvas teóricas do Big-O**."*

---

### ⏱️ Momento 3: Os 4 Algoritmos & Exemplos do Cotidiano (2 a 3 minutos)

1. **$O(1)$ — Tempo Constante:**
   > *"No código, acessamos o primeiro item da lista (`lista[0]`).  
   > **Analogia do cotidiano:** É como **pegar o prato do topo de uma pilha limpa**. Não importa se a pilha tem 3 pratos ou 1.000 pratos: você estende a mão e pega o de cima em um único movimento instantâneo."*

2. **$O(\log n)$ — Tempo Logarítmico (Busca Binária):**
   > *"No código, dividimos sucessivamente a lista ordenada ao meio.  
   > **Analogia do cotidiano:** É como **procurar uma palavra em um dicionário de papel**. Você não lê da página 1 até o fim; você abre no meio. Se a letra que procura vem depois, descarta toda a metade esquerda. A cada folheada, metade do problema vai embora."*

3. **$O(n)$ — Tempo Linear:**
   > *"No código, somamos todos os itens percorrendo a lista com um laço `for`.  
   > **Analogia do cotidiano:** É como **procurar uma meia numa gaveta desorganizada**. Como não há ordem, você é obrigado a olhar meia por meia. Se tiver 100 meias, você fará até 100 checagens. O tempo cresce em linha reta junto com a quantidade de itens."*

4. **$O(n^2)$ — Tempo Quadrático:**
   > *"No código, usamos dois laços `for` aninhados para comparar pares.  
   > **Analogia do cotidiano:** É como **uma festa com $N$ convidados onde cada pessoa precisa cumprimentar todas as outras com um aperto de mão individual**. Se forem 10 pessoas, são 100 apertos de mão; se forem 100 pessoas, são 10.000 cumprimentos! O trabalho se multiplica por ele mesmo."*

---

### ⏱️ Momento 4: Demonstração dos Gráficos (1 a 2 minutos)
*(Projetar a imagem `grafico_complexidade.png`)*

> *"Aqui está o gráfico real gerado pelos nossos testes com entradas de 1.000 até 20.000 elementos:  
> * **No gráfico da esquerda (Geral):** Reparem na curva vermelha do $O(n^2)$. Com $N = 20.000$, foram **400 milhões de operações**, levando cerca de 15 segundos. Ela subiu tão rápido que fez as outras curvas parecerem coladas no zero.  
> * **No gráfico da direita (Zoom):** Por isso, fizemos um segundo gráfico removendo o quadrático. Nele podemos ver com clareza o $O(n)$ subindo em uma reta diagonal perfeita, e o $O(1)$ e o $O(\log n)$ quase imperceptíveis lá embaixo, provando sua extrema velocidade."*

---

### ⏱️ Momento 5: Desafio Extra: $O(2^n)$ (1 minuto)
> *"Para o desafio extra, implementamos a geração de subconjuntos de uma lista (Power Set), que é um algoritmo exponencial $O(2^n)$.  
> A cada novo elemento adicionado, a quantidade de resultados **dobra**:  
> * Com $N = 10$, foram 1.024 subconjuntos.  
> * Com $N = 20$, passou de 1 milhão.  
> * Com $N = 24$, foram **16,7 milhões de subconjuntos** criados na memória, levando mais de 6 segundos.  
> **Onde ele se torna inviável?** Entre **$N = 25$ e $N = 30$**. Se tentássemos rodar com $N = 30$, seriam mais de 1 bilhão de listas, o que exigiria mais de 30 GB de RAM e travaria o computador por falta de memória (`MemoryError`)."*

---

### ⏱️ Momento 6: O Gran Finale — E com 1 Bilhão ($10^9$) de Elementos? (1 minuto)
*(O ponto alto da apresentação para surpreender a turma e o professor)*:

> *"Para finalizar, estimamos quanto tempo cada um dos nossos algoritmos levaria para processar **1 bilhão de elementos** em um computador moderno que executa cerca de 1 bilhão de operações por segundo:  
> 1. **$O(1)$**: Faz 1 operação $\rightarrow$ **1 nanossegundo** (instantâneo).  
> 2. **$O(\log n)$**: Faz cerca de 30 operações $\rightarrow$ **30 nanossegundos** (instantâneo).  
> 3. **$O(n)$**: Faz 1 bilhão de operações $\rightarrow$ **cerca de 1 segundo**.  
> 4. **$O(n^2)$**: Fará $(10^9)^2 = 10^{18}$ operações. Dividindo por 1 bilhão de operações por segundo, teríamos 1 bilhão de segundos... o que dá nada menos que **31,7 ANOS na frente do computador!**  
> 5. **$O(2^n)$**: O tempo ultrapassaria em muitas vezes a idade de todo o universo."*

---

### ⏱️ Momento 7: Conclusão Final
> *"A conclusão do nosso grupo é que entender a complexidade de algoritmos não é um mero exercício teórico: é o que define se o seu sistema responde a um usuário em frações de segundo ou se ele passará décadas travado.  
> Muito obrigado a todos, estamos abertos a perguntas!"*

---

### 💡 Dicas para Responder as Perguntas do Professor:

1. **"Por que você buscou o `-1` na busca binária?"**  
   * **Resposta:** *"Porque a lista só contém valores positivos de $0$ até $N-1$. Ao procurar um item inexistente, garantimos que a busca percorra todas as subdivisões possíveis até o final, cronometrando o pior caso real."*

2. **"Se a busca binária é tão rápida, por que não a usamos em todas as situações?"**  
   * **Resposta:** *"Porque ela exige que os dados estejam previamente ordenados. Ordenar uma lista custa $O(n \log n)$, então a busca binária só compensa se a lista for consultada várias vezes."*
