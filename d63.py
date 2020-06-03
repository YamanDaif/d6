from DictHash import *
from LinkedQ import *
import sys


class ParentNode:

    def __init__(self, word, parent= None):
        self.word = word
        self.parent = parent



def makechildren(ord, ordlista):

        boks_L=list("abcdefghijklmnopqrstuvwxyzåäö")
        children=[]

        for x in boks_L:
                ordkomp1 = "".join([x, ord[1], ord[2]])
                if ordkomp1 in ordlista and ordkomp1 != ord:
                    children.append(ordkomp1)#lagra ordet i children med append


                ordkomp2= "".join([ord[0],x,ord[2]])
                if ordkomp2 in ordlista and ordkomp2 != ord:
                    children.append(ordkomp2)#lagra den i children lista med append

                ordkomp3 = ''.join([ord[0], ord[1], x])
                if ordkomp3 in ordlista and ordkomp3 != ord:
                    children.append(ordkomp3)#lagra den i en lista med append

        return children

queueOfWords = LinkedQ()


ordlista = DictHash()  # för att hasha orden som kommer att lagras i "ordlistan"
word3 = open('word3.txt', 'r')   # för att öppna ord listan och läsa den
for rad in word3:
    ordlista.store(rad[:-1], None)  # we are storing the word3 in the Dicthash ones at a timereturn

Road = []
def writechain(Node):
    while queueOfWords.isEmpty() is False:
        if Node.parent != None:
            Road.append(Node.word)
            writechain(Node.parent)
        else: Road.append(Node.word)
        if Node.parent == None :
            Road.reverse()
            print(Road)
        return

#ordtest=['mak','men','man','rad','kan','han' ,'hen']
#test = makechildren('fan',ordlista)
#print(test)

def Hitta_vagen(word1,word2):

    StartOrd = word1 #(input("Startord:"))
    SlutOrd = word2 #(input("Slutord"))
    start = ParentNode(StartOrd, parent=None)
    queueOfWords.enqueue(start)


    redan_besokta = DictHash()
    redan_besokta.store(StartOrd, None)



    while queueOfWords.isEmpty() is False:

        Node = queueOfWords.dequeue() #next word is now a parent node that was queued in linkedQ(queueOfWords)
        barn = makechildren(Node.word, ordlista)  # making ParentNoder

        for word in barn:  # we can't itrate binary tree nodes so we etrate a list
            wordNode = ParentNode(word, Node)  # and create a parentnode for each (str word) with its (ParentNode)

            if Node.word == SlutOrd:
                print("Vägen från ",StartOrd," till", SlutOrd,"är: ")
                writechain(Node)
                return
            if redan_besokta.__contains__(word) is False:  # här köar vi bara barn (ParentNoder)som inte har köat förut.
                queueOfWords.enqueue(wordNode)  # first queue the chilled
                redan_besokta.store(word, None)  # then store it in bintree for next loop

        if queueOfWords.isEmpty() is True:
            print("Det fanns ingen väg")


if len(sys.argv) < 3:
    print("Start- och slutord saknas")
    print('Använd programmet så här på terminalen: \n\t python3', sys.argv[0], ' [StartOrd] [slutord] "Tre gemena bokstäver för varje ord"')
    sys.exit()

else:
   Hitta_vagen(sys.argv[1],sys.argv[2])
'''
#Hitta_vagen("fan","gud")
import sys

if len(sys.argv) < 3:
   print("parametrar saknas")
   print('Använd programmet så här på terminalen: \n\t python3', sys.argv[0], 'Parameter1  Parameter2')
   sys.exit()
else:
   print("parameter 1 är",  sys.argv[1], " och parameter 2 är", sys.argv[2])
'''