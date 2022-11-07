import rest_framework
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ukol.serializers import *
import ast
from django.apps import apps
from ukol.models import *


"""
dict of serializers. Key is model
"""
DICT_OF_SERIALIZERS = {
    "Product": ProductSerializer,
    "Attribute": AttributeSerializer,
    "Catalog": CatalogSerializer,
    "ProductImage": ProductImageSerializer,
    "Image": ImageSerializer,
    "AttributeName": AttributeNameSerializer,
    "AttributeValue": AttributeValueSerializer,
    "ProductAttributes": ProductAttributesSerializer,
}


# TODO: change function to class then store the logic to serialzier
@csrf_exempt
def import_data(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
        except rest_framework.exceptions.ParseError:
            return JsonResponse(
                {"error": "Data are not in correct JSON format"}, status=400
            )
        # parsing the data by key, if key is correct then update_serializer method is called and data are write
        # down to correct model
        for i in data:
            for key, val in i.items():
                if key == "AttributeName":
                    update_serializer(AttributeNameSerializer, AttributeName, val)
                elif key == "Product":
                    try:
                        val["published_on"]
                    except KeyError:
                        val["published_on"] = None
                    update_serializer(ProductSerializer, Product, val)
                elif key == "AttributeValue":
                    update_serializer(AttributeValueSerializer, AttributeValue, val)
                elif key == "Image":
                    update_serializer(ImageSerializer, Image, val)
                elif key == "ProductImage":
                    update_serializer(ProductImageSerializer, ProductImage, val)
                elif key == "Attribute":
                    update_serializer(AttributeSerializer, Attribute, val)
                elif key == "Catalog":
                    update_serializer(CatalogSerializer, Catalog, val)
                elif key == "ProductAttributes":
                    update_serializer(
                        ProductAttributesSerializer, ProductAttributes, val
                    )
        return HttpResponse("Success! Data were imported", status=201)


def create_list_of_models() -> dict:
    return {
        model.__name__: model
        for model in apps.get_models(include_auto_created=False, include_swapped=False)
    }


@csrf_exempt
def detail_of_model(request, name_of_model):
    if request.method == "GET":
        dict_of_models = create_list_of_models()
        list_of_models = []

        if name_of_model == "Catalog":
            return change_list_in_catalog_model(True)

        else:
            for key, value in dict_of_models.items():
                list_of_models.append(key)
            if name_of_model in list_of_models:
                class_of_model = apps.get_model(
                    app_label="ukol", model_name=name_of_model
                )
                serializer = DICT_OF_SERIALIZERS[name_of_model](
                    class_of_model.objects.all(), many=True
                )
            else:
                return JsonResponse(
                    {"error": f"Cannot find the {name_of_model} in models"}, status=400
                )
            return JsonResponse(serializer.data, safe=False)


def change_list_in_catalog_model(all: bool, catalog_id=None):
    if all:
        serializer = Catalog.objects.all().values()[0]
    else:
        try:
            serializer = Catalog.objects.filter(id=catalog_id).values()[0]
        except IndexError:
            return JsonResponse(
                {"error": f"Cannot find id {catalog_id} in Catalog"}, status=400
            )
    serializer["products_ids"] = ast.literal_eval(serializer["products_ids"])
    serializer["attributes_ids"] = ast.literal_eval(serializer["attributes_ids"])
    return JsonResponse(serializer, safe=False)


"""
endpoint for geting details about model. Name of models are store in dict_of_models automatically. TO DO: remove auth,
admin, etc... from dict_of_models
"""


def detail_of_value(request, name_of_model, id):
    if request.method == "GET":
        dict_of_models = create_list_of_models()
        list_of_models = []

        if name_of_model == "Catalog":
            return change_list_in_catalog_model(False, id)

        else:
            for key, value in dict_of_models.items():
                list_of_models.append(key)
            if name_of_model in list_of_models:
                class_of_model = apps.get_model(
                    app_label="ukol", model_name=name_of_model
                )
                serializer = DICT_OF_SERIALIZERS[name_of_model](
                    class_of_model.objects.filter(id=id), many=True
                )
            else:
                return JsonResponse(
                    {"error": f"Cannot find {name_of_model} in models"}, status=400
                )
            return JsonResponse(serializer.data, safe=False)


"""
check if id already in db, if yes ignore it. Maybe business logic is different. Should be update it? 
Better create special update endpoint
"""


def update_serializer(name_of_serializer, name_of_model, val):
    queryset = name_of_model.objects.filter(id=val["id"])
    if not queryset:
        serializer_name = name_of_serializer(data=val)
        if serializer_name.is_valid():
            serializer_name.save()
