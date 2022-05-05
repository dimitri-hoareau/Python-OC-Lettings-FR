import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from lettings.models import Letting, Address

@pytest.mark.django_db  
def test_lettings_index_view():
    client = Client()
    path = reverse('lettings:index')
    response = client.get(path)

    assert response.status_code == 200
    assert b"<h1>Lettings</h1>" in response.content
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db  
def test_lettings_letting_view():
    client = Client()
    address_model = Address.objects.create(number = 588,
                                            street = "Argyle Avenue", 
                                            city = "East Meadow", 
                                            state = "NY", 
                                            zip_code = 11554, 
                                            country_iso_code = "USA")
    
    Letting.objects.create(title = "Underground Hygge",
                        address = address_model)
    path = reverse('lettings:letting', kwargs={'letting_id':1})
    response = client.get(path)

    assert response.status_code == 200
    assert b"<h1>Underground Hygge</h1>" in response.content
    assertTemplateUsed(response, "lettings/letting.html")
