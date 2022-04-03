def userDefDict():
    myDict = {}
    for i in range(21):
        myDict[i] =  i**2
    #print(myDict)
    return myDict.keys()
print(userDefDict())