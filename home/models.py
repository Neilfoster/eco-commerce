from django.db import models

# Create your models here.
def index(request):
    """"Displays the index page """
    return render(request, "index.html")