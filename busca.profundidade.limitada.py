# Classe Cidade que representa um nó
class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionarVizinho(self, vizinho):
        self.vizinhos.append({'cidade': vizinho})

# Função de busca em profundidade limitada
def buscaEmProfundidadeLimitada(inicio, objetivo, limiteProfundidade):
    pilha = []
    visitados = set()

    pilha.append({'no': inicio, 'profundidade': 0}) # adiciona o nó inicial à pilha com profundidade 0
    visitados.add(inicio) # marca o nó inicial como visitado

    while pilha:
        atual = pilha.pop() # remove o último nó da pilha

        no = atual['no']
        profundidade = atual['profundidade']

        print(f"Visitando a cidade: {no.nome}")

        if no.nome == objetivo.nome:
            print(f"Encontrou o objetivo: {no.nome}")
            return True

        # Verifica se a profundidade atual é maior que o limite
        if profundidade >= limiteProfundidade:
            continue

        # Adiciona os vizinhos do nó atual à pilha
        for vizinho in reversed(no.vizinhos): # inverte a ordem dos vizinhos para simular a pilha
            cidade_vizinha = vizinho['cidade']
            if cidade_vizinha not in visitados: # se o vizinho ainda não foi visitado
                pilha.append({'no': cidade_vizinha, 'profundidade': profundidade + 1})
                visitados.add(cidade_vizinha) # marca o vizinho como visitado

    return False

#Grafo
cidadeArad = Cidade("Arad")
cidadeZerind = Cidade("Zerind")
cidadeOradea = Cidade("Oradea")
cidadeSibiu = Cidade("Sibiu")
cidadeTimisoara = Cidade("Timisoara")
cidadeLugoj = Cidade("Lugoj")
cidadeMehadia = Cidade("Mehadia")
cidadeDobreta = Cidade("Dobreta")
cidadeCraiova = Cidade("Craiova")
cidadeRimnicuVilcea = Cidade("Rimnicu Vilcea")
cidadeFagaras = Cidade("Fagaras")
cidadePitesti = Cidade("Pitesti")
cidadeBucharest = Cidade("Bucharest")
cidadeGiurgiu = Cidade("Giurgiu")
cidadeUrziceni = Cidade("Urziceni")
cidadeHirsova = Cidade("Hirsova")
cidadeEforie = Cidade("Eforie")
cidadeVaslui = Cidade("Vaslui")
cidadeIasi = Cidade("Iasi")
cidadeNeamt = Cidade("Neamt")
# Adicionando os vizinhos
cidadeArad.adicionarVizinho(cidadeTimisoara)
cidadeArad.adicionarVizinho(cidadeSibiu)
cidadeArad.adicionarVizinho(cidadeZerind)

cidadeZerind.adicionarVizinho(cidadeArad)
cidadeZerind.adicionarVizinho(cidadeOradea)

cidadeOradea.adicionarVizinho(cidadeSibiu)
cidadeOradea.adicionarVizinho(cidadeZerind)

cidadeSibiu.adicionarVizinho(cidadeArad)
cidadeSibiu.adicionarVizinho(cidadeRimnicuVilcea)
cidadeSibiu.adicionarVizinho(cidadeFagaras)
cidadeSibiu.adicionarVizinho(cidadeOradea)

cidadeTimisoara.adicionarVizinho(cidadeArad)
cidadeTimisoara.adicionarVizinho(cidadeLugoj)

cidadeLugoj.adicionarVizinho(cidadeMehadia)
cidadeLugoj.adicionarVizinho(cidadeTimisoara)

cidadeMehadia.adicionarVizinho(cidadeDobreta)
cidadeMehadia.adicionarVizinho(cidadeLugoj)

cidadeDobreta.adicionarVizinho(cidadeCraiova)
cidadeDobreta.adicionarVizinho(cidadeMehadia)

cidadeCraiova.adicionarVizinho(cidadeDobreta)
cidadeCraiova.adicionarVizinho(cidadePitesti)
cidadeCraiova.adicionarVizinho(cidadeRimnicuVilcea)

cidadeRimnicuVilcea.adicionarVizinho(cidadeSibiu)
cidadeRimnicuVilcea.adicionarVizinho(cidadePitesti)
cidadeRimnicuVilcea.adicionarVizinho(cidadeCraiova)

cidadeFagaras.adicionarVizinho(cidadeSibiu)
cidadeFagaras.adicionarVizinho(cidadeBucharest)

cidadePitesti.adicionarVizinho(cidadeCraiova)
cidadePitesti.adicionarVizinho(cidadeRimnicuVilcea)
cidadePitesti.adicionarVizinho(cidadeBucharest)

cidadeBucharest.adicionarVizinho(cidadeFagaras)
cidadeBucharest.adicionarVizinho(cidadePitesti)
cidadeBucharest.adicionarVizinho(cidadeGiurgiu)
cidadeBucharest.adicionarVizinho(cidadeUrziceni)

cidadeGiurgiu.adicionarVizinho(cidadeBucharest)

cidadeUrziceni.adicionarVizinho(cidadeBucharest)
cidadeUrziceni.adicionarVizinho(cidadeHirsova)
cidadeUrziceni.adicionarVizinho(cidadeVaslui)

cidadeHirsova.adicionarVizinho(cidadeUrziceni)
cidadeHirsova.adicionarVizinho(cidadeEforie)

cidadeEforie.adicionarVizinho(cidadeHirsova)

cidadeVaslui.adicionarVizinho(cidadeUrziceni)
cidadeVaslui.adicionarVizinho(cidadeIasi)

cidadeIasi.adicionarVizinho(cidadeVaslui)
cidadeIasi.adicionarVizinho(cidadeNeamt)

cidadeNeamt.adicionarVizinho(cidadeIasi)

# Busca em profundidade limitada
resultado = buscaEmProfundidadeLimitada(cidadeArad, cidadeZerind, 5)

if resultado:
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado!")
