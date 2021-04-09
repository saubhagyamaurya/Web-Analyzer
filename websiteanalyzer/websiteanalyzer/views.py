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
        filesname = os.listdir('F:\\ProjectDjango\\websiteanalyzer\\templates\Excel')
        internallinks,internallinkname,externallinks = ws.allFunctionCall(baseurl,currenturl)
        print(internallinks)
        data = {'baseurl':baseurl,'currenturl':currenturl,'processing':'processing','internallinks':list(internallinks),'internallinkname':list(filesname),'externallinks':list(externallinks)} 
        
        
        return render(request,"home.html",{'data':data})
    except:
        data = {'baseurl':"",'currenturl':"",'started':"","inernallinks":""}
        return render(request,"home.html",{'data':data})

def goToExcel(request):
    #url=request.GET['url']
    return render(request,"varanasikshetra_com_.html")


def abc(request):
    l=[1,2,3,4] 
    data = {'l':l}
    return render(request,'list.html',{'data':data})


