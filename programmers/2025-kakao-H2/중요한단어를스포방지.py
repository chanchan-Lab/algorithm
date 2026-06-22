def solution(message, spoiler_ranges):
    print(message[34],message[53],message[59])
    
    # 0-1. 문장 내 단어
    words = message.split(' ')
    print('words', words)

    # 0-2. 문장 내 단어 index => words_range_idx
    words_range_idx = []
    print('길이', (words[11]))
    n = 0
    for word in words : 
        words_range_idx.append([n, n+int(len(word))-1])
        # print([n, n+int(len(word))-1])
        n = n+int(len(word))+1
    print("words_range_idx", words_range_idx)
    
    # 1. spoiler_ranges로 word_index 찾기
    return_s = []
    return_e = []
    for (s, e) in spoiler_ranges: # spoil 구간

        if message[int(s)] == ' ' :
            print('*here' , message[int(s)], message[int(e)])

            s = s+1
        if message[int(e)] == ' ' :
            print('*here' , message[int(s)], message[int(e)])

            e = e-1

        print(s,e)
        print('here' , message[int(s)], message[int(e)])

        print('s=', s)
        for i, j in words_range_idx:
            if s <= j:
                return_s.append(words_range_idx.index([i,j]))
                print('s', return_s, words_range_idx.index([i,j]))
                break

    for (s, e) in spoiler_ranges: # 0, 3
        print('e=', e)

        if message[int(s)] == ' ' :
            print('*here' , message[int(s)], message[int(e)])

            s = s+1
        if message[int(e)] == ' ' :
            print('*here' , message[int(s)], message[int(e)])

            e = e-1

        for i, j in words_range_idx:
            if e <= j:
                return_e.append(words_range_idx.index([i,j]))
                print('e', return_e, words_range_idx.index([i,j]))
                break

    spoil_idx_words = []
    for i in range(len(spoiler_ranges)):
        spoil_idx_words.append((return_s[i], return_e[i]))

    print('spoil_idx_words', spoil_idx_words)


    # 2. spoil_word_ind로 words삭제
    spoil_words = set()
    for (spoil_word_idx_s, spoil_word_idx_e) in spoil_idx_words:
        spoil_words.add(words[int(spoil_word_idx_s)])
        spoil_words.add(words[int(spoil_word_idx_e)])
        
    print(spoil_words)

    # 3. spoil_word가 제거된 words에서 spoil_word와 중복된 단어는 카운트에서 제외시키기
    count = len(spoil_words)
    for spoil_word in spoil_words:
        print(spoil_word)
        words.remove(spoil_word)
        print(words)

    print('spoil 삭제된 words', words)
    for spoil_word in spoil_words:
        if spoil_word in words:
            print(words)
            print(spoil_word)
            count -= 1

    print(count)
    return count



# MAIN ____
message = "my phone number is 01012345678 and may i have your phone number"
spoiler_ranges = [[5, 5], [25, 28], [34, 40], [53, 59]]

print(solution(message, spoiler_ranges))



'''
1. 첫번쨰 시도
[문제] (공백)word(공백) => 처리를 잘못했다. 

2. 두번째 시도
[문제] spoil words 자료형을 set으로 하는 바람에 spoil안에서 두번 중복되는 phone의 경우, 한번만 삭제되는 문제가 발생했다. 
[해결] 완전히 관점을 벗어나서 새롭게 발상해보자. 즉, spoil기준으로 (왼쪽공백), (오른쪽공백)을 찾는거야.

'''