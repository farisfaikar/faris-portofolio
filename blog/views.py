from django.shortcuts import render


# Create your views here.
def blog_index_view(request):
    context = {
    }
    return render(request, "blog/index.html", context=context)