import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        test = HTMLNode("p", "loren ipsum", props={"href": "https://www.google.com", "target": "_blank",})
        test_expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(test.props_to_html(), test_expected)

    def test_prop_def_value(self):
        test = HTMLNode("p", "loren ipsum",)
        self.assertIs(test.props, None)

    def test_node_repr(self):
        test = HTMLNode("p", "loren ipsum", props={"href": "https://www.google.com", "target": "",})
        test_expected = f"HTMLNode({test.tag}, {test.value}, {test.children}, {test.props})"
        self.assertEqual(test.__repr__(), test_expected)

if __name__ == "__main__":
    unittest.main()