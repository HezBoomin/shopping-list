from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Kiel',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)