from django.shortcuts import render

# Create your views here.


def main_view(request):
    context = {}

    return render(request=request, template_name='chat/main.html', context=context)
