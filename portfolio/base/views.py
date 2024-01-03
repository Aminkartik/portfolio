from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

# def pdf_view(request):
#     with open('D:\Certificates\Full_Stack_Development.pdf', 'rb') as pdf:
#         response = HttpResponse(pdf.read(), content_type='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=Full_Stack_Development.pdf'
#         return response

def contact(request):
    return render(request, 'base/contact.html')