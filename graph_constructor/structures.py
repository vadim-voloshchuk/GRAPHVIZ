# Импорт внешних библиотек
import pandas as pd
import numpy
import networkx as nx
import matplotlib.pyplot as plt

# Импорт внутренних библиотек
import random

# Импорт модулей проекта
# from .common.pereferences import *

class User():
    def __init__(self, nickname, *args):
        self.nickname = nickname

        self.firstname = ""
        self.lastname = ""
        self.patronymic = ""
        self.age = ""
        self.location = ""
        self.phone = ""
        self.email = ""
        self.language = ""
        self.university = ""
        self.work_experience = ""

    def __str__(self):
        return f"Пользователь: {self.nickname}"

    def get_nick(self):
        return self.nickname

class SocialGraph:
    def __init__(self, nodes = []):
        self.nodes = {}
        self.edges = {}

        for i in range(len(nodes)):
            self.nodes[i] = nodes[i]

    def __str__(self):
        return f"Граф содержит {len(self.nodes)} узлов и {len(self.edges)} ребер."

    def read_csv(self, path):
        data = pd.read_csv(path)

        for user_i in data.to_numpy():
            self.nodes[len(self.nodes)] = (User(user_i[7]))

    def add_node(self, user):
        # TODO (V): Сделать систему внутри метода, чтобы пользователь добавлял параметры без инициализации класса User
        self.nodes[len(self.nodes)] = user

    def add_edge(self, id_1, id_2, weight = 0.5, type_c = None):
        # TODO (V): Сделать проверку на существующие id вершин
        assert -1 <= weight <= 1, "Вес связи выходит за установленные границы: [-1, 1]"
        self.edges[len(self.edges)] = {
                'source' : id_1,
                'target': id_2,
                'weight': weight,
                'type': type_c
                }

    def get_nodes(self, table_pd = False, show = False):
        if table_pd:
            raw_table = {
                'index': [],
                'nickname': []
            }

            for i in range(len(self.nodes)):
                raw_table['index'].append(i)
                raw_table['nickname'].append(self.nodes[i].get_nick())

            result = pd.DataFrame(raw_table)

        else:
            result = self.nodes

        if show:
            print(result)

        return result

    # TODO (A): Дописать по анологии с get_nodes
    def get_edges(self, table_pd=False, show=False):
        if table_pd:
            raw_table = {
                'index': [],
                'source': [],
                'target': [],
                'weight': [],
                'type': []
            }

            for i, (edge_id, edge) in enumerate(self.edges.items()):
                raw_table['index'].append(i)
                raw_table['source'].append(edge['source'])
                raw_table['target'].append(edge['target'])
                raw_table['weight'].append(edge['weight'])
                raw_table['type'].append(edge['type'])

            result = pd.DataFrame(raw_table)

        else:
            result = self.edges

        if show:
            print(result)

        return result

    # TODO (A): Реализовать удаление элементов графа (по сути элементов словаря)
    def del_node(self, id):
        if id in self.nodes:
            del self.nodes[id]

            remove_edges = []
            for edge_id, edge in self.edges.items():
                if edge['source'] == id or edge['target'] == id:
                    remove_edges.append(edge_id)

            for edge_id in remove_edges:
                del self.edges[edge_id]

    def del_edge(self, id):
        if id in self.edges:
            del self.edges[id]


    # TODO (V): Дописать правильное обращение к классу User
    # def update_node(self, id, param, value):
    #     self.nodes[id][param] = value

    def update_edge(self, id, param, value):
        self.edges[id][param] = value

    # def draw(self):
    #     plt.figure(figsize=(15, 20))

    #     G_VIS = nx.


if __name__ == "__main__":
    g = SocialGraph()
    g.read_csv('common/test_data/gen_data.csv')
    g.add_edge(3, 4)

    # g.get_nodes(show=True)
    print(g)
