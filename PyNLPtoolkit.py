#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Necessary Imports 
import re
import pandas as pd

# Reference Number Lists
numbersList = ['zeroth','first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth',
               'eleventh','twelvth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth',
               'twentieth','thirtieth','fourtieth,','fiftieth','sixtieth','seventieth','eightieth','nintieth',
               'hundreth','thousandth','millionth','billionth','trillionth']

uniqueNumbersList = ['zero','one','two','three','four','five','six','seven','eight','nine','ten',
                     'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',
                     'twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety',
                     'hundred','thousand','million','billioin','trillion']

numbSuffixList = ['st','nd','rd','th']

numbWordList = ['1st','2nd','3rd','13th','23rd','31st','222nd','65th','99th','4,256th',
                '0.1','0.93','0.21','0.00','-1.10','0.001','0.1234','3.14159',
                '3,265','5,384','26,221','469,365','1,000,000','2,000,000,000',
                '644.355.222,01','3,000,000,000,000','965,000,332,000,001']


# In[56]:


# Functions List

# Returns a list of all phone numbers (handles international) in a given sentence/string
def extract_phone_numb(inputString):
    extractedNumbList = re.findall('((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))',inputString)
    df = pd.DataFrame(extractedNumbList,columns =['Phone_Numbers'])
    display(df)
    return extractedNumbList

# Returns a list of all emails (handles non-'.com' domains) in a given sentence/string
def extract_emails(inputString):
    extractedEmailList = re.findall('\S+@\S+', inputString)
    for e,email in enumerate(extractedEmailList):
        emailSplit = email.split('.')
        domainSub = re.sub(r'[^\w\s]', '', emailSplit[1])
        extractedEmailList[e] = f'{emailSplit[0]}.{domainSub}'
    df = pd.DataFrame(extractedEmailList,columns =['Email_Addresses'])
    display(df)
    return extractedEmailList

# 
def numb_list_to_word_list(stringList):
    wordList = []
    for string in stringList:
        negativeNumb = False
        placeNumb = False
        stringLenght = len(string)
        if '-' in string:
            negativeNumb = True
        for suf in numbSuffixList:
            if suf in string:
                placeNumb = True
        if placeNumb:
            updatedString = numb_to_string(string[:-2], placeNumb)
        elif negativeNumb:
            updatedString = numb_to_string(string.replace('-',''),placeNumb)
            updatedString = 'negative-'+updatedString
        else:
            updatedString = numb_to_string(string, placeNumb)
        wordList.append(updatedString)
    df = pd.DataFrame(list(zip(stringList, wordList)),columns =['Input', 'Output'])
    display(df)
    return wordList

