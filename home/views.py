from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Returns the landing page
    """

    return render(request, 'index.html')