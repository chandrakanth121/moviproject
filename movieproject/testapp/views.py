from django.shortcuts import render
from testapp import forms
from testapp.models import moviemodel


# Create your views here.
def  indexview(request):
    return render(request,'testapp/index.html')

def addmovieview(request):
    form=forms.movieform()
    if request.method=='POST':
        form=forms.movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return indexview(request)
    return render(request,'testapp/addmovie.html',{'form':form})



def movielistview(request):
    movie_list=moviemodel.objects.all()
    my_dict={'movie_list':movie_list}
    return render(request,'testapp/movielist.html',context=my_dict)
