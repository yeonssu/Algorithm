from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)

    for i in report:
        a,b = i.split()
        user[a].add(b)
        cnt[b] += 1

    for i in id_list:
        result = 0
        for u in user[i]:
            if cnt[u] >= k:
               result += 1
        answer.append(result)
    print(answer)
    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
# solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)