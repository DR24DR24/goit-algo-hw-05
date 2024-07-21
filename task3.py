def compute_lps0(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def compute_lps(pattern):
    length=len(pattern)
    lps=[0]*length
    for i in range(1,len(pattern)):
        k=i-1
        while k>=0:
            if pattern[i]==pattern[lps[k]]:
                lps[i]=lps[k]+1
                break
            k=lps[k]-1
            
    return lps

def kmp_search0(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps0(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."

pattern = "алг"

print(kmp_search0(raw, pattern))




#print(compute_lps0("aabaa"))
#print(compute_lps("aabaa"))

def kmp_search(main_string, pattern):
    lps=compute_lps(pattern)
    print(lps)
    lps=compute_lps0(pattern)
    print(lps)
    M = len(pattern)
    N = len(main_string)
    
    i=segment=0

    while i<N:
        if main_string[i]==pattern[segment]:
            segment+=1
            i+=1
        elif segment!=0:
            segment=lps[segment-1]
        else:
            i+=1

        if segment==M:
            return i-M
    return -1


res=kmp_search("aab" , "aab")
print("2",res)

raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."

pattern = "алг"

res=kmp_search(raw , pattern)
print(res)

def read_file(name):
    with open(name,"r") as file:
        text=file.read().replace("\n"," ")
    return text

text=read_file("стаття 2.txt")

res=kmp_search(text,"системах.  Наявність")
print(res)
if res>=0:
    print(text[res:min(res+80,len(text))])

    
  

