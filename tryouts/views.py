# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import TryoutEvent, TryoutRegistrant
from .forms import TryoutRegistrantForm
from django.core.paginator import Paginator


def tryoutsHome(request):

    events = TryoutEvent.objects.all().order_by('-date')

    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "tryoutList.html", {"page_obj": page_obj} )





# views.py
def tryout_register(request):
    if request.method == "POST":
        form = TryoutRegistrantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("tryout_success")
    else:
        form = TryoutRegistrantForm()

    return render(request, "tryout_register.html", {"form": form})


def tryout_success(request):

    return render(request, "tryout_success.html")
