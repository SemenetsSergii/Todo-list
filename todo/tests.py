from django.test import TestCase

from .models import Tag, Task


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")

    def test_tag_creation(self):
        tag = Tag.objects.get(name="Urgent")
        self.assertEqual(tag.name, "Urgent")

    def test_str_method(self):
        self.assertEqual(str(self.tag), "Urgent")


class TaskModelTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Urgent")
        self.tag2 = Tag.objects.create(name="Home")
        self.task = Task.objects.create(
            content="Finish homework", deadline="2024-07-25T10:00:00Z"
        )

    def test_task_creation(self):
        task = Task.objects.get(content="Finish homework")
        self.assertEqual(task.content, "Finish homework")

    def test_task_tags(self):
        self.task.tags.add(self.tag1, self.tag2)
        task = Task.objects.get(content="Finish homework")
        self.assertIn(self.tag1, task.tags.all())
        self.assertIn(self.tag2, task.tags.all())

    def test_str_method(self):
        self.assertEqual(str(self.task), "Finish homework")
