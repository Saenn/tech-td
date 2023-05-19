
class STATS:
    ALPHABET_COUNT = 'alphabet_count'
    # add more here

class Generator:
    stats = {}

    def __init__(self):
        pass

    def generate_stats(self, data: str):
        alphabet_count = self._count_alphabet(data)
        self.stats[STATS.ALPHABET_COUNT] = alphabet_count

        # add more here
        
        return self.stats

    def _count_alphabet(self, data: str) -> dict:
        mapper = {}
        for _chr in data:
            
            # check if a character is an alphabet
            if not _chr.isalpha(): continue

            if _chr in mapper:
                mapper[_chr] += 1
            else: mapper[_chr] = 1

        mapper = dict(sorted(mapper.items()))
        return mapper
