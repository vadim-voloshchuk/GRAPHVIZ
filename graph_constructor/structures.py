# Импорт внешних библиотек
import pandas as pd
import numpy

# Импорт внутренних библиотек
import random

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

class SocialGraph:
    def __init__(self, nodes = []):
        self.nodes = {}
        self.edges = []

        for i in range(len(nodes)):
            self.nodes[i] = nodes[i]

    def __str__(self):
        return f"Граф содержит {len(self.nodes)} узлов и {len(self.edges)} ребер."

    def read_csv(self, path):
        data = pd.read_csv(path)

        print(data.to_numpy())

        for user_i in data.to_numpy():
            self.nodes[len(self.nodes)] = (User(user_i[7]))

    def add_node(self, user):
        self.nodes[len(self.nodes)] = user

    def add_edge(self):
        pass

if __name__ == "__main__":
    g = SocialGraph()
    g.read_csv('../common/test_data/gen_data.csv')

    print(g.nodes)
