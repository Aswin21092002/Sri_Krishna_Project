from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save()
            return redirect('complaint_success')
    else:
        form = ComplaintForm()

    return render(request, 'complaints/submit_complaint.html', {'form': form})

def complaint_success(request):
    return render(request, 'complaints/complaint_success.html')

def resolve_complaint(request, complaint_id):
    complaint = Complaint.objects.get(pk=complaint_id)
    if request.method == 'POST':
        complaint.is_resolved = True
        complaint.save()
        complaint.notify_shop()
        return redirect('complaint_resolved')
    return render(request, 'complaints/resolve_complaint.html', {'complaint': complaint})

def complaint_resolved(request):
    return render(request, 'complaints/complaint_resolved.html')


