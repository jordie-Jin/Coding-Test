def solution(m, o, s):
    answer = m[:s] + o + m[s + len(o):]
    return answer