from itertools import cycle
import matplotlib.pyplot as plt

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ref_freq = {'о': 0.1107, 'е,ё': 0.0841, 'а': 0.0792, 'и': 0.0683, 'н': 0.0672,
            'т': 0.0618, 'с': 0.0533, 'л': 0.05, 'р': 0.0445, 'в': 0.0433,
            'к': 0.0336, 'м': 0.0326, 'д': 0.0305, 'п': 0.0281, 'у': 0.028,
            'я': 0.0213, 'ы': 0.0196, 'ь': 0.0192, 'з': 0.0175, 'г': 0.0174,
            'б': 0.0171, 'ч': 0.0147, 'й': 0.0112, 'ж': 0.0105, 'х': 0.0089,
            'ш': 0.0081, 'ю': 0.0061, 'э': 0.0038, 'щ': 0.0037, 'ц': 0.0036,
            'ф': 0.0019, 'ъ': 0.0002}


def encode(text, key):
    replacements = [(' ', ''), (',', ''), ('!', ''),
                    ('.', ''), ('?', ''), (':', ''),
                    ('-', ''), ('–', ''), (';', ''),
                    ('\"', ''), ('\'', ''), ('\n', ''),
                    ('\t', ''), ('ё', 'е'), ('(', ''),
                    (')', ''), ('—', ''), ('[', ''),
                    (']', ''), ('«', ''), ('»', ''),
                    ('…', '')]
    text = text.lower()
    key = key.lower()
    for char, replacement in replacements:
        if char in text:
            text = text.replace(char, replacement)
        if char in key:
            key = key.replace(char, replacement)
    f = lambda arg: alphabet[(alphabet.index(arg[0]) + alphabet.index(arg[1]) % 32) % 32]
    return ''.join(map(f, zip(text, cycle(key))))


def freq_analysis(encoded_text):
    encoded_text_lists = [[] for _ in range(6)]
    for i, char in enumerate(encoded_text):
        encoded_text_lists[i % 6].append(char)
    frequencies = []
    for encoded_list in encoded_text_lists:
        frequency = {letter: encoded_list.count(letter) for letter in set(encoded_list)}
        fact_freq = {letter: round(count / len(encoded_list), 4) for letter, count in frequency.items()}
        frequencies.append(sorted(fact_freq.items(), key=lambda x: x[1], reverse=True))

    return frequencies


def show_plots(encoded_text, ref_freq):
    fact_freq = freq_analysis(encoded_text)
    fig, axs = plt.subplots(7, figsize=(10, 2 * 6))
    i = 0
    for arr in fact_freq:
        for letters, freq in arr:
            axs[i].bar(letters, freq)
            axs[i].set_xlabel(f'Символы {i + 1}')
            axs[i].set_ylabel(f'Отн.част. {i + 1}')
            axs[i].set_title(f'Относительная частота появления символов в тексте {i + 1}')
        i += 1

    ref_freq = sorted(ref_freq.items(), key=lambda x: x[1], reverse=True)
    for letters, freq in ref_freq:
        axs[6].bar(letters, freq)
        axs[6].set_xlabel(f'Символы')
        axs[6].set_ylabel(f'Отн.част.')
        axs[6].set_title(f'Эталонные отн. частоты')
    plt.tight_layout()
    return plt.show()
