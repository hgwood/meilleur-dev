def update(a_dict, another_dict):
    new_dict = a_dict.copy()
    new_dict.update(another_dict)
    return new_dict

def remove_coin(wallet, coin_value):
    return update(wallet, {coin_value: wallet[coin_value] - 1})

def has_next_solution(solution, next_coin_value):
    coins_given, wallet = solution
    return wallet[next_coin_value] > 0 and coins_given != "IMPOSSIBLE"

def next_solution(solution, next_coin_value):
    coins_given, wallet = solution
    return coins_given + 1, remove_coin(wallet, next_coin_value)
    
def parent_solutions(solutions, amount_left, coin_values):
    for coin_value in coin_values:
        if coin_value <= amount_left:
            solution = (solutions[amount_left - coin_value], coin_value)
            if has_next_solution(*solution):
                yield next_solution(*solution)

def best_parent_solution(solutions, amount_left, coin_values):
    return min(parent_solutions(solutions, amount_left, coin_values), key=lambda solution: solution[0], default=("IMPOSSIBLE", {}))

def minimum_number_of_coins(amount, wallet):
    solutions = [(0, wallet)]
    for i in range(1, amount + 1):
        solutions.append(best_parent_solution(solutions, i, wallet))
    return solutions[-1][0]

amount = int(input())
ncoin_types = int(input())
wallet = {coinValue: coinsLeft for coinsLeft, coinValue in (map(int, input().split()) for _ in range(ncoin_types))}

print(minimum_number_of_coins(amount, wallet))
