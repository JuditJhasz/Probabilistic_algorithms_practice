import random
import json
import string

# Load configuration
CONFIG_FILE = "config.json"

def load_config(filename):
    with open(filename, "r") as f:
        return json.load(f)

def generate_random_sequence(length):
    return "".join(random.choices("ACGT", k=length))

def introduce_point_mutations(sequence, mutation_rate):
    sequence = list(sequence)
    for i in range(len(sequence)):
        if random.random() < mutation_rate:
            sequence[i] = random.choice("ACGT".replace(sequence[i], ""))
    return "".join(sequence)

def introduce_inversions(sequence, inversion_rate, max_inversion_size):
    sequence = list(sequence)
    for i in range(len(sequence) - max_inversion_size):
        if random.random() < inversion_rate:
            size = random.randint(1, max_inversion_size)
            sequence[i:i+size] = reversed(sequence[i:i+size])
    return "".join(sequence)

def introduce_insertions(sequence, insertion_rate, max_insertion_size):
    new_sequence = []
    for base in sequence:
        new_sequence.append(base)
        if random.random() < insertion_rate:
            insertion = generate_random_sequence(random.randint(1, max_insertion_size))
            new_sequence.extend(insertion)
    return "".join(new_sequence)

def introduce_deletions(sequence, deletion_rate, max_deletion_size):
    new_sequence = []
    i = 0
    while i < len(sequence):
        if random.random() < deletion_rate:
            i += random.randint(1, max_deletion_size)  # Skip bases (delete them)
        else:
            new_sequence.append(sequence[i])
            i += 1
    return "".join(new_sequence)

def generate_sequences(config):
    sequences = {}
    num_families = config["num_families"]
    num_sequences_per_family = config["num_sequences_per_family"]
    sequence_length = config["sequence_length"]
    
    family_letters = random.sample(string.ascii_uppercase, num_families)
    
    for family_index, family_letter in enumerate(family_letters):
        base_sequence = generate_random_sequence(sequence_length)
        sequences[f"{family_letter}_original"] = base_sequence
        for i in range(num_sequences_per_family):
            mutated = base_sequence
            mutated = introduce_point_mutations(mutated, config["mutation_rate"])
            mutated = introduce_inversions(mutated, config["inversion_rate"], config["max_inversion_size"])
            mutated = introduce_insertions(mutated, config["insertion_rate"], config["max_insertion_size"])
            mutated = introduce_deletions(mutated, config["deletion_rate"], config["max_deletion_size"])
            sequences[f"{family_letter}_seq_{i}_mutated"] = mutated
    
    return sequences

def main():
    config = load_config(CONFIG_FILE)
    sequences = generate_sequences(config)
    with open("sequences/sequences_len_1000.fasta", "w") as f:
        for name, seq in sequences.items():
            f.write(f">{name}\n{seq}\n")
    print("Sequences generated and saved to sequences.fasta")

if __name__ == "__main__":
    main()
