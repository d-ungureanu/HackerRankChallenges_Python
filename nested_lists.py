if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    unique_scores = set()
    for pair in records:
        unique_scores.add(pair[1])
    unique_scores_list = sorted(list(unique_scores))
    if len(unique_scores_list) > 1:
        second_grade = unique_scores_list[1]
    result =[]
    for pair in records:
        if pair[1] == second_grade:
            result.append(pair[0])
    for name in sorted(result):
        print(name)
