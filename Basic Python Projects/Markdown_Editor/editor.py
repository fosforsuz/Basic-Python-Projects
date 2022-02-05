def main():
    while True:
        string = input("- Choose a formatter: ")

        if string in command_list:
            markdown_control(string)
            print(*markdown, sep="")
            continue
        elif string == "!help":
            print("Available formatters: ", command_list[0], command_list[1], command_list[2], command_list[3],
                  command_list[4], command_list[5], command_list[6], command_list[7], command_list[8])
            print("Special commands: !help !done")
            continue
        elif string == "!done":
            save_to_file()
            break
        print("Unknown formatting type or command. Please try again")


def markdown_control(content):
    if content == "plain":
        text = input("- Text:")
        markdown.append(text)
    elif content == "bold":
        text = f"**{input('- Text: ')}**"
        markdown.append(text)
    elif content == "italic":
        text = f"*{input('- Text: ')}*"
        markdown.append(text)
    elif content == "inline-code":
        text = f"`{input('- Text: ')}`"
        markdown.append(text)
    elif content == "link":
        label = input("- Label:")
        url = input("- URL:")
        markdown.append("[" + label + "]" + "(" + url + ")")
    elif content == "header":
        level = int(input("- Level:"))
        if 1 <= level <= 6:
            text = input("- Text:")
            markdown.append(level * "#" + " " + text + "\n")
        else:
            print("The level should be within the range of 1 to 6")
    elif content == "line-break":
        markdown.append("\n")
    elif content == "ordered-list":
        create_list(content)
    elif content == "unordered-list":
        create_list(content)


def create_list(content):
    rows = 0
    while rows < 1:
        rows = int(input("- Number of rows: "))
        if rows < 1:
            print("The number of rows should be greater than zero")

    for i in range(rows):
        text = input(f"Row #{i + 1}: ")
        if content == "ordered-list":
            markdown.append(f"{i + 1}. " + text + "\n")
        else:
            markdown.append(f"* " + text + "\n")


def print_list():
    global markdown
    for word in markdown:
        print(word)


def save_to_file():
    with open("output.md", "w+") as file:
        file.writelines(markdown)


command_list = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list",
                "line-break"]
markdown = []
main()
