from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, DetailView
from .parser import parsing
from .models import TestModel




class BookListView(ListView):
    model = TestModel
    paginate_by = 10
    template_name = 'megatest/gogi.html'


class NamesDetails(DetailView):
    model = TestModel
    slug_field = 'slug'
    template_name = 'megatest/vasya.html'

    def post(self, request, *args, **kwargs):
        if 'salam' in request.POST:
            for key, value in kwargs.items():
                print(key, value)
            print('Метот ПОСТ ',kwargs, args)
            print(request.POST['salam'])
            return HttpResponse('Бандиты ПОСТ')

        return render(request, 'megatest/vasya.html')


    def get(self, request, *args, **kwargs):

        if 'privet' in request.GET:
            print('Метот гет ' * 100)
            print(request.GET['privet'])
            return HttpResponse('Здарова бандиты')

        return render(request, 'megatest/vasya.html')


def pooling(request):
    names = TestModel.objects.all()
    for name in names:
        name.slug = str(name)
        name.save()
    return render(request, 'megatest/testmodel_list.html')
