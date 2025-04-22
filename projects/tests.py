from rest_framework import serializers
from django.test import TestCase
from users.models import CustomUser
from projects.models import Project
from projects.serializers import ProjectUpdateMemberSerializer


class ProjectUpdateMemberSerializerTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email="testuser", password="testpass"
        )
        self.project = Project.objects.create(name="Test Project", max_members=5)

    def test_valid_user_ids(self):
        valid_user_ids = [self.user.id]
        serializer = ProjectUpdateMemberSerializer(data={"user_ids": valid_user_ids})

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["user_ids"], valid_user_ids)

    def test_invalid_user_ids(self):
        serializer = ProjectUpdateMemberSerializer(data={"user_ids": ["a", "b", "c"]})

        self.assertFalse(serializer.is_valid())
        self.assertIn("user_ids", serializer.errors)
        self.assertFalse(
            all(
                isinstance(err, serializers.ValidationError)
                for err in serializer.errors["user_ids"]
            )
        )

    def test_non_existent_user_ids(self):
        non_existent_user_ids = [999, 1000]
        serializer = ProjectUpdateMemberSerializer(
            data={"user_ids": non_existent_user_ids}
        )

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["user_ids"], non_existent_user_ids)

    def test_mixed_user_ids(self):
        mixed_user_ids = [self.user.id, "invalid_id", 999]
        serializer = ProjectUpdateMemberSerializer(data={"user_ids": mixed_user_ids})

        self.assertFalse(serializer.is_valid())
        self.assertIn("user_ids", serializer.errors)
        self.assertFalse(
            all(
                isinstance(err, serializers.ValidationError)
                for err in serializer.errors["user_ids"]
            )
        )
