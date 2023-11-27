PROBABILITY = {}


def arithmetic_decoding(encoded_value, text_length):
    decoded_text = ""
    low, high = 0.0, 1.0
    for _ in range(text_length):
        for char, prob in PROBABILITY.items():
            rang = high - low
            if low + rang * prob <= encoded_value < low + rang * (prob + PROBABILITY[char]):
                decoded_text += char
                high = low + rang * (prob + PROBABILITY[char])
                low = low + rang * prob
                break
    return decoded_text


def arithmetic_coding(text):
    for char in text:
        if char in PROBABILITY:
            PROBABILITY[char] += 1
        else:
            PROBABILITY[char] = 1

    for key in PROBABILITY:
        PROBABILITY[key] /= len(text)

    low, high = 0.0, 1.0

    for char in text:
        rang = high - low
        high = low + rang * PROBABILITY[char]
        low = high - rang * PROBABILITY[char]

    return (low + high) / 2


if __name__ == '__main__':
    with open('text_file.txt', 'r') as file:
        lines: list[str] = file.readlines()

        encoded_lines: list[str] = []
        for line in lines:
            encoded_lines.append(arithmetic_coding(line))

        # Выводим закодированные строки

        with open('interval_coding.txt', 'w') as result:
            for line in encoded_lines:
                result.write(str(line) + '\n')

    with open('interval_coding.txt', 'r') as file:
        encoded_lines = file.readlines()

        encoded_information = []
        for line in encoded_lines:
            encoded_information.append(arithmetic_decoding(float(line), len(line)))

        print(encoded_information)
