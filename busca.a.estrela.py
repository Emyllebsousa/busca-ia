import math

# Classe Cidade que representa um nó
class Cidade:
    def __init__(self, nome, distancia_objetivo):
        self.nome = nome
        self.distancia_objetivo = distancia_objetivo
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho, distancia):
        self.vizinhos.append({'cidade': vizinho, 'custo': distancia})

# Função de busca A*
def busca_a_estrela(inicio, objetivo):
    abertos = [inicio] # Nós ainda não avaliados
    fechados = [] # Nós já avaliados
    caminho = {inicio.nome: {'custo': 0, 'pai': None}} # O custo para chegar à cidade inicial é 0 e não tem pai

    # Função de custo total estimado
    def custo_total_estimado(cidade):
        return cidade.distancia_objetivo + caminho[cidade.nome]['custo']

    while abertos:
        # Encontrando a cidade com o menor custo total estimado
        cidade_atual = min(abertos, key=lambda cidade: custo_total_estimado(cidade))

        if cidade_atual == objetivo:
            caminho_final = []
            while cidade_atual:
                caminho_final.insert(0, cidade_atual.nome)
                cidade_atual = caminho[cidade_atual.nome]['pai']
            return caminho_final

        # Removendo a cidade atual da lista de nós abertos
        abertos.remove(cidade_atual)
        fechados.append(cidade_atual)

        for vizinho in cidade_atual.vizinhos:
            if vizinho['cidade'] not in fechados: # Se o vizinho ainda não foi avaliado
                custo_atualizado = caminho[cidade_atual.nome]['custo'] + vizinho['custo']

                # Se o vizinho ainda não está na lista de nós abertos, ou se o novo custo é menor
                if vizinho['cidade'] not in abertos or custo_atualizado < caminho[vizinho['cidade'].nome]['custo']:
                    caminho[vizinho['cidade'].nome] = {'custo': custo_atualizado, 'pai': cidade_atual} # Atualiza o custo e o pai do vizinho
                    if vizinho['cidade'] not in abertos:
                        abertos.append(vizinho['cidade']) # Adiciona o vizinho à lista de nós abertos
    return None

# Criação do grafo
cidade_arad = Cidade("Arad", 366)
cidade_zerind = Cidade("Zerind", 374)
cidade_oradea = Cidade("Oradea", 380)
cidade_sibiu = Cidade("Sibiu", 253)
cidade_timisoara = Cidade("Timisoara", 329)
cidade_lugoj = Cidade("Lugoj", 244)
cidade_mehadia = Cidade("Mehadia", 241)
cidade_dobreta = Cidade("Dobreta", 242)
cidade_craiova = Cidade("Craiova", 160)
cidade_rimnicu_vilcea = Cidade("Rimnicu Vilcea", 193)
cidade_fagaras = Cidade("Fagaras", 178)
cidade_pitesti = Cidade("Pitesti", 98)
cidade_bucharest = Cidade("Bucharest", 0)
cidade_giurgiu = Cidade("Giurgiu", 77)
cidade_urziceni = Cidade("Urziceni", 80)
cidade_hirsova = Cidade("Hirsova", 151)
cidade_eforie = Cidade("Eforie", 161)
cidade_vaslui = Cidade("Vaslui", 199)
cidade_iasi = Cidade("Iasi", 226)
cidade_neamt = Cidade("Neamt", 234)

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

# Execução da busca A*
resultado = busca_a_estrela(cidade_arad, cidade_bucharest)

if resultado is not None:
    print("Caminho encontrado:")
    print(resultado)
else:
    print("Caminho não encontrado.")
