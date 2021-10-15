states = {
    "R": 0,
    "P": 1,
    "S": 2
}

history = ['R', 'P', 'P', 'S', 'R', 'R', 'S', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R', 'R', 'P']

nhist = list(map(lambda x: states[x], history))

def transition_matrix(transitions):
    n = 1+ max(transitions)

    M = [[0]*n for _ in range(n)]

    for (i,j) in zip(transitions,transitions[1:]):
        M[i][j] += 1

    for row in M:
        s = sum(row)
        if s > 0:
            row[:] = [f/s for f in row]
    return M

m = transition_matrix(nhist)
for row in m: print(' '.join('{0:.2f}'.format(x) for x in row))


print(m[2].index(max(m[2])))