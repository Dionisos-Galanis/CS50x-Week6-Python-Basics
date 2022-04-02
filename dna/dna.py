import csv
import sys


def main():

    # Check for command-line usage
    if not len(sys.argv) == 3:
        print("Usage: python dna <database.csv> sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    with open(sys.argv[1], 'r') as db:
        if not db:
            print(f"Can't open a {sys.argv[1]} file")
            sys.exit(1)
        reader = csv.reader(db)
        lineNo = 0
        strsDB = {}
        for line in reader:
            lineNo += 1
            if lineNo == 1:
                STRs = line[1:]
            else:
                nums = []
                for k in range(1, len(line)):
                    nums.append(int(line[k]))
                strsDB[line[0]] = nums

    # Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as seq:
        if not seq:
            print(f"Can't open a {sys.argv[2]} file")
            sys.exit(1)
        sequence = seq.read()

    # Find longest match of each STR in DNA sequence
    longestMatches = []
    for subsequence in STRs:
        longestMatches.append(longest_match(sequence, subsequence))

    # TODO: Check database for matching profiles
    for person in strsDB:
        if longestMatches == strsDB[person]:
            print(person)
            sys.exit(0)

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
