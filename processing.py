from nltk.corpus import wordnet
def do_calculation(word, nword, must, sword):
    import enchant
    global mess
    d = enchant.Dict("en_US")
    # dictionary=PyDictionary()


    word = word.lower()
    nword = nword.lower()
    sword = sword.lower()
    must = must.lower()

    lword = len(word)
    lnword = len(nword)
    lsword = len(sword)
    lmust  = len(must)

    a1 = word[0:1]
    a2 = word[1:2]
    a3 = word[2:3]
    a4 = word[3:4]
    a5 = word[4:5]

    if a1 != "*" : a1 = a1.lower()
    if a2 != "*" : a2 = a2.lower()
    if a3 != "*" : a3 = a3.lower()
    if a4 != "*" : a4 = a4.lower()
    if a5 != "*" : a5 = a5.lower()

    l1=1
    l2=1
    l3=1
    l4=1
    l5=1

    if a1 == '*' :
        l1 =26
    if a2 == '*' :
        l2 =26
    if a3 == '*' :
        l3=26
    if a4 == '*' :
        l4=26
    if a5 == '*' :
        l5=26

    a11=a1
    a22=a2
    a33=a3
    a44=a4
    a55=a5

    oa1 = ord(a1)
    oa2 = ord(a2)
    oa3 = ord(a3)
    oa4 = ord(a4)
    oa5 = ord(a5)

    valid = False

    if(str(oa1) == "32") :
        mess = "No spaces. use * for Unknown."
        return mess, mess
    if(str(oa2) == "32") :
        mess = "No spaces. use * for Unknown."
        return mess, mess
    if(str(oa3) == "32") :
        mess = "No spaces. use * for Unknown."
        return mess, mess
    if(str(oa4) == "32") :
        mess = "No spaces. use * for Unknown."
        return mess, mess
    if(str(oa5) == "32") :
        mess = "No spaces. use * for Unknown."
        return mess, mess

    if (str(oa1) == "42" or (oa1>96 and oa1<123)):
        valid = True
    else :
        mess ="First character must a letter or *"
        return word, mess

    if (str(oa2) == "42" or (oa2>96 and oa2<123)):
        valid = True
    else :
        mess ="Second character must a letter or *"
        return word, mess

    if (str(oa3) == "42" or (oa3>96 and oa3<123)):
        valid = True
    else :
        mess ="Third character must a letter or *"
        return word, mess

    if (str(oa4) == "42" or (oa4>96 and oa4<123)):
        valid = True
    else :
        mess ="Fourth character must a letter or *"
        return word, mess

    if (str(oa5) == "42" or (oa5>96 and oa5<123)):
        valid = True
    else :
        mess ="Last character must a letter or *"
        return word, mess

    count = 0
    wardl = ""
    if lword != 5 :
        mess = "Found "+str(lword) + "letters, please enter 5 characters, * for unknown letter. Example **A*L"
        return word, mess

    mess = " Happy Wordling"

    for x1 in range(0, l1):
        if a1 == '*' : a11 = chr(97 + x1)
        for x2 in range(0, l2):
            if a2 == '*' : a22 = chr(97 + x2)
            for x3 in range(0, l3):
                if a3 == '*' : a33 = chr(97 + x3)
                for x4 in range(0, l4):
                    if a4 == '*' : a44 = chr(97 + x4)
                    for x5 in range(0, l5):
                        if a5 == '*' : a55 = chr(97 + x5)
                        wardle = a11+a22+a33+a44+a55

                        #print(str(count) + " " + wardle)

                        lt=True
                        if d.check(wardle) == True:

                            if count > 300:
                                mess = "  Too many results, showing only the first 300"
                                return wardl
                            for xx in range(0,lnword):
                                if str(nword[xx]) in wardle :
                                    lt=False

                            for xx in range(0,lmust):
                                if str(must[xx]) not in wardle :
                                    lt=False

                            for xx in range(0,lsword,2):
                                xx1=xx+1
                                spos = int(sword[xx1]) - 1
                                if (sword[xx] == wardle[spos]):
                                    lt=False
                            if(lt):
                                wd = ""
                                
                                syn = wordnet.synsets(wardle)
                                try:
                                    wd = syn[0].definition()
                                except IndexError:
                                    pass
                                finally:
                                    
                                    wardl = wardl  + wardle + ",     "
                                    count = count + 1
    wardl = wardl.rstrip(",")
    #print(wardl)
    mess = str(count) + " results, Happy Wordling!"
    aList = "".join(wardl)
    aList = aList.split(',')
    #print('DONE processing, returning')
    return aList