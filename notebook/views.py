from django.shortcuts import render
from .forms import MyForm
from django.http import HttpResponse
from .models import Person


def index(request):
    if request.method == "POST":
        my_form = MyForm(request.POST)
        if my_form.is_valid():
            name = my_form.cleaned_data["name"]
            Person.objects.bulk_create([
                Person(name=name)
            ])
            people = Person.objects.in_bulk()
            people = [people[key].name for key in people][:20]
            my_form = MyForm()
            data = {'people': people, 'form': my_form}
            return render(request, "index.html", context=data)
        else:
            return HttpResponse("Invalid data")
    else:
        people = Person.objects.in_bulk()
        people = [people[key].name for key in people][:20]
        my_form = MyForm()
        data = {'people': people, 'form': my_form}
        return render(request, "index.html", context=data)


def my_dict(request):
    people = Person.objects.in_bulk()
    people = [people[key].name for key in people][:20]
    data = {'people': people}
    return render(request, "dict.html", context=data)
