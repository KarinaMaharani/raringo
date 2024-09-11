from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Karina Maharani',
        'class' : 'PBP A',
        'application' : 'Raringo',

        'product' : 'Eyeshadow Parastyles X Gone',
        'price': 75000,
        'description': 'Trio Best Selling Shades in our combined customer base',
        'tags': 'BEAUTY, LIFESTYLE',
        'ratings': 4.3

    }

    return render(request, "main.html", context)
