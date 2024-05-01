import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node = HTMLNode('p', 'Hello, world!', [], {'class': 'test'})

    def test_init(self):
        self.assertEqual(self.node.tag, 'p')
        self.assertEqual(self.node.value, 'Hello, world!')
        self.assertEqual(self.node.children, [])
        self.assertEqual(self.node.props, {'class': 'test'})

    def test_props_to_html(self):
        self.assertEqual(self.node.props_to_html(), ' class="test"')
        
    def test_props_to_html_multiple(self):
        self.node.props = {'class': 'test', 'id': 'node1', 'data-info': 'sample'}
        expected_output = ' class="test" id="node1" data-info="sample"'
        self.assertEqual(self.node.props_to_html(), expected_output)

    def test_repr(self):
        self.assertEqual(repr(self.node), 'HTMLNode(p, Hello, world!, [], {\'class\': \'test\'})')

    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            self.node.to_html()

class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.leaf_node = LeafNode('p', 'Hello, world!', {'class': 'test'})

    def test_init(self):
        self.assertEqual(self.leaf_node.tag, 'p')
        self.assertEqual(self.leaf_node.value, 'Hello, world!')
        self.assertEqual(self.leaf_node.props, {'class': 'test'})

    def test_to_html(self):
        expected_output = '<p class="test">Hello, world!</p>'
        self.assertEqual(self.leaf_node.to_html(), expected_output)

    def test_to_html_no_tag(self):
        self.leaf_node.tag = None
        expected_output = 'Hello, world!'
        self.assertEqual(self.leaf_node.to_html(), expected_output)

    def test_to_html_no_value(self):
        self.leaf_node.value = None
        with self.assertRaises(ValueError):
            self.leaf_node.to_html()

    def test_to_html_multiple_props(self):
        self.leaf_node.props = {'class': 'test', 'id': 'node1', 'data-info': 'sample'}
        expected_output = '<p class="test" id="node1" data-info="sample">Hello, world!</p>'
        self.assertEqual(self.leaf_node.to_html(), expected_output)

if __name__ == '__main__':
    unittest.main()