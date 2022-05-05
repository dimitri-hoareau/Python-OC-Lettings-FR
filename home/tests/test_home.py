import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db  
def test_home_index_view():
    client = Client()
    path = reverse('home:index')
    response = client.get(path)

    assert response.status_code == 200
    assert b"<h1>Welcome to Holiday Homes</h1>" in response.content
    assertTemplateUsed(response, "home/index.html")