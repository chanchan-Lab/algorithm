def find_words(message):
    words = list(message.split(' '))
    words = words[1:len(words)-1]
    return words

def solution(message, spoiler_ranges):
    message = ' ' + message + ' '
    
    # spoil 되어야하는 단어들의 범위를 구한다. 
    spoil_ind_ranges = [[0,0]]
    for spoiler_ranges_left, spoiler_ranges_rght in spoiler_ranges:
        spoiler_ranges_left = spoiler_ranges_left + 1
        spoiler_ranges_rght = spoiler_ranges_rght + 1
        left_i = spoiler_ranges_left
        rght_i = spoiler_ranges_rght 

        while(message[left_i]!=' '):
            left_i -= 1
            if left_i < 0:
                break    


        while(message[rght_i]!=' '):
            rght_i += 1
            if rght_i > len(message)-1:
                break
            
        
        spoil_ind_ranges.append([left_i, rght_i])

        print(len(message))
        print([left_i, rght_i])
        print('*', message[left_i], message[rght_i])
    
    print('-' *100)
    print(spoil_ind_ranges)
    print(message)

# ----------------------------------------------------------------------------------------------------
    # [(문제) 앞에서부터 삭제하려고 했더니.. index가 너무 꼬였다. => (해결) 뒤에서부터 삭제]
    # # spoil_words를 구간으로 삭제
    # for ind, [left_i, rght_i] in enumerate(spoil_ind_ranges):
    
    #     print(ind, ')' ,[left_i, rght_i])
    #     if ind == 0:
    #         continue
    #     left_i = left_i - (spoil_ind_ranges[ind-1][1]-spoil_ind_ranges[ind-1][0])
    #     rght_i = rght_i - (spoil_ind_ranges[ind-1][1]-spoil_ind_ranges[ind-1][0])
    #     print('v',left_i, rght_i)
    #     print('#', message[left_i], message[rght_i])

    #     message=message[:left_i] +" "+ message[rght_i+1:]
        
    #     print(message)
# ----------------------------------------------------------------------------------------------------

    live_message = message
    for left_i, rght_i in reversed(spoil_ind_ranges[1:]):
        live_message = live_message[:left_i] + " " + live_message[rght_i+1:]

        # print('00', live_message)
        

    result = set()
    for i in find_words(message):
        # print(i)
        if i not in find_words(live_message):
            result.add(i)

    # print("RESULT", len(result))
    return len(result)

# MAIN ____
# message = "my phone number is 01012345678 and may i have your phone number"
message = "here is muzi here is a secret message"

# spoiler_ranges = [[5, 5], [25, 28], [34, 40], [53, 59]]
spoiler_ranges = [[0, 3], [23, 28]]
print(solution(message, spoiler_ranges))


