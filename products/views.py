# from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, object_list=None, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, *kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)



class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"


    def get_context_data(self, *args, object_list=None, **kwargs):
      context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
      print(context)
      return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get("pk")

        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product not found")
        return instance

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get("pk")
        return Product.objects.filter(pk=pk)

def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk = pk)  # id
    # instance = get_object_or_404(Product, pk = pk)
#     try:
#         instance = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         raise Http404("Product not found test http404")
# #        print("Product not found")
#     except:
#         print("exception raised")

    # queryset = Product.objects.all()

    instance = Product.objects.get_by_id(pk)

    print(instance)
    print(type(instance))

    if instance is None:
        raise Http404("Product does not exist")

    # print(instance)
    # print(type(instance))
    # qs = Product.objects.filter(id=pk)
    #
    # if qs.exists() and qs.count() ==1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product not exist - test of qs")


    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)