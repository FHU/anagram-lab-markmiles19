#REMOVE PASS AND FIX THIS FUNCTION
letterCount1 = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0,
               'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0,
               'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0,
               'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0,
               'Y':0, 'Z':0}

letterCount2 = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0,
               'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0,
               'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0,
               'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0,
               'Y':0, 'Z':0}

def anagram(word1, word2):
    word1 = word1.upper().replace(' ', '')
    word2 = word2.upper().replace(' ', '')
    for letter in word1:
        letterCount1[letter] += 1
    for letter in word2:
        letterCount2[letter] += 1
    if word1 == '':
        return False
    elif word2 == '':
        return False
    else:
        if letterCount1 == letterCount2:
            return True
        else:
            return False

if __name__ == '__main__':
    user_input1 = input()
    user_input2 = input()
    print(anagram(user_input1, user_input2))
    