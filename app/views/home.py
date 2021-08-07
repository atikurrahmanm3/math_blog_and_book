from django.shortcuts import render
from django.views import View
from app.models import Chapter
from app.models import Content


# Create your views here.
class Home(View):
    def get(self, request):
        chapter = Chapter.get_all_chapter()
        contents = Content.get_all_contents()
        print(request.GET)
        context = {'contents': contents, 'chapter': chapter}
        return render(request, 'home.html', context)
