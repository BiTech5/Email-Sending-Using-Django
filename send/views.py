from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if request.method=="POST":
        title=str(request.POST.get('title'))
        fir_name=str(request.POST.get('first'))
        las_name=str(request.POST.get('last'))
        body=str(request.POST.get('body'))
        send_mail(
        title,
        f"{fir_name} {las_name}\n\n\t\t{body}",
        "from@gmail.com",
        ["to@gmail.com"],
        fail_silently=False,
        )
        print(f'{title}\n{fir_name} {las_name}\n\n\t\t{body}')
    return render(request,'main.html')
