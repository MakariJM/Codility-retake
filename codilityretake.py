                             #Key Notes
#Given an array S consisting of N strings. Every string is of the same length M.
#find a pair of strings in array S such that there exists a position in which both of the strings have the same letter. Both the index in array S and the positions in the strings are numbered from zero.
#result should be represented as an array containing three integers. 
#Assumptions:
         #N is an integer within the range [1..30,000];
         #M is an integer within the range [1..2,000];
         #each element of S consists only of lowercase English letters (a-z);
         #N*M≤ 30,000.


def solution(S):
    # Creating dictionary to store common letters and their indices
    common_letters = {}
    
    # Iterating over strings in the list S
    for i, string in enumerate(S):
        # Creating dictionary to store the count of each letter in the current string
        letter_count = {}
        
        # Iterating each letter in the string
        for j, letter in enumerate(string):
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        # Iterating each letter and its count in the letter_count dictionary
        for letter, count in letter_count.items():
            if letter in common_letters:
                common_letters[letter].append(i)
            else:
                common_letters[letter] = [i]
    
    # Creating empty list to store results
    result = []
    
    # Iterating each letter and its indices in the common_letters dictionary
    for letter, indices in common_letters.items():
        if len(indices) > 1:
            for i in range(len(indices) - 1):
                result.append([indices[i], indices[i + 1], S[indices[i]].index(letter)])
    
    # For a result list that is empty, return empty list
    if not result:
        return []
    # Otherwise, return the first item in result list
    else:
        return result[0]


                    #Test samples
print(solution(["abcd", "efgh", "ijkl", "mnop"]))
print(solution(["abcd", "zyxw", "ijkl", "wxyz"]))
print(solution(["abcd", "efgh", "ijkl", "mnop", "mnop"]))