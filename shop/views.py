from django.shortcuts import render


def shop(request):
    name = 'gay'
    data = {
        'name': name,
    }
    return render(request=request, template_name='shop/index.html', context=data)
