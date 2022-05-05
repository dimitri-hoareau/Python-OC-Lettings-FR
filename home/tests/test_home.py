import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db  
def test_book_infos_view():
    client = Client()
    path = reverse('home:index')
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "home/index.html")