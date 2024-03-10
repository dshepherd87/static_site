import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_null_url(self):
        node = TextNode("This node has a null url", "bold")
        node2 = TextNode("This node has a null url", "bold", None)
        self.assertEqual(node, node2)
    
    def test_dif_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_dif_url(self):
        node = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "bold", "yahoo.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
