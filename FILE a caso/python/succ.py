import re
import random
import string

# Definisci l'espressione regolare
pattern = r'^flag\{[\D]{2}[0][a-z][^0-9][L][\w]{4}[^a-pr-z]{3}[^\d]{2}[\d][b]\}$'

# Funzione per generare una stringa casuale che potrebbe corrispondere al pattern
def generate_matching_string():
    # Genera una stringa casuale con le caratteristiche richieste
    random_string = f"flag{''.join(random.choice(string.ascii_lowercase) for _ in range(2))}0" \
                    f"{random.choice(string.ascii_lowercase)}L" \
                    f"{''.join(random.choice(string.ascii_letters + string.digits + '_') for _ in range(4))}" \
                    f"{''.join(random.choice(string.ascii_letters.replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '').replace('i', '').replace('j', '').replace('k', '').replace('l', '').replace('m', '').replace('n', '').replace('o', '').replace('p', '').replace('q', '').replace('r', '').replace('s', '').replace('t', '').replace('u', '').replace('v', '').replace('w', '').replace('x', '').replace('y', '').replace('z', '')) for _ in range(3)}" \
                    f"{''.join(random.choice(string.ascii_letters.replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('e', '').replace('f', '').replace('g', '').replace('h', '').replace('i', '').replace('j', '').replace('k', '').replace('l', '').replace('m', '').replace('n', '').replace('o', '').replace('p', '').replace('q', '').replace('r', '').replace('s', '').replace('t', '').replace('u', '').replace('v', '').replace('w', '').replace('x', '').replace('y', '').replace('z', '')) for _ in range(2)}" \
                    f"{random.choice(string.digits)}b"

    return random_string

# Cerca una stringa che corrisponda al pattern
matching_string_found = False
while not matching_string_found:
    candidate_string = generate_matching_string()
    match = re.match(pattern, candidate_string)
    if match:
        matching_string_found = True
        print(f"Stringa trovata: {candidate_string}")
