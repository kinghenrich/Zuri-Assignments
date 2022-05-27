# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(s1, s2):
    # [assignment] Add your code here
    if(sorted(s1)==sorted(s2)):
        print("true")
    else:
        print("false")
s1="listen"
s2="silent"
find_anagrams(s1, s2)