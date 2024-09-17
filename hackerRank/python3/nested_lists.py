if __name__ == '__main__':
    score_list = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(name)
        score_list.append(score)


    n_inputs = len(score_list) // 2

    nested_score = list()

    index = -1
    for i in range(n_inputs):
        nested_score.append(list())
        index += 1
        nested_score[i].append(score_list[index])
        index += 1
        nested_score[i].append(score_list[index])

    scores = list()
    for li in nested_score:
        scores.append(li[1])
        # comparing the score with the maximum score
    
    scores.sort()
    lowest = scores[0]
    #sec_lowest = scores[1]
    
    names =list()
    scores = list()
    for li in nested_score:
        if li[1] != lowest:
            names.append(li[0])
            scores.append(li[1])
    
    #names.sort()
    scores.sort()
    
    sec_lowest = scores[0]
    sec_names = list()
    
    for li in nested_score:
        if li[1] == sec_lowest:
            sec_names.append(li[0])

    sec_names.sort()

    for name in sec_names:
        print(name)
