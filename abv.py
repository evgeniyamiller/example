def readfile (name): 
    fr = open(name,'r', encoding = 'utf-8') 
    f = fr.read().split() 
    fr.close()
    return f

def poalfavitu(f): 
    text = '' 
    string = '' 
    alf = 'абвгдеёжхийклмнопрстуфхцчшщъыьэюя' 
    for i in alf: 
        string = i + '\t' 
        for word in f: 
            word = word.lower() 
            word = word.strip('()",.:;!?') 
            if word.startswith(i): 
                string = string + word + ', ' 
        text = text + string + '\n' 
        string = ''
    return text

def writefile(text): 
    fw = open('new.tsv', 'w') 
    fw.write(text) 
    fw.close()

def main():
    writefile (poalfavitu (readfile ('вождь.txt')))
    
main()
