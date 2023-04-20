from django.test import TestCase, Client
from django.urls import reverse
from .models import Article

# Create your tests here.


class MyModelListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("my_model_list")

    def test_view_returns_200_and_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my_model_list.html")

    def test_view_displays_all_articles(self):
        article1 = Article.objects.create(name="Article 1", default_language="en", title={"en": "Title 1"})
        article2 = Article.objects.create(name="Article 2", default_language="es", title={"es": "Título 2"})
        response = self.client.get(self.url)
        self.assertContains(response, article1.name)
        self.assertContains(response, article2.name)


class MyModelCreateViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("my_model_create")

    def test_view_returns_200_and_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my_model_form.html")

    def test_view_creates_article(self):
        data = {
            "name": "New Article",
            "default_language": "en",
            "title": {"en": "New Title"}
        }
        response = self.client.post(self.url, data=data, follow=True)
        self.assertContains(response, data["name"])
        self.assertContains(response, data["default_language"])


class MyModelUpdateViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.article = Article.objects.create(name='Article 1', default_language='en', title={'en': 'Title 1'})
        self.url = reverse('my_model_update', kwargs={'pk': self.article.pk})

    def test_view_updates_article_and_redirects_to_list_view(self):
        data = {
            "name": "Updated Article",
            "default_language": "fr",
            "title": {"fr": "Title modifié"}
        }
        response = self.client.post(self.url, data=data, follow=True)
        self.assertContains(response, data["name"])
        self.assertContains(response, data["default_language"])