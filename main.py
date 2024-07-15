def hill_climbing(initial_state, evaluate, get_neighbors):
    current_state = initial_state
    current_score = evaluate(current_state)

    while True:
        neighbors = get_neighbors(current_state)
        best_neighbor = current_state
        best_score = current_score

        for neighbor in neighbors:
            neighbor_score = evaluate(neighbor)
            if neighbor_score < best_score:
                best_neighbor = neighbor
                best_score = neighbor_score

        if best_score >= current_score:
            break

        current_state = best_neighbor
        current_score = best_score

    return current_state

def evaluate(state):
    correct_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    state_matrix = [
        state[:3],
        state[3:6],
        state[6:]
    ]

    score = 0
    for i in range(3):
        for j in range(3):
            value = state_matrix[i][j]
            if value != 0:
                correct_i, correct_j = divmod(value - 1, 3)
                score += abs(i - correct_i) + abs(j - correct_j)

    return score

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    zero_i, zero_j = divmod(zero_index, 3)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for di, dj in directions:
        new_i, new_j = zero_i + di, zero_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            neighbor = state[:]
            neighbor[zero_index], neighbor[new_i * 3 + new_j] = neighbor[new_i * 3 + new_j], neighbor[zero_index]
            neighbors.append(neighbor)

    return neighbors

initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
solution = hill_climbing(initial_state, evaluate, get_neighbors)
print('פתרון:', solution)