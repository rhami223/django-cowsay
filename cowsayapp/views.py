from django.shortcuts import render, HttpResponse
from .forms import CowsayText
from .models import History
from subprocess import check_output

#Howard Post assisted me in completing the assignment

def index(request):
    output = ""
    if request.method == "POST":
        form = CowsayText(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            History.objects.create(
                textline = data.get("textline")
            )
            text = data.get("textline")
            output = check_output(["cowsay", text], text=True)
    form = CowsayText()
    return render(request, "index.html", {"form": form, "output": output})
 
def history_view(request):
    data = History.objects.all()[:10]
    return render(request, "history.html", {"data": data})