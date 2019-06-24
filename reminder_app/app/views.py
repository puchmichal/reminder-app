from django.http import HttpResponse
from django.template import loader
from .models import Person

def index(request):
    all_users = Person.objects.all()
    template = loader.get_template('app/index.html')
    context = {
        'all users': all_users
    }
    return HttpResponse(template.render(context, request))
