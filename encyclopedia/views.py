from fileinput import filename
from tkinter import Entry
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util, decoder, forms

import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def strn(request, entry):
    if entry == "random":
        entry2 = entry
        while entry2 == entry:
            entry = random.choice(util.list_entries())
    if util.get_entry(entry) != None:
        return render(request, "encyclopedia/strn.html", {
            "ime": entry,
            "entries": decoder.decode(str(util.get_entry(entry)).split("\n"))
        })
    else:
        return render(request, "encyclopedia/error.html", {
        "entries": util.list_entries()
        })

def rand(request):
    strn(request)

def new(request):
    if request.method == 'POST':
        form = forms.Newform(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data['text']

            filename = "".join(["entries",chr(92),str(title),".md"])
            try :
                filem = open(filename, "x")
                filem.write(text)
                filem.close()
                return HttpResponseRedirect("/"+str(title)+"/")
            except FileExistsError:
                return render(request, "encyclopedia/newerror.html", {
                    'form':form
                    })

    else:
        form = forms.Newform()
    
        return render(request, "encyclopedia/new.html", {
            'form':form
        })
      


def edit(request, entry):
    if request.method == 'POST':
        form = forms.Editform(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            filename = "".join(["entries",chr(92),str(entry),".md"])
            filem = open(filename, "w")
            filem.write(text)
            filem.close()
            return HttpResponseRedirect("/"+str(entry)+"/")

    else:
        
        datas = open("entries/"+str(entry)+".md", "r")
        content = []
        for i in range (100):
            content.append(datas.readline())
        form = forms.Editform(initial={'text': "".join(content)})
    
        return render(request, "encyclopedia/edit.html", {
            'form':form,
            "ime":entry
        })
      
def search(request):
    if request.method == 'POST':
            ulaz = request.POST["q"]
            list = []
            for one in util.list_entries():
                if (ulaz.upper() in one.upper()):
                    list.append(one)
            if list != []:
                return render(request, "encyclopedia/search.html", {
                    "list":list,
                    'ulaz':ulaz
                })
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries()
                })