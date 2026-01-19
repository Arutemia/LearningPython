def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    return emoticon

def main():
    print(convert(input()))

main()
