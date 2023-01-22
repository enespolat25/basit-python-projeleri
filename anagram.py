from collections import defaultdict

def anagramlari_grupla(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

kelimeler = ["açlık", "çalık", "çakıl", "laçkı", "kalıç", "kaçlı", "akçıl","asılmak", "kasılma", "ıslamak", "kısalma", "salkıma", "mıskala", "makaslı", "asmalık","alim", "mali", "imla", "mail", "imal", "ilam","akşamları", "karşılama", "karışlama", "karılaşma", "ıraklaşma", "arılaşmak", "arıklaşma","alaşım", "şamalı", "maşalı", "aşılma", "alışma", "maaşlı","kaykılma", "yakılmak", "yamaklık", "yakmalık", "kaymaklı", "kaymalık","arıklaşmak", "ıraklaşmak", "karılaşmak", "karşılamak", "karışlamak","anlaştırmak", "tıraşlanmak", "tanrılaşmak" ]
#print(anagramlari_grupla(kelimeler))

liste=list(anagramlari_grupla(kelimeler))
for i,liste in enumerate(liste):
    print((i+1),". grup->",liste)