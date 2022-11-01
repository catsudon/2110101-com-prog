def match(word, pattern, include_chars, exclude_chars):
    vst = [0]*199
    for i in include_chars:
        vst[ord(i)] += 1
    if(len(word) != len(pattern)):
        return False

    for i in range(len(word)):
        if(pattern[i]=='?'):
            if(word[i] in exclude_chars): return False
            vst[ord(word[i])] -= 1
        else:
            if(word[i] != pattern[i]): return False
    
    for i in vst:
        if(i > 0): return False
    return True
     
exec(input()) # DON'T remove this line