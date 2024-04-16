# Classe Cidade que representa um nó
class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionarVizinho(self, vizinho):
        self.vizinhos.append({'cidade': vizinho})

# Função da busca em profundidade
def buscaEmProfundidade(inicio, objetivo):
    pilha = [] 
    visitados = set()

    pilha.append(inicio) # adiciona o nó inicial à pilha
    visitados.add(inicio) # marca o nó inicial como visitado

    while pilha:
        cidade = pilha.pop() # remove o último nó da pilha
        print(f"Visitando a cidade: {cidade.nome}")

        if cidade.nome == objetivo.nome: # se o nó é o objetivo, termina a busca
            print(f"Encontrou o objetivo: {cidade.nome}")
            return

        # Adiciona os vizinhos do nó atual à pilha
        for vizinho in reversed(cidade.vizinhos): # inverte a ordem dos vizinhos para simular a pilha
            cidade_vizinho = vizinho['cidade']
            if cidade_vizinho not in visitados: # se o vizinho ainda não foi visitado
                pilha.append(cidade_vizinho)
                visitados.add(cidade_vizinho) # marca o vizinho como visitado

    print("Caminho não encontrado!")
    return None

# Criação do grafo
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
cidadeArad.adicionarVizinho(cidadeSibiu)
cidadeArad.adicionarVizinho(cidadeTimisoara)
cidadeArad.adicionarVizinho(cidadeZerind)

cidadeZerind.adicionarVizinho(cidadeArad)
cidadeZerind.adicionarVizinho(cidadeOradea)

cidadeOradea.adicionarVizinho(cidadeZerind)
cidadeOradea.adicionarVizinho(cidadeSibiu)

cidadeSibiu.adicionarVizinho(cidadeArad)
cidadeSibiu.adicionarVizinho(cidadeFagaras)
cidadeSibiu.adicionarVizinho(cidadeOradea)
cidadeSibiu.adicionarVizinho(cidadeRimnicuVilcea)

cidadeTimisoara.adicionarVizinho(cidadeArad)
cidadeTimisoara.adicionarVizinho(cidadeLugoj)

cidadeLugoj.adicionarVizinho(cidadeTimisoara)
cidadeLugoj.adicionarVizinho(cidadeMehadia)

cidadeMehadia.adicionarVizinho(cidadeLugoj)
cidadeMehadia.adicionarVizinho(cidadeDobreta)

cidadeDobreta.adicionarVizinho(cidadeMehadia)
cidadeDobreta.adicionarVizinho(cidadeCraiova)

cidadeCraiova.adicionarVizinho(cidadeDobreta)
cidadeCraiova.adicionarVizinho(cidadePitesti)
cidadeCraiova.adicionarVizinho(cidadeRimnicuVilcea)

cidadeRimnicuVilcea.adicionarVizinho(cidadeSibiu)
cidadeRimnicuVilcea.adicionarVizinho(cidadePitesti)
cidadeRimnicuVilcea.adicionarVizinho(cidadeCraiova)

cidadeFagaras.adicionarVizinho(cidadeSibiu)
cidadeFagaras.adicionarVizinho(cidadeBucharest)

cidadePitesti.adicionarVizinho(cidadeRimnicuVilcea)
cidadePitesti.adicionarVizinho(cidadeCraiova)
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

# Busca em profundidade
buscaEmProfundidade(cidadeArad, cidadeBucharest)
