# difficulty: easy
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = list(arr)
    maximum = max(scores)
    while maximum in scores:
        scores.remove(maximum)
        
    runner_up = max(scores)
    print(runner_up)
