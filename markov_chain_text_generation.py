import random
from collections import defaultdict


def preprocess_text(text):
    return text.lower().split()


def build_markov_chain(words, n=2):
    markov_chain = defaultdict(lambda: defaultdict(int))
    for i in range(len(words) - n):
        current_state = tuple(words[i:i+n])
        next_state = words[i+n]
        markov_chain[current_state][next_state] += 1
    return markov_chain

def normalize_chain(chain):
    normalized_chain = {}
    for current_state, transitions in chain.items():
        total = sum(transitions.values())
        normalized_chain[current_state] = {state: count / total for state, count in transitions.items()}
    return normalized_chain


def generate_text(chain, start_state, length=50):
    current_state = start_state
    output = list(current_state)
    for _ in range(length):
        if current_state not in chain or not chain[current_state]:
            print(f"Warning: {current_state} not in chain or has no transitions. Using random state.")
            current_state = random.choice(list(chain.keys()))
            if current_state not in chain or not chain[current_state]:
                break
        next_state = random.choices(list(chain[current_state].keys()), list(chain[current_state].values()))[0]
        output.append(next_state)
        current_state = tuple(output[-len(start_state):])
    return ' '.join(output)


text = """
In a land where imagination flows like rivers and creativity soars like eagles, there was a curious inventor. He built fantastical machines that could bend the laws of reality and transform ordinary moments into extraordinary experiences. One day, his greatest creation malfunctioned, unleashing a whirlwind of whimsical wonders that altered the very fabric of his world. As he navigated through this new realm of wonder, he discovered that the boundary between dreams and reality was not as clear as he once thought. Each adventure led him deeper into the mysteries of the cosmos and the secrets of the human spirit. The journey was filled with strange creatures, enchanted forests, and endless possibilities, revealing the true power of imagination.
"""


words = preprocess_text(text)
chain = build_markov_chain(words, n=2)  # Use n=2
normalized_chain = normalize_chain(chain)


start_state = ('a', 'land')


generated_text = generate_text(normalized_chain, start_state, length=50)
print("Generated Text:\n", generated_text)
