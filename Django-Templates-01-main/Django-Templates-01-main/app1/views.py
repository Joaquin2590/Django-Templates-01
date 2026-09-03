from django.shortcuts import render

# Create your views here.
def vista1_app1(request):
    return render(request, 'app1/vista1_v1.html')

def vista2_app1(request):
    return render(request, 'app1/vista2_v2.html')