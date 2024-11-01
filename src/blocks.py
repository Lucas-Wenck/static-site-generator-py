def markdown_to_blocks(markdown):
    clean_block = []
    block = markdown.split("\n\n")
    for i in range(len(block)):
        if block[i].strip() != "":
            clean_block.append(block[i].strip())
    return clean_block
    
def block_to_block(markdown_block):
    lines = markdown_block.split("\n")
    if markdown_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    if markdown_block[0] == ">":
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    if markdown_block[0:2] == "* ":
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
    if markdown_block[0:2] == "- ":
        for line in lines:
            if not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    if markdown_block[0:3] == "1. ":
        count = 1
        for line in lines:
            if not line.startswith(f"{count}. "):
                return "paragraph"
            count += 1
        return "ordered_list"
    return "paragraph"
