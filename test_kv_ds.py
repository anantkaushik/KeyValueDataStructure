from unittest import TestCase
from kv_ds import KeyValueDataStructure


class TestKeyValueDataStructure(TestCase):

    def setUp(self):
        self.hashmap = KeyValueDataStructure()

    def test_set_value(self):
        self.hashmap.set(1, "test_val")
        self.assertEqual(self.hashmap.get(1), "test_val")

    def test_set_negative_value(self):
        self.hashmap.set(-56, "test_val_negative")
        self.assertEqual(self.hashmap.get(-56), "test_val_negative")

    def test_set_duplicate_value(self):
        self.hashmap.set(1, "test_val")

        self.assertEqual(self.hashmap.get(1), "test_val")

        self.hashmap.set(1, "test_val_new")
        self.assertEqual(self.hashmap.get(1), "test_val_new")

    def test_get_non_existing_value(self):
        self.assertEqual(self.hashmap.get(200), None)

    def test_string_key(self):
        self.hashmap.set("hey", "test_val_negative")
        self.assertEqual(self.hashmap.get("hey"), None)

    def test_collision_set(self):
        self.hashmap.set(0, "test_val")
        self.assertEqual(self.hashmap.get(0), "test_val")
        self.hashmap.set(self.hashmap.size, "new_test_val")
        self.assertEqual(self.hashmap.get(self.hashmap.size), "new_test_val")
        # it'll verify collision
        self.assertEqual(len(self.hashmap.used_keys), 1)

    def test_collision_duplicate_set(self):
        self.hashmap.set(0, "test_val")
        self.assertEqual(self.hashmap.get(0), "test_val")
        self.hashmap.set(self.hashmap.size, "new_test_val")
        self.assertEqual(self.hashmap.get(self.hashmap.size), "new_test_val")
        self.hashmap.set(self.hashmap.size, "updated_test_val")
        self.assertEqual(self.hashmap.get(self.hashmap.size), "updated_test_val")
        self.hashmap.set(0, "updated_test")
        self.assertEqual(self.hashmap.get(0), "updated_test")
        # it'll verify collision
        self.assertEqual(len(self.hashmap.used_keys), 1)

    def test_display(self):
        self.hashmap.set(0, "test_val")
        self.assertEqual(self.hashmap.display(), [(0, "test_val")])
        self.hashmap.set(1, "new_test_val")
        self.assertEqual(self.hashmap.display(), [(0, "test_val"), (1, "new_test_val")])

    def test_display_with_collison(self):
        self.hashmap.set(0, "test_val")
        self.assertEqual(self.hashmap.display(), [(0, "test_val")])
        self.hashmap.set(self.hashmap.size, "new_test_val")
        self.assertEqual(self.hashmap.display(), [(0, "test_val"), (self.hashmap.size, "new_test_val")])

