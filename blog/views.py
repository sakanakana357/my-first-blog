from django.shortcuts import render


#render
def post_list(request):
    return render(request, "blog/post_list.html", {})