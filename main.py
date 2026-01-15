def tri_insertion(liste):
    for i in range(1,len(liste)):
        element = liste[i]
        j = i-1
        while j>=0 and liste[j] > element:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = element
    return liste


liste = [6,5,3,1,8,7,2,4]

liste_trie = tri_insertion(liste)
print(liste_trie)