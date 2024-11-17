import sys

def maximumAffordableToys(toy_prices, budget):
    toy_prices = sorted(toy_prices)  
    toy_count = 0
    
    for price in toy_prices:
        if budget - price >= 0:
            budget -= price
            toy_count += 1
        else:
            break
        
    return toy_count
  

if __name__ == "__main__":
    num_toys, budget = input().strip().split(' ')  
    num_toys, budget = [int(num_toys), int(budget)]  
    toy_prices = list(map(int, input().strip().split(' '))) 
    result = maximumAffordableToys(toy_prices, budget) 
    print(result) 