import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    list_of_lines = markdown.split("\n\n")
    blocks = []
    for line in list_of_lines:
        if line != "":
            blocks.append(line.strip())
    return blocks

def block_to_block_type(block):
    if not isinstance(block, str):
        raise Exception("The given input is not a string")
    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    if re.match(r'^#{1,6} ', block):
        return block_type_heading
    # Code blocks must start with 3 backticks and end with 3 backticks.
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    
    # split the block into all lines to check for quote or list types
    block_lines = block.split("\n")
    # Every line in a quote block must start with a > character.
    if block.startswith(">"):
        for line in block_lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    
    # Every line in an unordered list block must start with a * or - character (but it must be consistent).
    if block.startswith("*"):
        for line in block_lines:
            if not line.startswith("*"):
                return block_type_paragraph
        return block_type_unordered_list
    
    if block.startsiwth("-"):
        for line in block_lines:
            if not line.startsiwth("-"):
                return block_type_paragraph
        return block_type_unordered_list

    # Every line in an ordered list block must start with a number followed by a . character. The number must start at 1 and increment by 1 for each line.
    is_ordered_list = False
    for i in range(len(block_lines)):
        if block_lines[i].startswith(f"{i+1}."):
            is_ordered_list = True
        else:
            is_ordered_list = False
        if not is_ordered_list:
            break
    if is_ordered_list:
        return block_type_olist
    
    # If none of the above conditions are met, the block is a normal paragraph.
    else:
        return block_type_paragraph
    

    

