import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import Ad, Category


def index(request):
    return JsonResponse({
        "status": "ok"
    }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })

        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Category()
        category.name = category_data["name"]

        category.save()

        return JsonResponse({"status": "category saved"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ad.objects.all()

        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price
            })

        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ad()
        ad.name = ad_data["name"]
        ad.price = ad_data["price"]
        ad.author = ad_data["author"]
        ad.desc = ad_data["desc"]
        ad.address = ad_data["address"]

        ad.save()

        return JsonResponse({"status": "ad saved"}, status=200)


class CategoryView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        }, safe=False, status=200)


class AdView(View):
    def get(self, request, ad_id):
        ad = get_object_or_404(Ad, pk=ad_id)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "desc": ad.desc,
            "address": ad.address,
            "is_published": ad.is_published
        }, safe=False, status=200)
