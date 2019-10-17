def equation(a, b, c, n):
    possibilites = []
    for x in range(0, n+1):
        for y in range(0, n+1):
            for z in range(0, n+1):
                if (a * x + b * y + c * z == 100):
                    possibilites.append({
                        'x': x,
                        'y': y,
                        'z': z
                    })
    return possibilites

if __name__ == '__main__':
    print(equation(10, 10, 10, 10))
