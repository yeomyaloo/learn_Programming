from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    # 신고 당한애
    reportA = defaultdict(set)
    # 신고한 애
    reportB = defaultdict(set)

    for i in report:
        a, b = i.split(' ')
        reportA[b].add(a)
        reportB[a].add(b)

    for id in id_list:
        cnt = 0
        for i in reportB[id]:
            if len(reportA[i]) >= k:
                cnt += 1
        answer.append(cnt)

    return answer