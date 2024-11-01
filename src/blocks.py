def markdown_to_blocks(markdown):
    clean_block = []
    block = markdown.split("\n\n")
    for i in range(len(block)):
        if block[i].strip() != "":
            clean_block.append(block[i].strip())
    return clean_block
    
