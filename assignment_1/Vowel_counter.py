def vowel_counter(string):
    count = 0
    for c in string:
        if(c == 'a' or c == 'e'or c == 'i' or c == 'o' or c == 'u'):
            count += 1
    
    return count