from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username="User1", password="123abc")
        testuser1.save()
        test_post = Post.objects.create(
            author=testuser1, title="test title", body="test body"
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "User1")
        self.assertEqual(title, "test title")
        self.assertEqual(body, "test body")
