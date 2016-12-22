keywords = {}
k=1
for i in 'abcdefghijklmnopqrstuvwxyz':
    keywords[i] = k
    k+=1

import unicodedata


def uni(s):
    return unicodedata.normalize('NFKD', s).encode('ascii','ignore')

def change(i):
    i = i.lower()
    changed = ''    
    for j in i:
        if keywords.get(j):
            x = str(keywords.get(j))
            if len(x) >= 2:
                changed+="("+str(keywords.get(j))+")"
            else:
                changed+=str(keywords.get(j))
        else:
            changed+=j
    return changed

def do_again(word):
    import random
    x = random.choice(word)
    if len(x) > 5:
        return x
    else:
        return random.choice(word)

    
def leave_blanks(i):
    i = i.lower()
    word_list = i.split()
    changed_list = []
    x = ''
    import random

    # Creating missing letters list

    x = i.replace(random.choice(word_list),"____")
    if len(i) <= 7:
        return i
    if len(word_list) <=3:
        return i
    if len(i) >= 5:
            j = i.replace(random.choice(word_list),"____")
            v = j.replace(random.choice(word_list),"____")
            x = v.replace(random.choice(word_list),"____")

            return x            
            
