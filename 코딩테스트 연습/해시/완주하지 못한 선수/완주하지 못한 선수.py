def solution(participant, completion):
    
    # efficiency test Failed
    # for h in completion:
    #     participant.remove(h)
    # answer = participant[0]
    
    participant.sort()
    completion.sort()
    
    answer = participant[-1]
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer