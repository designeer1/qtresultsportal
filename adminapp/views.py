from django.shortcuts import render, redirect
from .models import Result

def admin_dashboard(request):
    results = Result.objects.all().order_by('-id')
    return render(request, "adminapp/dashboard.html", {"results": results})


def add_result(request):
    if request.method == "POST":
        title = request.POST.get("title")
        file = request.FILES.get("file")
        active = True if request.POST.get("is_active") == "on" else False

        Result.objects.create(
            title=title,
            file=file,
            is_active=active
        )

        return redirect("admin_dashboard")

    return render(request, "adminapp/add_result.html")

from django.shortcuts import render, redirect, get_object_or_404
import os

def edit_result(request, id):
    result = get_object_or_404(Result, id=id)

    if request.method == "POST":
        result.title = request.POST.get("title")
        result.is_active = True if request.POST.get("is_active") == "on" else False

        if request.FILES.get("file"):  # if new file uploaded
            if os.path.exists(result.file.path):
                os.remove(result.file.path)  # delete old file
            result.file = request.FILES["file"]

        result.save()
        return redirect("admin_dashboard")

    return render(request, "adminapp/edit_result.html", {"result": result})


def delete_result(request, id):
    result = get_object_or_404(Result, id=id)

    # Delete file
    try:
        if os.path.exists(result.file.path):
            os.remove(result.file.path)
    except:
        pass

    result.delete()
    return redirect("admin_dashboard")
