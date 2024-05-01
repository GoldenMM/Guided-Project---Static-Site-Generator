import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def setUp(self):
        self.child1 = LeafNode('p', 'Hello, world!', {'class': 'test'})
        self.child2 = LeafNode('p', 'Goodbye, world!', {'class': 'test'})
        self.parent_node = ParentNode('div', [self.child1, self.child2], {'class': 'parent'})

    def test_init(self):
        self.assertEqual(self.parent_node.tag, 'div')
        self.assertEqual(self.parent_node.children, [self.child1, self.child2])
        self.assertEqual(self.parent_node.props, {'class': 'parent'})

    def test_to_html(self):
        expected_output = '<div class="parent"><p class="test">Hello, world!</p><p class="test">Goodbye, world!</p></div>'
        self.assertEqual(self.parent_node.to_html(), expected_output)

    def test_to_html_no_tag(self):
        self.parent_node.tag = None
        with self.assertRaises(ValueError):
            self.parent_node.to_html()

    def test_to_html_no_children(self):
        self.parent_node.children = None
        with self.assertRaises(ValueError):
            self.parent_node.to_html()

    def test_to_html_nested(self):
        grandchild = LeafNode('p', 'Nested child', {'class': 'nested'})
        child = ParentNode('div', [grandchild], {'class': 'child'})
        parent = ParentNode('div', [child], {'class': 'parent'})
        expected_output = '<div class="parent"><div class="child"><p class="nested">Nested child</p></div></div>'
        self.assertEqual(parent.to_html(), expected_output)

if __name__ == '__main__':
    unittest.main()