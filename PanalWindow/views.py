from django.shortcuts import render
from django.http import HttpResponse
from . import models

def Home(request):
    p_details = models.patient_info.objects.all().order_by('id')
    return render(request,'homepage.html',{'patient':p_details})


def Details(request):
    if request.POST:
        Name = request.POST.get('Name')
        Gender = request.POST.get('Gender') 
        Age = request.POST.get('age')
        disease = request.POST.get('d')
        bp = request.POST.get('bp')
        sugar = request.POST.get('sugar')
        oxygen = request.POST.get('o')
        status = request.POST.get('status')

        pat_obj = models.patient_info(Name = Name,Age=Age, Gender = Gender , Disease = disease
                                      ,bp = bp,sugar = sugar,oxygen = oxygen,status=status)
        pat_obj.save()
        print(pat_obj)
        p_details = models.patient_info.objects.all().order_by('id')
        return render(request,'homepage.html',{'patient':p_details})
    else:
        return render(request,'biodata.html')

def Delete(request,keyid):
    instance = models.patient_info.objects.get(id = keyid)
    instance.delete()
    p_details = models.patient_info.objects.all().order_by('id')
    return render(request,'homepage.html',{'patient':p_details})

def Edit(request,keyid):
    instance = models.patient_info.objects.get(id = keyid)
    if request.POST:
        
        instance.Age = request.POST.get('age')
        instance.Disease = request.POST.get('d')
        instance.Gender = request.POST.get('Gender')
        instance.bp = request.POST.get('bp')
        instance.sugar = request.POST.get('sugar')
        instance.oxygen = request.POST.get('o')
        instance.status = request.POST.get('status')
        instance.save()    
        p_details = models.patient_info.objects.all().order_by('id')
        return render(request,'homepage.html',{'patient':p_details})
        
    return render(request, 'editdata.html', {'ed': instance})
     
     