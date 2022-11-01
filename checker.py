import re


# shit = []
class Hasan:

  def __init__(self) -> None:
     self.shit = []

  def normalizeI(self, txt):
    
    if ("<br" in txt):
        txt.replace("<br ", "")
        size = len(txt)
        
        txt1 = txt[:size - 3]
        # print("11- ",txt1)
    
        return txt1  
    if ("_x000D_" in txt):
        txt.replace("_x000D_", "")
        size = len(txt)
          
        txt2 = txt[:size - 7]
        return txt2

        

    return txt


  def create_stopwords(self):
    with open ('shitty.txt', encoding="utf8") as shitty:
      # shit = shitty.readlines()
      # shit = list(shitty)
      self.shit = shitty.read().split('\n')


  def normalizeII(self, txt):
    import string
    test_str = txt.translate(str.maketrans('', '', string.punctuation))
    return test_str

  def isEmail(self, txt , f):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex, txt):
        print("Valid email:" , txt , file=f)
        #txt = ""
        return 1

    return 0

  def isLink(self, txt ,f):
    regex = re.compile(r'((https?|ftp):\/\/)?(?<!@)(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})[-\w@:%_\.\+\/~#?=&]*')
    httpFormCheckerString = txt[:4]
    if re.fullmatch(regex, txt):
        print("Valid Link:" , txt , file=f)
        #txt = ""
        return 1

    return 0

  def isID(self, txt ,f):
    regex = re.compile(r'(?<![\w\._])(@[\w_]+)')

    if re.fullmatch(regex, txt):
        print("Valid ID:" , txt , file=f)
        #txt = ""
        return 1
        
    return 0

  def isIPAddress(self, txt ,f):
    regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    if re.fullmatch(regex, txt):
        print("Valid IP:" , txt , file=f)
        #txt = ""
        return 1
        
    return 0

  def isDate(self, txt , f):
    date_patternI = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
    date_patternII = "^(?:\\d{4})-(?:\\d{2})-(?:\\d{2})T(?:\\d{2}):(?:\\d{2}):(?:\\d{2}(?:\\.\\d*)?)(?:(?:-(?:\\d{2}):(?:\\d{2})|Z)?)$"
    
    if (re.match(date_patternI, txt) or re.match(date_patternII, txt)):
        print("Valid Date:" , txt , file=f)
        #txt = ""
        return 1
        
    return 0


  def isCommon(self, txt2 , f):
    # txt2 = normalizeII(txt2)

    # if "سلام" in txt2 :
    #       print("----------------------------------"+txt2+"-")
    #       print(txt2)
    #       print(self.normalizeII(txt2))
    # print("herrrrrrrrrrrrrrrrre")
    # print(type(self.shit))
    txt2 = self.normalizeII(txt2)
    for s in self.shit:
      if s == txt2:
        print("Valid Useless(Common): " , txt2, file=f)
        #txt = ""
        return 1
    
    return 0

  def isNumeric(self, txt , f):
    # txt = normalizeII(txt)
    regex = re.compile(r'[0-9]+')

    if re.fullmatch(regex, txt):
        dateFormCheckerString = txt[:4]
        dateFormCheckerInt = int(dateFormCheckerString)
        if (dateFormCheckerInt > 1350 and dateFormCheckerInt < 1450):
          print("Valid Date(Other Format):" , txt, file=f)
          #txt = ""
        # print("date: " , dateFormChecker)
        elif (len(txt) > 7 and (txt[0] == '0' or txt[0] == '9')):
          print("Valid PhoneNumber:" , txt, file=f)
          #txt = ""
        else:
          print("Valid Number:" , txt, file=f)
          #txt = ""
        return 1
        
    return 0

  def listToString(self, s):
    
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += " "
        str1 += ele

    # return string
    return str1


  def restCounter(self, words , f2):
    with open ('worthy.txt', encoding="utf8") as worthy:
      list_worthies = worthy.read().split('\n')

    all_worthies = dict()
    non_worthy_words = []
    worthy_words = []

    for x in list_worthies:
        all_worthies[x] = 0

    for w in words:
        if(list_worthies.__contains__(w)):
            # print(w)
            all_worthies[w] = all_worthies[w] + 1           
        else:
            non_worthy_words.append(w)

    kk = all_worthies.keys() 
    print("worthy words with count:", file = f2)       
    for k in kk:
        if(all_worthies[k] != 0):
            print(k , " , " , all_worthies[k] , file = f2)        
    
    print("------------------------------------------" , file = f2)        
    print("non worthy words with count:", file = f2)    
    for w in non_worthy_words:    
        print(w, file = f2)

  #######################################################################3############


  def main(self, txt, counter , f , f2):
    self.create_stopwords()
    txt = txt.replace("\r", " ")
    txt = txt.replace("\n", " ")
    txt = txt.replace("\t", " ")
    words = txt.split()
    new_words = []
    # f = open("output.txt" , "w", encoding="utf8")

          
    for index , elem in enumerate(words):
      
        #normalize0...

      if (elem == 'می'): 
            words[index] = ""
            words[index+1] = "می" + words[index+1]
            words.pop(index)
            
      if (elem == 'نمی'): 
            words[index] = ""
            words[index+1] = "نمی" + words[index+1]
            words.pop(index)


      words[index] = self.normalizeI(words[index])
      h = str(words[index])

      h = h.strip()
      if h.endswith("."):
        h = h[:-1]

      if (len(words[index]) >= 1): 
        print("I am checking the word: ", type(words[index]), words[index], file = f)
        # if "سلام" in words[index] :
        #   print("----------------------------------"+words[index]+"-")
        print( "", file = f)
        if (self.isEmail(words[index] , f) == 1 ): words.pop(index)
        elif (self.isLink(words[index] , f) == 1 ): words.pop(index)
        elif (self.isID(words[index] , f) == 1 ): words.pop(index)
        elif (self.isIPAddress(words[index] , f) == 1 ): words.pop(index)
        elif (self.isDate(words[index] , f) == 1 ): words.pop(index)
        elif (self.isNumeric(words[index] , f) == 1 ): 
          words[index] = self.normalizeII(words[index])
          words.pop(index)
        elif (self.isCommon(words[index] , f) == 1 ): 
          words[index] = self.normalizeII(words[index])
          words.pop(index) 
        elif (words[index].islower() or words[index].isupper()):
            words[index] = self.normalizeII(words[index]) 
            print("Valid ENgForm:"  , words[index] , file=f)
            words.pop(index)
          #else: print("Z others:"  , words[index] , file=f)
        # if (index < len(words)):
        print("end word: ", file = f)
        print("", file = f)
        print("", file = f)
          

          
    print("hehehheheheheheheheheheh" , counter)
    if (counter == 0):
        print("Second Time :////////////////////" , file=f)  
        s = self.listToString(words)
        
        self.main(s, 2, f ,f2)
    if (counter == 2):
        print("Third Time :////////////////////" , file=f)  
        s = self.listToString(words)
        
        self.main(s, 3, f , f2)
    if (counter == 3):
        print("Fourth Time :////////////////////" , file=f)  
        s = self.listToString(words)
        
        self.main(s, 1, f , f2)
    if (counter == 1):    
        print("hehehhehehehehehehehehehL" , counter)
        
        print("rest: " , file = f2)    
        for w in words:
            print(w , file = f2) 
        print("------------------------------------------" , file = f2)
        self.restCounter(words , f2)    
    f.close()



h = Hasan()


with open('sample.txt', encoding="utf8") as f:
    lines = f.read()
    # print(type(.

    f = open("output.txt" , "w", encoding="utf8")
    f2 =open("output2.txt" , "w", encoding="utf8")

    h.main(lines,0 , f , f2)

# text = input("enter comment:")
