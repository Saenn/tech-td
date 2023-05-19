from helper.sanitizer import Sanitizer
from helper.stat_generator import Generator, STATS


def sanitize_data(data: str):
    sanitizer = Sanitizer()
    data = sanitizer.transform_data(data)
    print(f'Sanitized data:\n  "{data}"\n')
    return data

def generate_and_show_stat(data: str):
    stats = Generator().generate_stats(data)
    alphabet_count = stats[STATS.ALPHABET_COUNT]

    print("Alphabet Count:")
    for alp in alphabet_count:
        capture = f"{alp}: {alphabet_count[alp]}"
        print(f"  {capture}")
