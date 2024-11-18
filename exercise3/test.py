import unittest
import handler

class TestManejadorTipos(unittest.TestCase):

    def test_add_atomic_type(self):
        self.assertTrue(handler.add_atomic_type("a", 1, 4))

    def test_add_existing_atomic_type_fails(self):
        handler.add_atomic_type("b", 1, 2)
        self.assertFalse(handler.add_atomic_type("b", 4, 7))

    def test_add_union_type(self):
        handler.add_atomic_type("c", 4, 4)
        handler.add_atomic_type("d", 1, 4)
        self.assertTrue(handler.add_union_type("union1", ["c", "d"]))

    def test_add_existing_union_type(self):
        handler.add_atomic_type("e", 4, 4)
        handler.add_atomic_type("f", 2, 4)
        handler.add_union_type("union2", ["e", "f"])
        self.assertFalse(handler.add_union_type("union2", ["e", "f"]))

    def test_add_struct_type_success(self):
        handler.add_atomic_type("g", 1, 1)
        handler.add_atomic_type("h", 2, 2)
        self.assertTrue(handler.add_struct_type("struct1", ["g", "h"]))

    def test_add_existing_struct_type(self):
        handler.add_atomic_type("i", 2, 4)
        handler.add_atomic_type("j", 1, 2)
        handler.add_struct_type("struct2", ["i", "j"])
        self.assertFalse(handler.add_struct_type("struct2", ["i", "j"]))

    def test_describe_atomic_type(self):
        handler.add_atomic_type("k", 3, 8)
        self.assertTrue(handler.describe_type("k"))

    def test_describe_structure(self):
        handler.add_atomic_type("l", 2, 2)
        handler.add_atomic_type("s", 4, 2)
        handler.add_struct_type("struct3", ["l", "s"])
        self.assertTrue(handler.describe_type("struct3"))

    def test_union_type_description(self):
        handler.add_atomic_type("d", 3, 8)
        handler.add_atomic_type("e", 2, 1)
        handler.add_union_type("union3", ["e", "d"])
        self.assertTrue(handler.describe_type("union3"))

if __name__ == '__main__':
    unittest.main()
