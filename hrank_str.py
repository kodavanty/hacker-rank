#!/usr/bin/python
import string

# HACKERRANK string challenges

'''
Pangrams are sentences constructed by using every letter of the alphabet at 
least once.
'''
def pangram():
    s = raw_input("Enter string: ")

    dict = {}
    for c in s.lower():
        if not c.isalpha():
            continue

        if not c in dict:
            dict[c] = 1

    for c in string.ascii_lowercase:
        if not c in dict:
            return False

    return True

'''
Si - Si-1 = Ri - Ri-1 then string is funny
'''
def is_funny_string(s):
    for i in range(0, len(s)/2):
        f = abs(ord(s[i]) - ord(s[i+1]))
        #print "%d: %c %c %d" % (i, s[i], s[i+1], f)
        r = abs(ord(s[len(s)-i-1]) - ord(s[len(s)-i-2]))
        #print "%d: %c %c %d" % (i, s[len(s)-i-1], s[len(s)-i-2], r)
        if f != r:
            return False

    return True

def funny_string():
    num_str = int(raw_input())

    strA = {}
    for i in range(0,num_str):
        strA[i] = raw_input()

    for s in strA.values():
        if is_funny_string(s):
            print "Funny"
        else:
            print "Not Funny"
            
def alt_chars():
    num_str = int(raw_input())

    strA = {}
    for i in range(0,num_str):
        strA[i] = raw_input()

    for s in strA.values():
        num = {}
        j = 0
        k = 0
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                k = k + 1
            else:
                num[j] = k
                k = 0
                j = j + 1

        num[j] = k

        k = 0
        for n in num.values():
            k = k + n 

        print k

def game_of_thrones():
    string = raw_input()
     
    not_found = False
    # Anagram is a palindrome if it has one letter with odd frequency and 
    # rest even.
    dict = {}

    for c in string:
        if c in dict:
            dict[c] = dict[c] + 1
        else:
            dict[c] = 1

    num_odd = 0
    for v in dict.values():
        if v%2 == 1:
            num_odd = num_odd + 1
            if num_odd > 1:
                not_found = True
                break
                
    if not_found:
        print("NO")
    else:
        print("YES")

def two_two():
    return

if __name__ == "__main__":

    two_two()

    '''
    #4
    game_of_thrones()

    #3
    alt_chars()

    #2

    funny_string()
    #1
    res = pangram()
    if res:
        print "pangram"
    else:
        print "not pangram"

    '''
