from django.http import HttpResponse
from django.shortcuts import render
from .import websiteanalyzer as ws
from django.template import Context, loader
import pandas as pd
from .import analyzer as an
import json


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




def analyzerviews(request):
    try:
        currenturl=request.POST.__getitem__("currenturl")
        print(currenturl)
        matchinpercentagedict,figname, detaillist= an.allfunctioncall(currenturl)
        #print(matchinpercentagedict,allresultlist,figname)
        #matchinpercentagedict = json.dumps(matchinpercentagedict)
        keyname = list(matchinpercentagedict.keys())
        matchvalue = list(matchinpercentagedict.values())
        data = {"currenturl":currenturl, "keyname":keyname, "matchvalue":matchvalue,"figname":str(figname) +".png"}
        data2 = {"detaillist":detaillist}
        return render(request,"analyzer.html",{'data':data,"data2":data2})
    except:
        data = {'currenturl':"", "matchingpercentage":"","allresultlist":"","figname":""}
        return render(request,"analyzer.html",{'data':data})





def mypath(request):
    if(request.GET):
        url=request.GET["url"]
        print(url)
        return render(request,url)
    return HttpResponse("No Get")






