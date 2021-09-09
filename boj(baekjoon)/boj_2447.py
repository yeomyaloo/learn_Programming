n = int(input())

def get_star(n):
    if n == 1:
        return ['*']
    
    stars = get_star(n//3)
    star_list = []
    
    for star in stars:
        star_list.append(star*3)
    for star in stars:
        star_list.append(star + ' '*(n//3) + star)
    for star in stars:
        star_list.append(star*3)
        
    return star_list

print('\n'.join(get_star(n)))
