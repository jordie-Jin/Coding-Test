def solution(arr, n):
    return [arr[i] + n if i % 2 != len(arr) % 2 else arr[i] for i in range(len(arr))] 