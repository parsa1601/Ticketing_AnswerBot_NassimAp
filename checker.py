import re



def normalizeI(txt):
  
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



def normalizeII(txt):
  pat = (r'[.?\-",]+')
  res = re.sub(r'[^\w\s]', ' ', txt)
  return res

def isEmail(txt , f):
  regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

  if re.fullmatch(regex, txt):
      print("Valid email:" , txt , file=f)
      txt = ""
      return 1

  return 0

def isLink(txt ,f):
  regex = re.compile(r'((https?|ftp):\/\/)?(?<!@)(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})[-\w@:%_\.\+\/~#?=&]*')
  httpFormCheckerString = txt[:4]
  if re.fullmatch(regex, txt):
      print("Valid Link:" , txt , file=f)
      txt = ""
      return 1

  return 0

def isID(txt ,f):
  regex = re.compile(r'(?<![\w\._])(@[\w_]+)')

  if re.fullmatch(regex, txt):
      print("Valid ID:" , txt , file=f)
      txt = ""
      return 1
      
  return 0

def isIPAddress(txt ,f):
  regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

  if re.fullmatch(regex, txt):
      print("Valid IP:" , txt , file=f)
      txt = ""
      return 1
      
  return 0

def isDate(txt , f):
  date_patternI = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
  date_patternII = "^(?:\\d{4})-(?:\\d{2})-(?:\\d{2})T(?:\\d{2}):(?:\\d{2}):(?:\\d{2}(?:\\.\\d*)?)(?:(?:-(?:\\d{2}):(?:\\d{2})|Z)?)$"
  
  if (re.match(date_patternI, txt) or re.match(date_patternII, txt)):
      print("Valid Date:" , txt , file=f)
      txt = ""
      return 1
      
  return 0


def isCommon(txt , f):
  for s in shit:
    if s == txt:
      print("Valid Useless(Common): " , txt, file=f)
      txt = ""
      return 1
  
  return 0

def isNumeric(txt , f):
  regex = re.compile(r'[0-9]+')

  if re.fullmatch(regex, txt):
      dateFormCheckerString = txt[:4]
      dateFormCheckerInt = int(dateFormCheckerString)
      if (dateFormCheckerInt > 1350 and dateFormCheckerInt < 1450):
        print("Valid Date(Other Format):" , txt, file=f)
        txt = ""
      # print("date: " , dateFormChecker)
      elif (len(txt) > 7 and (txt[0] == '0' or txt[0] == '9')):
        print("Valid PhoneNumber:" , txt, file=f)
        txt = ""
      else:
        print("Valid Number:" , txt, file=f)
        txt = ""
      return 1
      
  return 0




############


def main(txt):

  words = txt.split()
  new_words = []
  f = open("output.txt" , "w")

         
  for index , elem in enumerate(words):
    
      #normalize0...

    if (elem == 'می'): 
          words[index] = " "
          words[index+1] = "می" + words[index+1]
          words.pop(index)
          
    if (elem == 'نمی'): 
          words[index] = " "
          words[index+1] = "نمی" + words[index+1]
          words.pop(index)


    words[index] = normalizeI(words[index])
    words[index] = normalizeII(words[index])

    if (len(words[index]) != 0): 

      if (isEmail(words[index] , f) + isLink(words[index] , f) + isID(words[index] , f) 
      + isIPAddress(words[index] , f) + isDate(words[index] , f)
      + isNumeric(words[index] , f) + isCommon(words[index] , f) == 0 ): 
        if (words[index].islower() or words[index].isupper()): 
          print("Valid ENgForm:"  , words[index] , file=f)
          words[index] = ""
        #else: print("Z others:"  , words[index] , file=f)

        
      
      
  for w in words:
    print(w, end = '') 
  f.close()



  def run():
    text = input("enter the comment: ")
    main(text)