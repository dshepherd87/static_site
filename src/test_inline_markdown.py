import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertListEqual(extract_markdown_links(text), [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

    def test_extract_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertListEqual(extract_markdown_images(text), [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")])

    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",text_type_text,)
        node2 = TextNode("This is another node with an ![image](https://i.imgur.com/zjjcJKZ.png), and another ![second image](https://i.imgur.com/3elNhQu.png), and even another ![third image](https://i.imgur.com/whatever)", text_type_text)
        expected_result = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://i.imgur.com/3elNhQu.png"),
            TextNode("This is another node with an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(", and another ", text_type_text),
            TextNode("second image", text_type_image, "https://i.imgur.com/3elNhQu.png"),
            TextNode(", and even another ", text_type_text),
            TextNode("third image", text_type_image, "https://i.imgur.com/whatever")
        ]
        self.assertListEqual(split_nodes_image([node, node2]), expected_result)

    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](https://www.google.com) and another [second link](https://www.yahoo.com)", text_type_text,)
        expected_result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.google.com"),
            TextNode(" and another ", text_type_text),
            TextNode("second link", text_type_link, "https://www.yahoo.com"),
        ]
        self.assertListEqual(split_nodes_link([node]), expected_result)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected_result = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnodes(text), expected_result)

if __name__ == "__main__":
    unittest.main()