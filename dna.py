import csv
import sys


def main():
    # Check command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    database_path = sys.argv[1]
    sequence_path = sys.argv[2]

    # Read database CSV into memory
    with open(database_path, "r") as db_file:
        reader = csv.DictReader(db_file)
        strs = reader.fieldnames[1:]   # STR columns (skip "name")
        people = list(reader)          # list of dict rows

    # Read DNA sequence file into memory
    with open(sequence_path, "r") as seq_file:
        sequence = seq_file.read().strip()

    # Compute STR counts in the DNA sequence
    counts = {}
    for s in strs:
        counts[s] = longest_match(sequence, s)

    # Compare against each person in database
    for person in people:
        is_match = True

        for s in strs:
            if int(person[s]) != counts[s]:
                is_match = False
                break

        if is_match:
            print(person["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    longest_run = 0
    subseq_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0

        while True:
            start = i + count * subseq_len
            end = start + subseq_len

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
