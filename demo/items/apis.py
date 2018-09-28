# -*- coding: utf-8 -*-
from django.forms.models import model_to_dict
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods

from items.models import Item

@require_http_methods(['GET'])
def items(request, *args, **kwargs):
    if request.method == 'GET':
        response = {'result': [model_to_dict(i) for i in Item.objects.all()]}
        return JsonResponse(response)
    else:
        raise Http404


@require_http_methods(['GET', 'POST', 'PUT', 'DELETE'])
def item(request, item_id, *args, **kwargs):
    try:
        if request.method == 'GET':
            items = Item.objects.get(id=item_id)
            response = {'meta': True, 'result': model_to_dict(items)}
            return JsonResponse(response)
        elif request.method == 'POST':
            item = Item.objects.create(**request.POST)
            response = {'meta': True, 'result': model_to_dict(item)}
            return JsonResponse(response)
        elif request.method == 'PUT':
            print(request.POST)
            item = Item.objects.filter(id=item_id).update(**request.POST)
            response = {'meta': True, 'result': model_to_dict(item)}
            return JsonResponse(response)
        elif request.method == 'DELETE':
            Item.objects.filter(id=item_id).delete()
            response = {'meta': True}
            return JsonResponse(response)
    except Exception as e:
        print(e)
        response = {'meta': False}
        return JsonResponse(response)
