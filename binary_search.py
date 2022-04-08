tests = []

test = {
    'input':{
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3 
}

tests.append(test)

#EDGE CASES
tests.append({
    'input':{
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
 })
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

def first_instance(cards, query, pos): 
    
    if cards[pos] == query:

        if pos - 1 >= 0 and cards[pos -1] == query:
            return 'left'
        else:
            return 'found'
    else:
        if cards[pos] > query:
            return 'right'
        else:
            return 'left'
    

def locate_number(cards, query):
    lo, hi = 0, len(cards) - 1  

    while lo <= hi:
        pos = (lo + hi) // 2
        result = first_instance(cards, query, pos)

        if result == 'found':
            return pos
        elif result == 'right':
            lo = pos + 1
        elif result == 'left':
            hi = pos - 1
    return -1

for i in range(0, len(tests)):
    result = locate_number(tests[i]['input']['cards'], tests[i]['input']['query'])
    ex_result = tests[i]['output']
    if result == ex_result:
        print("Success")
    else:
        print("Failed")