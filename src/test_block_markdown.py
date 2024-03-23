import unittest 

from block_markdown import (block_to_block_type,
                            block_type_paragraph,
                            block_type_heading,
                            block_type_code,
                            block_type_quote,
                            block_type_unordered_list,
                            block_type_olist)

class TestBockMarkdown(unittest.TestCase):
    def test_block_to_block_type(self):
        block1 = "This is just a normal paragraph, nothing strange is going on here.\nIf it happens to contain more than one line, don't worry about it!"
        block2 = "## This is a H2 header, please treat it as such"
        block3 = ">This is not the end\n>It is not even the beginning of the end.\n>But it is, perhaps, the end of the beginning"
        block4 = "* Milk\n* Eggs\n* Cream\n- Soda\n* bacon"
        block5 = "1. Get up\n2. Get dressed\n3. Eat breakfast"
        block6 = "```This is a code block you dummy```"
        block7 = "This combines elements of paragraph and list\n*with this being the first item\n*and this being the second"
        self.assertListEqual([block_to_block_type(block1), 
                              block_to_block_type(block2), 
                              block_to_block_type(block3),
                              block_to_block_type(block4),
                              block_to_block_type(block5),
                              block_to_block_type(block6),
                              block_to_block_type(block7)], 
                              [block_type_paragraph, 
                               block_type_heading, 
                               block_type_quote,
                               block_type_unordered_list,
                               block_type_olist,
                               block_type_code,
                               block_type_paragraph])