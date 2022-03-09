from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from DjangoCRUDApp.models import Posts


@csrf_exempt
def add_post(request):
    title = request.POST.get("title")
    description = request.POST.get("description")
    # print(title,description)
    post = Posts(title=title, description=description)
    post.save()

    return HttpResponse("Inserted")


def read_post(request):
    posts = Posts.objects.all()
    response = []
    for post in posts:
        response.append({'title':post.title, 'description':post.description})
    return JsonResponse(response, safe=False)


@csrf_exempt
def update_post(request):
    id = request.POST.get("id")
    title = request.POST.get("title")
    post = Posts.objects.get(id=id)
    post.title = title
    post.save()

    return HttpResponse("Updated")

@csrf_exempt
def delete_post(request):
    id = request.POST.get("id")
    post = Posts.objects.get(id=id)
    post.delete()
    return HttpResponse("Deleted")

