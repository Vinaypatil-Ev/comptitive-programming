def shortest_path(dist, s, d):
    if s == d or s == d - 1:
        return dist[s][d]
    short = dist[s][d]
    for i in range(s + 1, d):
        sdist = shortest_path(dist, s, i) + shortest_path(dist, i, d)
        if sdist < short:
            short = sdist
    return short



if __name__ == "__main__":
    dist = [ [0, 15, 80, 90],
         [float("inf"), 0, 40, 50],
         [float("inf"), float("inf"), 0, 70],
         [float("inf"), float("inf"), float("inf"), 0]
        ]
    s = 1
    d = 4
    x = shortest_path(dist, s - 1, d - 1)
    print(f"shortest path from station {s} to {d} is {x}")