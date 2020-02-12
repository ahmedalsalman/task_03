from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[{

    "restaurant_name": "Fooders",
    "food_type": "Edible objects"}
    ,{"restaurant_name": "27 Brothers",
    "food_type": "Bakery"}
    ,{"restaurant_name": "pizzazo",
    "food_type": "Pizza"}
    ,

    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object": {
    "restaurant_name":"Fooders",
    "food_type":"Edible objects"

    }

    }
    return render(request, 'detail.html', context)
