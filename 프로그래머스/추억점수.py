def solution(name, yearning, photo):
    memory = dict()
    for i in range(len(name)):
        memory[name[i]] = yearning[i]

    answer = []
    for ph in photo:
        score = 0
        for p in ph:
            try:
                score += memory[p]
            except KeyError:
                continue
        answer.append(score)

    return answer


solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
         [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])

solution(["kali", "mari", "don"], [11, 1, 55],
         [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])
