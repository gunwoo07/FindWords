import sys


def find_word(alphas, a, b, word):
    directions = []
    x = len(alphas[0])
    y = len(alphas)

    # direction1
    coordinates = []
    check = True
    if b + 1 >= len(word):
        for i in range(len(word)):
            if alphas[b - i][a] != word[i]:
                check = False
                break
            coordinates.append([a, b - i])
    
        if check:
            directions.append([1, coordinates])

    # direction3
    coordinates = []
    check = True
    if x - a >= len(word):
        for i in range(len(word)):
            if alphas[b][a + i] != word[i]:
                check = False
                break
            coordinates.append([a + i, b])
    
        if check:
            directions.append([3, coordinates])
                
    # direction5
    coordinates = []
    check = True
    if y - b >= len(word):
        for i in range(len(word)):
            if alphas[b + i][a] != word[i]:
                check = False
                break
            coordinates.append([a, b + i])

        if check:
            directions.append([5, coordinates])

    # direction7
    coordinates = []
    check = True
    if a + 1 >= len(word):
        for i in range(len(word)):
            if alphas[b][a - i] != word[i]:
                check = False
                break
            coordinates.append([a - i, b])
    
        if check:
            directions.append([7, coordinates])

    # direction2
    coordinates = []
    check = True
    if b + 1 >= x - a:
        if x - a >= len(word):
            for i in range(len(word)):
                if alphas[b - i][a + i] != word[i]:
                    check = False
                    break
                coordinates.append([a + i, b - i])   
            
            if check:
                directions.append([2, coordinates])

    else:
        if b + 1 >= len(word):
            for i in range(len(word)):
                if alphas[b - i][a + i] != word[i]:
                    check = False
                    break
                coordinates.append([a + i, b - i])   
            
            if check:
                directions.append([2, coordinates])

    # direction4
    coordinates = []
    check = True
    if y - b >= x - a:
        if x - a >= len(word):
            for i in range(len(word)):
                if alphas[b + i][a + i] != word[i]:
                    check = False
                    break
                coordinates.append([a + i, b + i])   
            
            if check:
                directions.append([4, coordinates])

    else:
        if y - b >= len(word):
            for i in range(len(word)):
                if alphas[b + i][a + i] != word[i]:
                    check = False
                    break
                coordinates.append([a + i, b + i])   
            
            if check:
                directions.append([4, coordinates])

    # direction6
    coordinates = []
    check = True
    if y - b >= a + 1:
        if a + 1 >= len(word):
            for i in range(len(word)):
                if alphas[b + i][a - i] != word[i]:
                    check = False
                    break
                coordinates.append([a - i, b + i])   
            
            if check:
                directions.append([6, coordinates])

    else:
        if y - b >= len(word):
            for i in range(len(word)):
                if alphas[b + i][a - i] != word[i]:
                    check = False
                    break
                coordinates.append([a - i, b + i])   
            
            if check:
                directions.append([6, coordinates])

    # direction8
    coordinates = []
    check = True
    if b + 1 >= a + 1:
        if a + 1 >= len(word):
            for i in range(len(word)):
                if alphas[b - i][a - i] != word[i]:
                    check = False
                    break
                coordinates.append([a - i, b - i])   
            
            if check:
                directions.append([8, coordinates])

    else:
        if b + 1 >= len(word):
            for i in range(len(word)):
                if alphas[b - i][a - i] != word[i]:
                    check = False
                    break
                coordinates.append([a - i, b - i])   
            
            if check:
                directions.append([8, coordinates])

    return directions


def search(alphas, word):
    for b in range(len(alphas)):
        for a in range(len(alphas[0])):
            if alphas[b][a] == word[0]:
                directions = find_word(alphas, a, b, word)
                if len(directions) > 0:
                    return directions


def main():
    with open('quiz') as f:
        data = f.read().split('\n')

    alphas = []

    for d in data:
        alphas.append(list(d))

    word_list = ['case', 'confident', 'experience', 'familiar']

    for word in word_list:
        a = search(alphas, word)
        print(f'=========={word}==========')
        for i in range(len(a)):
            print(f'direction: {a[i][0]}\n{a[i][1]}')
        print('')
    

main()