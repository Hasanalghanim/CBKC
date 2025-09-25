# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import TryoutEvent, TryoutRegistrant
from .forms import TryoutRegistrantForm
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TryoutEvent,TryoutRegistrant
from .serializers import TryoutEventSerializer,TryoutRegistrantSerializer
from rest_framework.exceptions import NotFound
from rest_framework import status



def tryoutsHome(request):
    events = TryoutEvent.objects.all().order_by('-date')
    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "tryoutList.html", {"page_obj": page_obj,"seo_object": events.first()} )



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



class TryoutEventList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = TryoutEvent.objects.all()
        serializer = TryoutEventSerializer(queryset, many=True)
        return Response(serializer.data)
    

class TryoutRegistrantList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, tryout_event_id ):
        queryset = TryoutRegistrant.objects.filter(tryout_event_id=tryout_event_id)
        serializer = TryoutRegistrantSerializer(queryset, many=True)
        return Response(serializer.data)
    




class TryoutEventDetail(APIView):
    permission_classes = [IsAuthenticated]  
    def get(self, request, slug):
        tryout_event = get_object_or_404(TryoutEvent, slug=slug)
        serializer = TryoutEventSerializer(tryout_event)
        return Response(serializer.data)
    

    def put(self, request, slug):
        tryout_event = get_object_or_404(TryoutEvent, slug=slug)
        serializer = TryoutEventSerializer(tryout_event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)