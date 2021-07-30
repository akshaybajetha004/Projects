import datetime

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.utils import timezone

from users.models import User
from articles.models import Article, Article_detail, Category, Comment


class TestViews(TestCase):

    def setUp(self):
        self.arti = Article.objects.create(
            article_id=12345,
            heading="test heading",
            article_link="https://www.sportskeeda.com/cricket/i-fear-the-hundred-indian-test-series-michael-vaughan-rishabh-pant-tests-positive-covid-19?ref=homepage",
            category="cricket",
            date_posted=timezone.now()-datetime.timedelta(days=15),
            img_url="https://staticg.sportskeeda.com/editor/2021/07/ec92f-16263421242054-800.jpg"
        )
        self.user = User.objects.create_user(
            username='username', email='email@app.com')
        self.user.set_password('password12!')
        self.user.is_email_verified = True
        self.user.save()
        '''creating article instance'''

        self.comment = Comment.objects.create(
            article=self.arti,
            name=self.user,
            body='First comment',
            date_added=timezone.now(),

        )

    def test_for_when_publish_for_sec(self):
        article = Article.objects.create(
            date_posted=timezone.now(),
        )

        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_min(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(minutes=1),
        )

        self.comment.date_added = self.comment.date_added-timezone.timedelta(minutes=1)
        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_mins(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(minutes=12),
        )
        self.comment.date_added = self.comment.date_added-timezone.timedelta(minutes=12)
        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_hour(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(hours=1),
        )
        self.comment.date_added = self.comment.date_added-timezone.timedelta(hours=1)
        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_hours(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(hours=2),
        )
        self.comment.date_added = self.comment.date_added-timezone.timedelta(hours=2)
        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_day(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(days=1),
        )
        self.comment.date_added = self.comment.date_added-timezone.timedelta(days=1)
        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_days(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(days=2),
        )
        self.comment.date_added = self.comment.date_added-timezone.timedelta(days=2)
        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_month(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(days=30),
        )
        self.comment.date_added = self.comment.date_added-timezone.timedelta(days=30)
        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_months(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(days=70),
        )
        self.comment.date_added = self.comment.date_added-timezone.timedelta(days=70)
        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_year(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(days=365),
        )
        self.comment.date_added = self.comment.date_added-timezone.timedelta(days=365)
        article.whenpublished()
        self.comment.whenpublished()

    def test_for_when_publish_for_years(self):
        article = Article.objects.create(
            date_posted=timezone.now()-timezone.timedelta(days=800),
        )
        self.comment.date_added = self.comment.date_added-timezone.timedelta(days=800)
        article.whenpublished()
        self.comment.whenpublished()

