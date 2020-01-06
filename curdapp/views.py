from django.shortcuts import render
from curdapp.models import productData
from django.http.response import HttpResponse


def Home(request):
    return render(request, 'Home.html')

def createview(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        pname = request.POST.get("pname")
        p_cost = request.POST.get("pcost")
        p_class = request.POST.get("pclass")
        nop = request.POST.get("nop")
        cname = request.POST.get("cname")
        mob = request.POST.get("mobile")
        email1 = request.POST.get("email")
        mfd = request.POST.get("mdate")
        exp = request.POST.get("edate")

        data = productData(
                product_id=pid,
                product_name=pname,
                product_cost=p_cost,
                product_class=p_class,
                no_of_product=nop,
                manufacture_date=mfd,
                expiry_date=exp,
                customer_name=cname,
                mobile=mob,
                email=email1
            )
        data.save()

        return render(request, 'curd_insert.html')
    else:

        return render(request, 'curd_insert.html')

def retrieveview(request):
    data = productData.objects.all()
    return render(request, 'curd_retrieve.html', {'data': data})

def updateview(request):
    if request.method == "POST":
        product_id = request.POST.get('pid')
        product_cost = request.POST.get('pcost')
        pro_id = productData.objects.filter(product_id=product_id)
        if not pro_id:
            return HttpResponse("ID is not available")
        else:
            pro_id.update(product_cost=product_cost)
            return render(request, 'curd_update.html')
    else:
        return render(request,'curd_update.html')


def deleteview(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        Pro_id = productData.objects.filter(product_id=pid)
        if not Pro_id:
            return HttpResponse("Product Id is not Available")
        else:
            Pro_id.delete()
            return render(request,'curd_delete.html')
    else:
        return render(request, 'curd_delete.html')