import re
import os

def readfile (name): 
    fr = open(name,'r', encoding = 'utf-8') 
    f = fr.read()
    fr.close()
    return f

def listnames(f):
    arr = re.findall('[А-Я]\. [А-Я][а-я]+', f)
    for el in arr:
        print(el)

def newlist(f):
    listnames = []
    arr = re.findall('(([А-Я]\. [А-Я][а-я]+)|([А-Я]\. ([А-Я]\.)? [А-Я][а-я]+)|([А-Я][а-я]+ [А-Я][а-я]+))', f)
    for el in arr:
        listnames.append(el[0])
    return listnames

def makedict(listnames):
    d = {}
    for el in listnames:
        name = el.split() 
        d[el] = str(name[-1])
    return d
    
def makedir (d):
    arr = []
    for el in d: 
        if d[el] not in arr:
            arr.append(d[el])
        try: 
            os.makedirs(d[el])
        except: pass

def makenewdict (d, f):
    newd = {}
    for k in d:
        regex = '([А-Яа-я,:";]* )*' + str(k) + '( [А-Яа-я,:";]*)*'
        r = re.search(regex, f)
        newd[k] = r.group()
    return newd
        

def writefile(text, name):
    fw = open(name, 'w', encoding = 'utf-8') 
    fw.write(text) 
    fw.close()
        
def walk (newd, d):
    arr = []
    for root, dirs, files in os.walk('.'):
        for el in root:
            text = newd[el]
            name = str(el)+'.txt'
            writefile(text, name)
            

listnames(readfile('статья.txt'))
walk(makenewdict((makedict(newlist(readfile('статья.txt')))), readfile('статья.txt')), makedict(newlist(readfile('статья.txt'))))



