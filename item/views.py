from django.shortcuts import render, get_object_or_404
from .models import item

def detail(request, pk):
	items = get_object_or_404(item, pk=pk)
	related_items = item.objects.filter(Category=items.Category, is_sold=False).exclude(pk=pk)[0:3]
	return render(request, 'item/detail.html', {
		'item': items,
		'related_items' : related_items,
	})