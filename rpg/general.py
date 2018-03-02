import copy


class MapChip:
    def __init__(self, init_estimate, x, y, state):
        self.cost = 0
        self.estimate = init_estimate
        self.ans = list()
        self.x = x
        self.y = y
        self.state = 1 if state else 0

    @property
    def score(self):
        return self.cost + self.estimate


def min2(m):
    mi = m[0][0]
    for mlen in m:
        for i in mlen:
            if (i.score - (i.state * 10000)) < (mi.score - (mi.state * 10000)):
                mi = i
    return mi

# A*で最短経路を返す


def a_star(m, sx, sy, gx, gy):
    cm = list()
    len_m = len(m)
    len_m0 = len(m[0])
    for y in range(len_m):
        cm.append(list())
        for x in range(len_m0):
            cm[y].append(MapChip(max(abs(x - gx), abs(y - gy)),  x, y,
                                 x == sx and y == sy))
    now = cm[sy][sx]
    koho = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while True:
        for i in range(4):
            koho_x = now.x + koho[i][0]
            koho_y = now.y + koho[i][1]
            if koho_x >= 0 and koho_x < len_m0 and koho_y >= 0 and koho_y < len_m and cm[koho_y][koho_x].state >= 0:
                if not m[koho_y][koho_x].type == 'obstacle':
                    cm[koho_y][koho_x].state = 1
                    cm[koho_y][koho_x].cost = now.cost + 1
                    cm[koho_y][koho_x].ans = copy.copy(now.ans)
                    cm[koho_y][koho_x].ans.append(i)
                    if koho_x == gx and koho_y == gy:
                        return cm[koho_y][koho_x].ans
        now.state = -1
        now = min2(cm)


if __name__ == "__main__":
    print(a_star([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, 0, 1, 2))
