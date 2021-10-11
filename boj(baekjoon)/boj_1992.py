n = int(input())

m = [list(map(int, input())) for _ in range(n)]

def quadtree(x, y, n):
    # n = 1, 하나의 픽셀만 볼 경우,
    if(n == 1):
        return str(m[x][y])
    
    result = []
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색이 다르면, 
            if(m[i][j] != m[x][y]):
                # append와 extend의 차이는
                # extend는 list, tuple, dict 등의 iterable object를
                # python list의 끝에 append 해주는 것.
                result.append('(')
                result.extend(quadtree(x, y, n//2))
                result.extend(quadtree(x, y + n//2, n//2))
                result.extend(quadtree(x + n//2, y, n//2))
                result.extend(quadtree(x + n//2, y + n//2, n//2))
                result.append(')')
                return result
            
    return str(m[x][y])
    
print(''.join(quadtree(0, 0, n)))
