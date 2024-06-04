from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method=="POST":
        title=str(request.POST.get('title'))
        fir_name=str(request.POST.get('first'))
        las_name=str(request.POST.get('last'))
        body=str(request.POST.get('body'))
        print(f'{title}\n{fir_name} {las_name}\n\t{body}')
    return render(request,'main.html')