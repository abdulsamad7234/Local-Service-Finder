from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ServiceForm
from .models import Category, Service


def home(request):
    featured_categories = Category.objects.annotate(
        service_count=Count("services", filter=Q(services__is_approved=True))
    ).filter(service_count__gt=0)[:4]
    recent_services = Service.objects.filter(is_approved=True).select_related("category")[:6]

    context = {
        "featured_categories": featured_categories,
        "recent_services": recent_services,
    }
    return render(request, "services/home.html", context)


def service_list(request):
    services = Service.objects.filter(is_approved=True).select_related("category")
    categories = Category.objects.all()
    cities = Service.objects.filter(is_approved=True).values_list("city", flat=True).distinct()

    query = request.GET.get("q", "").strip()
    category_slug = request.GET.get("category", "").strip()
    city = request.GET.get("city", "").strip()

    if query:
        services = services.filter(
            Q(title__icontains=query)
            | Q(provider_name__icontains=query)
            | Q(description__icontains=query)
        )
    if category_slug:
        services = services.filter(category__slug=category_slug)
    if city:
        services = services.filter(city__iexact=city)

    paginator = Paginator(services, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "page_obj": page_obj,
        "categories": categories,
        "cities": sorted(cities),
        "query": query,
        "selected_category": category_slug,
        "selected_city": city,
    }
    return render(request, "services/service_list.html", context)


def service_detail(request, pk, slug):
    service = get_object_or_404(
        Service.objects.filter(is_approved=True).select_related("category"),
        pk=pk,
        slug=slug,
    )
    return render(request, "services/service_detail.html", {"service": service})


def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.is_approved = False
            service.save()
            messages.success(
                request,
                "Your service has been submitted and is waiting for admin approval.",
            )
            return redirect("services:service_list")
    else:
        form = ServiceForm()

    return render(request, "services/service_form.html", {"form": form})


def about(request):
    return render(request, "services/about.html")
