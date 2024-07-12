from django.shortcuts import render
from .models import Recipe
import ast
import json

def search(request):
    query = request.GET.get('q')
    matching_items = []
    if query:
        # Use raw SQL to search for the query within the items field
        recipes = Recipe.objects.raw(
            'SELECT * FROM restaurant_app_recipe WHERE items LIKE %s', 
            ['%' + query + '%']

        )
        for recipe in recipes:
            data = json.loads(recipe.items)
            recipe_items = ast.literal_eval(data)
            for item, price in recipe_items.items():
                if query.lower() in item.lower():
                    matching_items.append({
                        'name' : item,
                        'price' : price
                    })
                    break  

    else:
        recipes = []
    return render(request, 'restaurant_app/search.html', {'recipes': recipes, 'query': query , 'matching_items' : matching_items } )



#  restaurant_app/views.py
# from django.shortcuts import render
# from .models import Recipe
# from django.db.models import Q

# def search(request):
#     query = request.GET.get('q')
#     results = []
#     if query:
#         recipes = Recipe.objects.filter(Q(items__icontains=query))
#         for recipe in recipes:
#             matching_items = {item: price for item, price in recipe.get_items.items() if query.lower() in item.lower()}
#             if matching_items:
#                 results.append({
#                     'name': recipe.name,
#                     'location': recipe.location,
#                     'items': matching_items
#                 })
#     return render(request, 'search.html', {'query': query, 'results': results})

