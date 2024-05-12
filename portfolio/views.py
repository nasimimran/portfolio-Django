from django.http import HttpResponse
from django.template import loader
from .forms import ContactedForm


# Create your views here.
def portfolio(request):
    template = loader.get_template('index.html')
    temss = loader.get_template('contacss.html')

    if request.method == "POST":
        form = ContactedForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse(temss.render({}, request))
            except:
                pass
    else:
        form = ContactedForm()
    return HttpResponse(template.render({'form': form}, request))
