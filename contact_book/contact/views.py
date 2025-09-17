from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.db.models import Q

def contact_list(request):
    query = request.GET.get("q")
    if query:
        contacts = Contact.objects.filter(
            Q(name__icontains=query) | Q(phone__icontains=query)
        )
    else:
        contacts = Contact.objects.all()

    return render(request, "contactbook/contact_list.html", {"contacts": contacts, "query": query})

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()
    return render(request, "contactbook/contact_form.html", {"form": form, "title": "Add Contact"})

def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contactbook/contact_form.html", {"form": form, "title": "Update Contact"})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(request, "contactbook/contact_confirm_delete.html", {"contact": contact})
