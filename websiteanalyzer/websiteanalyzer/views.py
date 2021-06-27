from django.http import HttpResponse
from django.shortcuts import render
from .import websiteanalyzer as ws
import os
from django.template import Context, loader
import pandas as pd


def homeviews(request):
    try:
        baseurl = request.POST.__getitem__("baseurl")
        currenturl = request.POST.__getitem__("currenturl")
        print(baseurl,currenturl)
        internallinks,internallinkname,externallinks = ws.allFunctionCall(baseurl,currenturl)
        df = pd.read_excel("F:\\ProjectDjango\\websiteanalyzer\\templates\Excel\main.xlsx",index_col=False)
        filesname = list(df["InternalLinksName"])
        print(internallinks, filesname)
        data = {'baseurl':baseurl,'currenturl':currenturl,'processing':'processing','internallinks':list(internallinks),'internallinkname':list(filesname),'externallinks':list(externallinks)}
        return render(request,"home.html",{'data':data})
    except:
        data = {'baseurl':"",'currenturl':"",'started':"","inernallinks":""}
        return render(request,"home.html",{'data':data})

def goToExcel(request):
    #url=request.GET['url']
    return render(request,"varanasikshetra_com_.html")

def mypath(request):
    if(request.GET):
        url=request.GET["url"]
        print(url)
        return render(request,url)
    return HttpResponse("No Get")
def abc(request):
    l=[1,2,3,4] 
    data = {'l':l}
    return render(request,'list.html',{'data':data})


