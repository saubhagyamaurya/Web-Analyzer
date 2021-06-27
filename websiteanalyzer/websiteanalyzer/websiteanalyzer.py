from nltk.corpus.reader import wordlist
import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup as bs
import pandas as pd 
import re
import lxml.html.clean
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords as sw



def getUrlContent(url):
    #Downloads and returns content
   return requests.get(url, timeout = 20).content

def findAllTag(url):
    #Find all HTML Tag on current web page
    taglist = set()
    html = getUrlContent(url)
    soup = bs(html,"html.parser")
    for tag in soup.find_all():
        tags = tag.name
        taglist.add(tags)
    return taglist 

def getUrls(baseurl,currenturl):
    # convert relative link in full link
    newurl = urljoin(baseurl, currenturl)
    html=getUrlContent(newurl)

    scraper = bs(html, 'html.parser')
    links=scraper.find_all("a")
    # inslize a blank set 
    internalurl=set()
    externalurl =set()
    for link in links:
        fulllink=urljoin(baseurl,link.get("href"))        
        if isInternalLink(baseurl,fulllink):
            internalurl.add(fulllink)
        else:
            externalurl.add(fulllink)
    #return founded url and add in foundurl set 
    return internalurl,externalurl


def isInternalLink(baseurl,currenturl):
    # verify link is internal or not
    #<a href = "http://abc.com/xyz"> text </a>
    baseurl=baseurl.lower().strip()
    currenturl=currenturl.lower().strip()
    if currenturl.startswith(baseurl):
        return True
    else:
        return False


def getLinks(baseurl,currenturl):
    # Find all type of links 
    internalurls=set()
    externalurl = set()
    visitedurls=set()
    remainingurls=set()
    internalurls.add(currenturl)
    remainingurls=internalurls.difference(visitedurls)
    n=len(remainingurls)
    while n>0:
        currenturl=remainingurls.pop()
        visitedurls.add(currenturl)
        foundurls,externalurl=getUrls(baseurl, currenturl)
        for i in externalurl:
            externalurl.add(i)
        for x in foundurls:
            internalurls.add(x)
        remainingurls=internalurls.difference(visitedurls)
        n = len(remainingurls)
    return internalurls,externalurl


def getInternalLinks(internallinks):
    # Replacing all the symbol
    intlinklist = []
    for link in internallinks:
        link = link.replace("http://","").replace("https://","").replace(".","_").replace("/","_").replace("#", "_")
        intlinklist = intlinklist + [link+".html"]
    return intlinklist

def getExternalLinks(externallinks):
    # this function creted for showing external ling
    for link in externallinks:
        print(link)
    return " "


def getUrlDetail(url,tagname):
    html = getUrlContent(url)
    scraper = bs(html,"html.parser")
    output = scraper.find_all("{}".format(tagname))
    l = []
    for i in range(0,len(output)):
        d = output[i].text
        l = l + [d]
    dict = {tagname:l}
    df = pd.DataFrame(dict)
    return df


def writeInExcel(baseurl,currenturl):
    internallinks,externallinks=getLinks(baseurl,currenturl)
    internallinkname = getInternalLinks(internallinks)
    df = pd.DataFrame()
    taglist = findAllTag(currenturl)
    for link,name in zip(internallinks,internallinkname):
        print(link)
        for tag in taglist:
            a = getUrlDetail(link,tag)
            df = df.append(a,ignore_index=False)
            #df.to_excel("templates//Excel//{}.xlsx".format(name),index=False)
            html = df.to_html(border=1)
            text_file = open("templates//Excel//{}".format(name),"w",encoding="utf-8")
            text_file.writelines('<meta charset = "UTF-8">\n')
            text_file.write(html)
            text_file.close()
            
        print(df)
    return ""



def cleanme(content):
  #Removing all tag and scripts from the scrapping data
    cleaner = lxml.html.clean.Cleaner(
        allow_tags=[''],
        remove_unknown_tags=False,
        style=True,
    )
    html = lxml.html.document_fromstring(content)
    html_clean = cleaner.clean_html(html)
    return html_clean.text_content().strip()



def contentProcessing(content):
  text_token = wt(content)
  #print(text_token)
  wordwithoutsw = [word for word in text_token if not word in sw.words()]
  wordswithfrequencies = nltk.FreqDist(wordwithoutsw)
  wordset = set(wordwithoutsw)
  #print(wordset)
  
  #print(type(wordswithfrequencies))
  keyvaluespairs = wordswithfrequencies.items()
  n = len(wordswithfrequencies)
  #wordswithfrequencies.plot(n,cumulative=False)
  return wordset,keyvaluespairs

"""
baseurl="http://varanasikshetra.com/"
"""
currenturl = "http://varanasikshetra.com/"


htmlpage = getUrlContent(currenturl)
content = cleanme(htmlpage)
wordset, keyvaluepairs = contentProcessing(content)

#print(keyvaluepairs)
travelset=set(["Sarovar","holiest","travel","Pandava","Rameshwar","temple","booking","Dharmic","Heritage","Mandirs","Ghats","Rivers","Ghat","River","Ganga","Viswanath","Prakriti","Hindus","Linga","Yatra"])
matches=travelset.intersection(wordset)
print("matchkeywords = ",matches)
newset={}
#print(type(keyvaluepairs))
for x in keyvaluepairs:
    if x[0] in matches:
        newset[x[0]]=x[1]
print("matchkeywordfrequency = ",newset)


newsetcount = len(newset)
keyvaluepairscount = len(keyvaluepairs)
matchingpercentage = (newsetcount/keyvaluepairscount)*100 

print("newsetcount = ",newsetcount)
print("keyValuepaircount = ",keyvaluepairscount)
print("matchingpercentage = ",matchingpercentage)

matcheskeys = list(newset.keys())
matchesvalues = list(newset.values())
#plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams.update({'font.size':9})
plt.bar(range(len(newset)), matchesvalues, tick_label=matcheskeys,color ='maroon',width=0.2)
plt.xlabel("Keyword Names")
plt.ylabel("Frequency of Keywords")
plt.title(currenturl)
plt.show()


def allFunctionCall(baseurl, currenturl):
    #baseurl="http://varanasikshetra.com/"
    #currenturl="http://varanasikshetra.com/"
    internallinks, externallinks=getLinks(baseurl, currenturl)
    internallinkname = getInternalLinks(internallinks)
    detail = {"InternalLinks": list(internallinks), "InternalLinksName": list(internallinkname)}
    df = pd.DataFrame(detail)
    df.to_excel("F://ProjectDjango//websiteanalyzer//templates//Excel//main.xlsx", index=False)
    #print(internallinks)
    writeInExcel(baseurl, currenturl)
    """
    html = getUrlContent(currenturl)
    content = cleanme(html)
    contentProcessing(content)"""
    return internallinks, internallinkname, externallinks
#print(allFunctionCall(baseurl,currenturl))
