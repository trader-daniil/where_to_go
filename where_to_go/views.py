from django.shortcuts import render

def show_phones(request):
    return render(
        request=request,
        template_name='mainpage.html',
    )
