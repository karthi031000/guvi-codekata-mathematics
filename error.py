string = input()
lst = []
for words in string:
  if ((words.isdigit() == True) and (int(words) % 2 == 0)):
      ind1 = string.index(words)
      if(string[ind1].isdigit() == True):
          change1 = words + ind1
          change2 = int(change1)
          if(change2 % 2 == 0):
              ind = string.index(words) - 1
              for i in range(0,ind):
                  lst.append(string[ind])
      else:
          typ = int(words)
          ind = string.index(words) - 1
          for i in range(0,typ):
            lst.append(string[ind])
print(*lst,sep="")
      
