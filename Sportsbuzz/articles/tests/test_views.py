import datetime

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.utils import timezone

from users.models import User
from articles.models import Article, Article_detail, Category, Comment



class TestViews(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            article_id=12345,
            heading="test heading",
            article_link="https://www.sportskeeda.com/cricket/i-fear-the-hundred-indian-test-series-michael-vaughan-rishabh-pant-tests-positive-covid-19?ref=homepage",
            category="cricket",
            date_posted=timezone.now(),
            img_url="https://staticg.sportskeeda.com/editor/2021/07/ec92f-16263421242054-800.jpg"
        )
        self.user = User.objects.create_user(
            username='username', email='email@app.com')
        self.user.set_password('password12!')
        self.user.is_email_verified = True
        self.user.save()

        self.article_detail = Article_detail.objects.create(
            article_detail_id=self.article,
            heading="test heading",
            img_url="https://staticg.sportskeeda.com/editor/2021/07/ec92f-16263421242054-800.jpg",
            date_posted=timezone.now(),
            description=str({
                'description': ['description1', 'description2', 'description3']
            }),
            tweet_url=str({
                'tweets': ['tweet1', 'tweet2']
            })

        )

    def test_should_show_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/home.html')

    def test_should_show_latest_articles_page(self):
        response = self.client.get(reverse('latest-article'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/latest_article.html')

    def test_should_show_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/about.html')

    def test_should_show_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/contact.html')

    def test_user_can_contact_website(self):
        response = self.client.post(reverse('contact'), data={
            'name': 'test',
            'email': 'test@123',
            'contact-number': '1234567890',
            'message': 'hii there',
            'total_message': 'hii there'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/contact.html')

    def test_should_show_article_detail_page(self):

        self.article_detail.likes.add(self.user.id)

        response = self.client.get(reverse('article-detail', args=(self.article.article_id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_detail.html')
        self.assertEqual(str(self.article), self.article.heading)

    def test_should_show_category_page(self):
        cat = Category.objects.create(
            name="cricket"
            )
        response = self.client.get(reverse('category', args=(cat.name,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/categories.html')
        self.assertEqual(str(cat), cat.name)

    def test_should_show_comments(self):
        '''creating article instance'''
        article_id2 = Article.objects.only('article_id').get(article_id=self.article.article_id)
        self.client.post(reverse("login"), {
            'username': self.user.username,
            'password': 'password12!'
        })
        self.article_detail.likes.add(self.user.id)

        comment = Comment.objects.create(
            article=article_id2,
            name=self.user,
            body='First comment',
            date_added=timezone.now(),

        )
        response = self.client.post(reverse('add-comment', args=(self.article.article_id,)))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('article-detail', args=(self.article.article_id,)))

    def test_user_can_likes(self):
        # self.article_detail.likes.add(self.user.id)
        self.client.post(reverse("login"), {
            'username': self.user.username,
            'password': 'password12!'
        })
        print(self.article.article_id)

        response = self.client.post(reverse('like_article', args=(self.article.article_id,)), data={
            'post_id': self.article.article_id,
        })
        self.assertEqual(response.status_code, 302)

    def test_user_can_unlikes(self):
        self.client.post(reverse("login"), {
            'username': self.user.username,
            'password': 'password12!'
        })
        self.article_detail.likes.add(self.user.id)

        response = self.client.post(reverse('like_article', args=(self.article.article_id,)), data={
            'post_id': self.article.article_id,
        })
        self.assertEqual(response.status_code, 302)













