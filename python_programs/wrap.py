
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        line, text = text[:end], text[end:]
        lines.append(line)

    lines.append(text)
    return lines
