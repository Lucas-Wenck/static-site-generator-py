import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_parentnode(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        node_expect = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), node_expect)

    def test_to_html_nested_parentnode(self):
        node = ParentNode("div",[ParentNode("span",[LeafNode(None, "Child text inside span"),]),LeafNode("p", "Sibling paragraph text")],)
        node_expect = "<div><span>Child text inside span</span><p>Sibling paragraph text</p></div>"
        self.assertEqual(node.to_html(), node_expect)

if __name__ == "__main__":
    unittest.main()