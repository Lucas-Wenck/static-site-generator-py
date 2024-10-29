from textnode import *

def main():
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    textnode2 = TextNode("This is a text node", "bold", "https://www.boot.dev")

    print(textnode == textnode2)

main()