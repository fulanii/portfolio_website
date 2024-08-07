from django.test import TestCase
from django.urls import reverse
from django.http import FileResponse
import os


class ViewTests(TestCase):
    def test_homepage_view(self):
        response = self.client.get(reverse('home'))  # Assuming 'home' is the name of the URL pattern for the homepage
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/home.html')

    def test_resume_view(self):
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, FileResponse)

        resume_path = os.path.join('portfolio', 'static', 'portfolio', 'files', 'resume.pdf')
        with open(resume_path, 'rb') as file:
            expected_content = file.read()

        response_content = b''.join(response.streaming_content)
        self.assertEqual(response_content, expected_content)

    def test_links_view(self):
        response = self.client.get(reverse('links'))  # Assuming 'links' is the name of the URL pattern for the links page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/links.html')