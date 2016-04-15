# pylint: disable=locally-disabled,missing-docstring

def minimum_number_of_coins(amount, wallet):
    solutions = [(0, wallet)]
    for intermediate_amount in range(1, amount + 1):
        solutions.append(find_best_solution(intermediate_amount, wallet, solutions))
    return solutions[-1][0]

def find_best_solution(amount, coin_values, solutions):
    return min(
        find_solutions(amount, coin_values, solutions),
        key=lambda solution: solution[0],
        default=("IMPOSSIBLE", {}))

def find_solutions(amount, coin_values, solutions):
    for coin_value in coin_values:
        if coin_value <= amount:
            coins_given, wallet = solutions[amount - coin_value]
            if wallet.get(coin_value, 0) > 0:
                yield coins_given + 1, remove_coin(wallet, coin_value)

def remove_coin(wallet, coin_value):
    return update(wallet, {coin_value: wallet[coin_value] - 1})

def update(a_dict, another_dict):
    new_dict = a_dict.copy()
    new_dict.update(another_dict)
    return new_dict

def main():
    amount = int(input())
    ncoin_types = int(input())
    wallet = {
        int(coin_value): int(coins_left) for coins_left, coin_value in
        (input().split() for _ in range(ncoin_types))}
    print(minimum_number_of_coins(amount, wallet))


if __name__ == "__main__":
    main()
