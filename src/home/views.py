
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits

# *args, **kwargs -> These are the extra arguments and keyword arguments that may be passed other than the request. And these are used when the developer is not sure of the arguments taht will be passed.
def home_page_view(request, *args, **kwargs):

    qs = PageVisits.objects.all() # This retrieves everything
    page_qs = PageVisits.objects.filter(path=request.path) # This retrieves everything with the path equals to the current path.
    # PageVisits is a django model that represents a table in the database
    # .objects.all() is a queryset method that retrieves all records from the PageVisits table
    # The result is a queryset which is a list like structure containing all database records. 

    my_title = "Welcome"
    my_content = {
        "made": my_title,
        "all_pages_visit_count": qs.count(),
        "page_visit_count": page_qs.count()
    }
    
    path = request.path
    print("path", path)
    
    PageVisits.objects.create(path=request.path) # This creates a new row/record in the database, .create() saves immediately and .save() lets you modify the object before saving

    return render(request, "home.html", my_content)








