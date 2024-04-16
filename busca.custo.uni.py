import math

# Classe Cidade que representa um nó
class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho, distancia):
        self.vizinhos.append({'cidade': vizinho, 'custo': distancia})

# Função de busca de custo uniforme
def busca_custo_uniforme(origem, objetivo):
    borda = [{'cidade': origem, 'caminho': [origem], 'custo': 0}]
    visitados = set()

    while borda:
        borda.sort(key=lambda x: x['custo']) # Ordena a borda com base no custo acumulado

        cidade_atual = borda.pop(0) # Escolhe o nó com menor custo e remove da borda
        cidade = cidade_atual['cidade']
        caminho = cidade_atual['caminho']
        custo = cidade_atual['custo']

        if cidade == objetivo:
            return {'caminho': caminho, 'custo': custo}

        visitados.add(cidade)

        for vizinho in cidade.vizinhos:
            cidade_vizinho = vizinho['cidade']
            custo_vizinho = vizinho['custo']
            if cidade_vizinho not in visitados:
                novo_caminho = caminho + [cidade_vizinho] # Caminho acumulado até o momento
                novo_custo = custo + custo_vizinho # Custo acumulado até o momento
                borda.append({'cidade': cidade_vizinho, 'caminho': novo_caminho, 'custo': novo_custo})

    return None

# Criação do grafo
cidade_arad = Cidade("Arad")
cidade_zerind = Cidade("Zerind")
cidade_oradea = Cidade("Oradea")
cidade_sibiu = Cidade("Sibiu")
cidade_timisoara = Cidade("Timisoara")
cidade_lugoj = Cidade("Lugoj")
cidade_mehadia = Cidade("Mehadia")
cidade_dobreta = Cidade("Dobreta")
cidade_craiova = Cidade("Craiova")
cidade_rimnicu_vilcea = Cidade("Rimnicu Vilcea")
cidade_fagaras = Cidade("Fagaras")
cidade_pitesti = Cidade("Pitesti")
cidade_bucharest = Cidade("Bucharest")
cidade_giurgiu = Cidade("Giurgiu")
cidade_urziceni = Cidade("Urziceni")
cidade_hirsova = Cidade("Hirsova")
cidade_eforie = Cidade("Eforie")
cidade_vaslui = Cidade("Vaslui")
cidade_iasi = Cidade("Iasi")
cidade_neamt = Cidade("Neamt")

# Adicionando os vizinhos
cidade_arad.adicionar_vizinho(cidade_sibiu, 140)
cidade_arad.adicionar_vizinho(cidade_timisoara, 118)
cidade_arad.adicionar_vizinho(cidade_zerind, 75)

cidade_zerind.adicionar_vizinho(cidade_arad, 75)
cidade_zerind.adicionar_vizinho(cidade_oradea, 71)

cidade_oradea.adicionar_vizinho(cidade_zerind, 71)
cidade_oradea.adicionar_vizinho(cidade_sibiu, 151)

cidade_sibiu.adicionar_vizinho(cidade_arad, 140)
cidade_sibiu.adicionar_vizinho(cidade_fagaras, 99)
cidade_sibiu.adicionar_vizinho(cidade_oradea, 151)
cidade_sibiu.adicionar_vizinho(cidade_rimnicu_vilcea, 80)

cidade_timisoara.adicionar_vizinho(cidade_arad, 118)
cidade_timisoara.adicionar_vizinho(cidade_lugoj, 111)

cidade_lugoj.adicionar_vizinho(cidade_timisoara, 111)
cidade_lugoj.adicionar_vizinho(cidade_mehadia, 70)

cidade_mehadia.adicionar_vizinho(cidade_lugoj, 70)
cidade_mehadia.adicionar_vizinho(cidade_dobreta, 75)

cidade_dobreta.adicionar_vizinho(cidade_mehadia, 75)
cidade_dobreta.adicionar_vizinho(cidade_craiova, 120)

cidade_craiova.adicionar_vizinho(cidade_dobreta, 120)
cidade_craiova.adicionar_vizinho(cidade_pitesti, 138)
cidade_craiova.adicionar_vizinho(cidade_rimnicu_vilcea, 146)

cidade_rimnicu_vilcea.adicionar_vizinho(cidade_sibiu, 80)
cidade_rimnicu_vilcea.adicionar_vizinho(cidade_pitesti, 97)
cidade_rimnicu_vilcea.adicionar_vizinho(cidade_craiova, 146)

cidade_fagaras.adicionar_vizinho(cidade_sibiu, 99)
cidade_fagaras.adicionar_vizinho(cidade_bucharest, 211)

cidade_pitesti.adicionar_vizinho(cidade_rimnicu_vilcea, 97)
cidade_pitesti.adicionar_vizinho(cidade_craiova, 138)
cidade_pitesti.adicionar_vizinho(cidade_bucharest, 101)

cidade_bucharest.adicionar_vizinho(cidade_fagaras, 211)
cidade_bucharest.adicionar_vizinho(cidade_pitesti, 101)
cidade_bucharest.adicionar_vizinho(cidade_giurgiu, 90)
cidade_bucharest.adicionar_vizinho(cidade_urziceni, 85)

cidade_giurgiu.adicionar_vizinho(cidade_bucharest, 90)

cidade_urziceni.adicionar_vizinho(cidade_bucharest, 85)
cidade_urziceni.adicionar_vizinho(cidade_hirsova, 98)
cidade_urziceni.adicionar_vizinho(cidade_vaslui, 142)

cidade_hirsova.adicionar_vizinho(cidade_urziceni, 98)
cidade_hirsova.adicionar_vizinho(cidade_eforie, 86)

cidade_eforie.adicionar_vizinho(cidade_hirsova, 86)

cidade_vaslui.adicionar_vizinho(cidade_urziceni, 142)
cidade_vaslui.adicionar_vizinho(cidade_iasi, 92)

cidade_iasi.adicionar_vizinho(cidade_vaslui, 92)
cidade_iasi.adicionar_vizinho(cidade_neamt, 87)

cidade_neamt.adicionar_vizinho(cidade_iasi, 87)

# Execução da busca de custo uniforme
resultado = busca_custo_uniforme(cidade_sibiu, cidade_bucharest)
# resultado= função (cidade inicial, objetivo)

if resultado is not None:
    caminho = [cidade.nome for cidade in resultado['caminho']]
    print("Menor caminho:", caminho)
    print("Custo total:", resultado['custo'])
else:
    print("Não foi possível encontrar um caminho.")
