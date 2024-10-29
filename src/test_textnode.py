import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_url(self):
        node = ("This is a text node", "bold", "https://www.random.dev")
        node2 = ("This is a text node", "bold", "https://random.dev")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()