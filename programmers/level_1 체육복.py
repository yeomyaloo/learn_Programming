def solution(n, lost, reserve):
    setReserve = set(reserve) - set(lost)
    setLost = set(lost) - set(reserve)
    for r in setReserve:
        if r - 1 in setLost:
            setLost.remove(r-1)

        elif r + 1 in setLost:
            setLost.remove(r+1)
            
    return n - len(setLost)
            
