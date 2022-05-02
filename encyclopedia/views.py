from django.shortcuts import render

from . import util, decoder

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
    return render(request, "encyclopedia/new.html")