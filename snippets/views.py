from django.shortcuts import render

from .forms import SnippetForm
from .models import Snippet


# Create your views here.
def create_snippet(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SnippetForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect("/thanks/")
            instance = Snippet.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                code=form.cleaned_data["code"],
                language=form.cleaned_data["language"],
                author=request.user,  # Assuming the user is authenticated
            )
            instance.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SnippetForm()

    return render(request, "home.html", {"form": form})
