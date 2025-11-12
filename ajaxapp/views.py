from django.shortcuts import render
import time
from django.http import JsonResponse

# Create your views here.
def ajax_index(request):
    return render(request,"ajax_index.html")

def ajax_test(request):
    if request.method == "GET":
        time.sleep(30)
        return JsonResponse({"message" : "GET method is not allowed"})
    return JsonResponse({"message": "POST method is called"})


def visualization(request):
    return render(request, "visualization.html")

def line(request):
    # Get Data in DB
    # ['data1', 30, 200, 100, 400, 150, 250],
    data = ['data1', 10.4, 50, 25.6, 124]
    return JsonResponse(data,safe=False)

def pie(request):
    # [['A', 30], ['B', 50], ['C', 20],]
    data = [['A', 10], ['B', 10.5], ['C', 5],]
    return JsonResponse(data,safe=False)

def getChartdata(request):
    data1 = [30, 200, 100, 400, 150, 250]
    data2 = [30, 200, 100, 400, 150, 250]

    data = {
        'data1':data1,
        'data2':data2
    }

    return JsonResponse(data)
