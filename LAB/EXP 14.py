def alphabeta(d, node, alpha, beta, maxi, v):
    if d == 2:
        return v[node]

    if maxi:
        best = -999
        for i in [0, 1]:
            best = max(best, alphabeta(d+1, node*2+i, alpha, beta, False, v))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for i in [0, 1]:
            best = min(best, alphabeta(d+1, node*2+i, alpha, beta, True, v))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

print(alphabeta(0, 0, -999, 999, True, [3, 5, 2, 9]))