# Returns a tokenized number-words for a decimal number segment
def decimal_parse(string,PrePostDesignation,placeNumb):
    finalNumbWord = []
    intNumb = int(string)
    strNumbList = []
    if len(string) == 1:
        tempNumbWord = uniqueNumbersList[intNumb]
        if placeNumb:
            tempNumbWordIndex = uniqueNumbersList.index(tempNumbWord)
            tempNumbWord = numbersList[tempNumbWordIndex]
        finalNumbWord.append(tempNumbWord)
    elif len(string) == 2:
        intNumbList = [int(d) for d in str(intNumb)]
        for n, numb in enumerate(intNumbList):
            numbIndex = int(numb)
            if n == 0:
                if numbIndex == 1:
                    pass
                elif numbIndex < 10:
                    if numbIndex == 0:
                        tenIndex = 0
                    else:
                        tenIndex = 18+numbIndex
                    strNumbList.append(uniqueNumbersList[tenIndex])
                else:
                    print(f'ERROR NUMBER OUT OF RANGE: {numb}')
            elif n == 1:
                if int(intNumbList[n-1])==1:
                    numbIndex = int(intNumbList[n])+10
                    strNumbList.append(uniqueNumbersList[numbIndex])
                else:
                    strNumbList.append(uniqueNumbersList[numb])                    
            else:
                print('ERROR IN TENS NUMBER RANGE PARSE')
        tempNumbWord = "-".join([str(i) for i in strNumbList])
        if PrePostDesignation == 'pre':
            tempNumbWord = tempNumbWord.replace('-zero','')
            tempNumbWord = tempNumbWord.replace('zero-','')
        elif PrePostDesignation =='post':
            pass
        else:
            print('ERROR PRE/POST DESIGNATION NOT SET')
        if placeNumb:
            tempNumbWord = tempNumbWord.replace('-point-zero','')
            try:
                tempNumbWordList = tempNumbWord.split('-')
                tempNumbWordListLen = len(tempNumbWordList)
                tempNumbWordLast = tempNumbWordList[tempNumbWordListLen-1]
                placeNumbIndex = uniqueNumbersList.index(tempNumbWordLast)
                if intNumb < 20:
                    tempNumbWordPlace = numbersList[placeNumbIndex]
                    tempNumbReplace = tempNumbWordLast
                else:
                    tempNumbWordPlace = '-'+numbersList[placeNumbIndex]
                    tempNumbReplace = '-'+tempNumbWordLast
                tempNumbWord = tempNumbWord.replace(tempNumbReplace,tempNumbWordPlace)
            except ValueError:
                print(f'ERROR IN PLACE NUMBER: {tempNumbWord}')
        finalNumbWord.append(tempNumbWord)
    elif len(string) == 3:
        intNumbList = [int(d) for d in string]
        strNumbList = []
        for n, numb in enumerate(intNumbList):
            numbIndex = int(numb)
            if n == 0:
                if numbIndex == 0:
                    strNumbList.append('zero')
                elif numbIndex < 10:
                    hundString = f'{uniqueNumbersList[numbIndex]}-{uniqueNumbersList[28]}'
                    strNumbList.append(hundString)
                else:
                    print(f'ERROR NUMBER OUT OF RANGE: {numb}')
            elif n == 1:
                if numbIndex == 0:
                    strNumbList.append('zero')
                elif numbIndex == 1:
                    pass
                elif numbIndex < 10:
                    tenIndex = 18+numbIndex
                    strNumbList.append(uniqueNumbersList[tenIndex])
                else:
                    print(f'ERROR NUMBER OUT OF RANGE: {numb}')
            elif n == 2:
                if int(intNumbList[n-1])==1:
                    numbIndex = int(intNumbList[n])+10
                    strNumbList.append(uniqueNumbersList[numbIndex])
                else:
                    strNumbList.append(uniqueNumbersList[numb])
            else:
                print('ERROR IN HUNDRED NUMBER RANGE PARSE')
        tempNumbWord = "-".join([str(i) for i in strNumbList])
        if PrePostDesignation == 'pre':
            tempNumbWord = tempNumbWord.replace('-zero','')
            tempNumbWord = tempNumbWord.replace('zero-','')
        elif PrePostDesignation =='post':
            pass
        else:
            print('ERROR PRE/POST DESIGNATION NOT SET')
        if placeNumb:
            tempNumbWord = tempNumbWord.replace('-point-zero','')
            try:
                tempNumbWordList = tempNumbWord.split('-')
                tempNumbWordListLen = len(tempNumbWordList)
                tempNumbWordLast = tempNumbWordList[tempNumbWordListLen-1]
                placeNumbIndex = uniqueNumbersList.index(tempNumbWordLast)
                tempNumbWordPlace = '-'+numbersList[placeNumbIndex]
                tempNumbWord = tempNumbWord.replace('-'+tempNumbWordLast,tempNumbWordPlace)
            except ValueError:
                print(f'ERROR IN PLACE NUMBER: {tempNumbWord}')
        finalNumbWord.append(tempNumbWord)
    else:
        intNumbList = [finalNumbWord.append(uniqueNumbersList[int(numb)]) for numb in str(intNumb)] 
    return finalNumbWord

