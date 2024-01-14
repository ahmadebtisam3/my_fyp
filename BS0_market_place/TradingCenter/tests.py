from django.test import TestCase

# Create your tests here.
# Create your tests here.
from component import CardsWithButton, CardsWithTwoButton, CustomBth


def test_cards_with_button():
    html = CardsWithButton("/test/url", "test", "/test2/url", 200, 2).html
    assert 'src="/test/url"' in html
    assert '<div class="kchfht">test</div>' in html
    assert '<div class="bkzXJS">200</div>' in html


def test_cards_with_two_button():
    assert CardsWithTwoButton(
        "/url/img",
        "test",
        "test detail",
        "btn/url",
        "test button",
        "test btn",
        "btn_url",
        "test tool tip",
        "btn name",
    ).html


def test_custom_btn():
    html = CustomBth([{"url": "/test/btn1", "name": "btn"}]).html
    assert f"""<a class = "btn btn-danger mx-2" href="/test/btn1"> btn </a>""" in html
