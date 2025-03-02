# 준 사람/ 받은 사람 테이블 만들기
# 만든 테이블 이용해서 각 친구의 선물 지수 리스트 만들기
# i,j 이용해서 테이블의 i,j와 j,i를 비교해서 같을 경우 선물 지수 리스트 참고 받을 선물 count하고 max값 추출
import sys
def solution(friends, gifts):
    answer = 0
    friend_num = len(friends)
    score = []
    table = [[0]*friend_num for _ in range(friend_num)]
    
    # 1:1로 선물 매칭 확인 
    # 테이블 만들기
    for i in range(friend_num):
        friend1 = friends[i]
        for j in range(i+1, friend_num):
            give = 0
            get = 0
            friend2 = friends[j]
            for g in gifts:
                give_friend,get_friend = map(str, g.split())
                # friend1이 friend2에게 선물을 주었을 때
                if friend1 == give_friend and friend2 == get_friend:
                    give += 1
                # friend2가 선물을 받았을 때
                if friend2 == give_friend and friend1 == get_friend:
                    get += 1
            table[i][j] = give
            table[j][i] = get
            
    for i in range(friend_num):
        give = 0
        get = 0
        for j in range(friend_num):
            give += table[i][j]
            get += table[j][i]
        score.append(give - get)
    
    for i in range(friend_num):  
        cnt = 0
        for j in range(friend_num):
            if i == j:
                continue
            give = table[i][j]
            get = table[j][i]
            if give == get:
                if score[i] > score[j]:
                    cnt += 1
            elif give > get:
                cnt += 1
        if cnt > answer:
            answer = cnt
            
    return answer