# Returns a compiled number-word as string from a tokenized decimal number input
def numb_to_string(inputNumb, placeNumb):   
    deciCount = inputNumb.count('.')
    # Check to see if number fits American styling
    if deciCount < 2:
        finalNumbWord = number_parse(inputNumb, placeNumb)
    # Check to see if number fits European styling
    elif deciCount > 1:
        inputNumb = inputNumb.replace(',',"'")
        inputNumb = inputNumb.replace('.',',')
        inputNumb = inputNumb.replace("'",'.')
        finalNumbWord = number_parse(inputNumb, placeNumb)    
    else:
        print('ERROR IN DECICOUNT/NUMBER STYLING')
    #print(f'Unknown Style Number: {u}')
    if '-zero-billion' in finalNumbWord:
        finalNumbWord = finalNumbWord.replace('-zero-billion','')
    if '-zero-million' in finalNumbWord:
        finalNumbWord = finalNumbWord.replace('-zero-million','')
    if '-zero-thousand' in finalNumbWord:
        finalNumbWord = finalNumbWord.replace('-zero-thousand','')
    if '-zero-point-zero' in finalNumbWord:
        finalNumbWord = finalNumbWord.replace('-zero-point-zero','')
    finalNumbWord = finalNumbWord.replace(', ','-')
    if placeNumb:
        finalNumbWord = finalNumbWord.replace('-point-zero','')
    return finalNumbWord

# Returns a compiled number-word from a number input (handles EU and US numbers )
def number_parse(inputNumb, placeNumb):
    deciSplitList = inputNumb.split('.')  
    preDeciList = deciSplitList[0].split(',')
    preDeciListLen  = len(preDeciList)
    tempPreDeci = [decimal_parse(deci,'pre',placeNumb) for deci in preDeciList]    
    if  preDeciListLen == 1:
        finalPreDeci= f'{tempPreDeci[0]}-'
    elif preDeciListLen == 2:
        finalPreDeci= f'{tempPreDeci[0]}-thousand-{tempPreDeci[1]}-'
    elif preDeciListLen == 3:
        finalPreDeci= f'{tempPreDeci[0]}-million-{tempPreDeci[1]}-thousand-{tempPreDeci[2]}-'
    elif preDeciListLen == 4:
        finalPreDeci= f'{tempPreDeci[0]}-billion-{tempPreDeci[1]}-million-{tempPreDeci[2]}-thousand-{tempPreDeci[3]}-'
    elif preDeciListLen == 5:
        finalPreDeci= f'{tempPreDeci[0]}-trillion-{tempPreDeci[1]}-billion-{tempPreDeci[2]}-million-{tempPreDeci[3]}-thousand-{tempPreDeci[4]}-'
    else:
        print(f'ERROR Number above Trillions:\n{u}')
    try:
        postDeciList = [deciSplitList[1]]
        postDeciListLen = len(postDeciList)
        finalPostDeci = [decimal_parse(deci,'post',placeNumb) for deci in postDeciList]
        if finalPostDeci[0] == ['']:
            if postDeciList[0] == '01':
                finalPostDeci = 'zero-one'
    except IndexError:
        finalPostDeci = 'zero'
    if finalPreDeci == '[]-':
        finalPreDeci = finalPreDeci.replace('[]','zero')

    finalNumbWord = f'{finalPreDeci}point-{finalPostDeci}'
    finalNumbWord = finalNumbWord.replace("'",'')
    finalNumbWord = finalNumbWord.replace('[','')
    finalNumbWord = finalNumbWord.replace(']','')
    return finalNumbWord


# In[57]:


updatedList = numb_list_to_word_list(numbWordList)
print(updatedList)


# In[58]:


inputString= "You can reach us at researcher@gmail.com or learner@ppb.gov! Also try Consultants@critical.cons!"
extractedEmails = extract_emails(inputString)


# In[59]:


inputString= "You can reach us at 555-259-4289, 1-800-259-9480. (999)333.5524 and internationally at the following numbers +44-713-565-0757 or 53531138486!"
extractedPhoneNumbs = extract_phone_numb(inputString)

