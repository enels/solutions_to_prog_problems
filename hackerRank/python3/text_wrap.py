def wrap(string, max_width):
    wrapped_string = ""
    s = ""
    end = max_width
    for c in string:
        s += c
        if (len(s) == max_width):
            wrapped_string += s + "\n"
            # reinitialize s
            s = ""

    if len(s) != 0:
        wrapped_string += s

    return wrapped_string

print(wrap("Waitformetocomeanddoitforyourtr", 5))