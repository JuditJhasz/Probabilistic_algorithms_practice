def parse_documents(file_path):
    documents = {}
    with open(file_path, "r") as file:
        lines = file.readlines()
        
        for i in range(0, len(lines) - 1, 2):  # Process in pairs (title, text)
            title = lines[i].strip()
            text = lines[i + 1].strip()
            documents[title] = text  # Store in dictionary

    return documents

def parse_fasta(file_path):
    fasta_dict = {}
    with open(file_path, "r") as file:
        sequence_id = None
        sequence = []
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):  # Header line
                if sequence_id:  # Save previous sequence
                    fasta_dict[sequence_id] = "".join(sequence)
                sequence_id = line[1:].split()[0]  # Extract first word as ID
                sequence = []  # Reset sequence
            else:
                sequence.append(line)  # Add sequence lines

        if sequence_id:  # Save last sequence
            fasta_dict[sequence_id] = "".join(sequence)

    return fasta_dict

