def puncs_split():
    english_shell = []
    for word in english.split(" "):
        added = False
        for p in puncs:
            if p in word:
                added = True
                english_shell.append(word.replace(p, ""))
                english_shell.append(p)
        if added == False:
            english_shell.append(word)
    return english_shell

def sentence_shell():
    line = None
    shell = []
    with open("dictonary.txt") as f:
        moheng = f.read().splitlines() 
    for word in english:
        added = False
        for mh in moheng:
            line = mh.split(" : ")
            if line[1] == word.lower():
                added = True
                shell.append(line[0])

            if word in puncs:
                shell[len(shell) - 1] += word
                added = True
                break
                
        if added == False:
            shell.append(word)
        
    return shell

def grammatize(sentence):
    #ToDo; after more words are added
    return sentence

puncs = [",", ".", ";", "!", "?"]

english = input("English Sentence:\n")
english = puncs_split()

moghol = []
moghol = sentence_shell()
moghol = grammatize(moghol)
moghol = " ".join(moghol)
print(moghol)
