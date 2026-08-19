import re

WORDS_PER_MINUTE = 225
READTIME_MARKER = "{{READTIME}}"


def on_page_markdown(markdown, page, config, files, **kwargs):
    if READTIME_MARKER not in markdown:
        return markdown

    text = re.sub(r"```.*?```", "", markdown, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)

    words = re.findall(r"[\w'-]+", text)
    minutes = max(1, round(len(words) / WORDS_PER_MINUTE))

    return markdown.replace(READTIME_MARKER, str(minutes))