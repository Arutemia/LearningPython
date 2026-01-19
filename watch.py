import re

def main():
    print(parse(input("HTML: ")))

def parse(s):

    match = re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()
