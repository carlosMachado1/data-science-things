# -*- coding: utf-8 -*-


def number_of_friends(user):
    """quantos amigos o usuário tem?"""
    return len(user["friends"])


users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3),
    (2, 3), (3, 4), (4, 5), (5, 6),
    (5, 7), (6, 8), (7, 8), (8, 9)
]

for user in users:
    user["friends"] = []

for i, j in friendships:
    # isso funciona porque users[i] é o usuário cuja id é i
    users[i]["friends"].append(users[j])  # adiciona i como um amigo de j
    users[j]["friends"].append(users[i])  # adiciona j como um amigo de i

# tamanho da lista friend_ids
total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
# tamanho da lista de usuários
avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]


num_friends_by_id = sorted(
    num_friends_by_id,  # lista que será ordenada
    key=lambda user: user[1],  # vai ordernar pelo numero de amigos
    reverse=True  # do maior para o menor
)
