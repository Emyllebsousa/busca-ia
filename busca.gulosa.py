# Classe Cidade que representa um nó
class Cidade:
    def __init__(self, nome, distanciaObjetivo):
        self.nome = nome
        self.distanciaObjetivo = distanciaObjetivo
        self.vizinhos = []

    def adicionarVizinho(self, vizinho):
        self.vizinhos.append({'cidade': vizinho})

# Função de busca gulosa
def buscaGulosa(inicio, objetivo):
    atual = inicio
    caminho = [inicio.nome]  # Inicia o caminho com a cidade inicial

    while atual != objetivo:
        menorDistancia = float('inf')  # Inicializa com infinito para garantir que a primeira cidade visitada será a mais próxima do objetivo
        proximaCidade = None

        for vizinho in atual.vizinhos:  # Itera sobre os vizinhos da cidade atual
            if vizinho['cidade'].distanciaObjetivo < menorDistancia:
                menorDistancia = vizinho['cidade'].distanciaObjetivo
                proximaCidade = vizinho['cidade']

        if proximaCidade is None:
            return None

        atual = proximaCidade
        caminho.append(atual.nome)

    return caminho

# Criação do grafo
cidadeArad = Cidade("Arad", 366)
cidadeZerind = Cidade("Zerind", 374)
cidadeOradea = Cidade("Oradea", 380)
cidadeSibiu = Cidade("Sibiu", 253)
cidadeTimisoara = Cidade("Timisoara", 329)
cidadeLugoj = Cidade("Lugoj", 244)
cidadeMehadia = Cidade("Mehadia", 241)
cidadeDobreta = Cidade("Dobreta", 242)
cidadeCraiova = Cidade("Craiova", 160)
cidadeRimnicuVilcea = Cidade("Rimnicu Vilcea", 193)
cidadeFagaras = Cidade("Fagaras", 178)
cidadePitesti = Cidade("Pitesti", 98)
cidadeBucharest = Cidade("Bucharest", 0)
cidadeGiurgiu = Cidade("Giurgiu", 77)
cidadeUrziceni = Cidade("Urziceni", 80)
cidadeHirsova = Cidade("Hirsova", 151)
cidadeEforie = Cidade("Eforie", 161)
cidadeVaslui = Cidade("Vaslui", 199)
cidadeIasi = Cidade("Iasi", 226)
cidadeNeamt = Cidade("Neamt", 234)

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

# Execução da busca gulosa
resultado = buscaGulosa(cidadeArad, cidadeBucharest)
if resultado is not None:
    print("Caminho encontrado:", ' -> '.join(resultado))
else:
    print("Caminho não encontrado!")
