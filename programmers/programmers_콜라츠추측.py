#https://programmers.co.kr/learn/courses/30/lessons/12943
#프로그래머스-콜라츠 추측
def solution(num):
    answer = 0
    while num!=1:
        if num%2==0:
            num/=2
        else:
            num=num*3+1
        if answer+1>500:
            return -1
        answer+=1
        
    return answer