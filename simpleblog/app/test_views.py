# app/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BlogPost

class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        # Create a sample blog post for testing
        self.post = BlogPost.objects.create(title="Test Post", content="Test Content")

    def test_create_post(self):
        url = reverse('post-list-create')  # URL for creating a blog post
        data = {
            "title": "New Test Post",
            "content": "New Test Content"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 2)  # One existing post + new post
        self.assertEqual(BlogPost.objects.get(id=response.data['id']).title, "New Test Post")

    def test_list_posts(self):
        url = reverse('post-list-create')  # URL for listing blog posts
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return the one created in setUp

    def test_retrieve_post(self):
        url = reverse('post-detail', args=[self.post.id])  # URL for retrieving the specific post
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_update_post(self):
        url = reverse('post-detail', args=[self.post.id])  # URL for updating the specific post
        data = {
            "title": "Updated Title",
            "content": "Updated Content"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.post.title, "Updated Title")

    def test_delete_post(self):
        url = reverse('post-detail', args=[self.post.id])  # URL for deleting the specific post
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlogPost.objects.count(), 0)  # Should be deleted
