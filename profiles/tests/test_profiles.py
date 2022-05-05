import pytest

from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from profiles.models import Profile

@pytest.mark.django_db  
def test_profiles_index_view():
    client = Client()
    path = reverse('profiles:index')
    response = client.get(path)
    print(response.content)

    assert response.status_code == 200
    assert b"<h1>Profiles</h1>" in response.content
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db  
def test_profiles_profile_view():
    client = Client()
    
    model_user = User.objects.create(username = "HeadlinesGazer",
                        password = "Password1234!")

    Profile.objects.create(user = model_user,
                        favorite_city = "Buenos Aires")
    path = reverse('profiles:profile', kwargs={'username':"HeadlinesGazer"})
    response = client.get(path)

    assert response.status_code == 200
    assert b"<h1>HeadlinesGazer</h1>" in response.content
    assertTemplateUsed(response, "profiles/profile.html")