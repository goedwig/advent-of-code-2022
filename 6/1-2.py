with open("6/input.txt") as f:
    datastream = f.read().rstrip()


def find_marker(distinct_chars):
    marker_chars = []

    for count, ch in enumerate(datastream, start=1):
        marker_chars.append(ch)
        marker_chars = marker_chars[-distinct_chars:]

        if len(set(marker_chars)) == distinct_chars:
            return count


print(find_marker(4))
print(find_marker(14))
