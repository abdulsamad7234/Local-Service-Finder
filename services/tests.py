from django.test import TestCase
from django.urls import reverse

from .models import Category, Service


class ServiceViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Tutoring")
        self.approved_service = Service.objects.create(
            category=self.category,
            title="Math Tutor",
            provider_name="Aisha Khan",
            city="Lahore",
            phone="03001234567",
            email="aisha@example.com",
            address="Model Town",
            description="Private math tutoring for high school students.",
            is_approved=True,
        )
        Service.objects.create(
            category=self.category,
            title="Hidden Tutor",
            provider_name="Ali",
            city="Karachi",
            phone="03001112222",
            email="hidden@example.com",
            address="Clifton",
            description="This listing is pending approval.",
            is_approved=False,
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("services:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Math Tutor")

    def test_service_list_filters_by_city(self):
        response = self.client.get(reverse("services:service_list"), {"city": "Lahore"})
        self.assertContains(response, "Math Tutor")
        self.assertNotContains(response, "Hidden Tutor")

    def test_create_service_sets_pending_approval(self):
        response = self.client.post(
            reverse("services:service_create"),
            {
                "title": "Physics Tutor",
                "provider_name": "Usman",
                "category": self.category.pk,
                "city": "Islamabad",
                "phone": "03123456789",
                "email": "usman@example.com",
                "address": "F-8",
                "description": "Physics classes for college students.",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Service.objects.filter(title="Physics Tutor", is_approved=False).exists())

# Create your tests here.
