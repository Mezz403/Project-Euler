def count_num(text, num):
    count = 0
    for c in text:
        if c == num:
            count += 1
    return count

def text_analyzer(file):
    with open(file) as text:
        text = list(map(int, text.read().split(',')))
        numFrequencies = {}

        for num in text:
            numFrequencies[num] = count_num(text, num)

    return numFrequencies
