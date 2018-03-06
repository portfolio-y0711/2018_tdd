from django.shortcuts import render, redirect
from lists.models import Item, List

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    return redirect('/lists/%d/' % (list_.id,))

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,)) 

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'items': items})

def home_page(request):
    return render(request, 'home.html')