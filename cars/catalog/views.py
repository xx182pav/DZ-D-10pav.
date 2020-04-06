from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import TemplateView
from django.template import loader

from catalog.models import Car


# class CarsView(TemplateView):
#     template_name = "index.html"

#     def get_context_data(self, **kwargs):
#         params = self.request.GET
#         query = Q()
#         print(params)
#         for key, value in params.items():
#             if value and key in vars(Car):
#                 query &= Q(**{key: value})
#         return {"cars": Car.objects.filter(query)}


def CarsList(request):
    template = loader.get_template('index.html')
    params = request.GET
    query = Q()
    # print(params)
    for key, value in params.items():
        if value and key in vars(Car):
            query &= Q(**{key: value})
            print(vars(Car))
    cars_data = {"cars": Car.objects.filter(query)}
    return HttpResponse(template.render(cars_data, request))