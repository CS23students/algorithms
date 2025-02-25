def search(pat, txt):
    """Find all occurrences of pat in txt and print their positions."""
    n = len(txt)
    m = len(pat)
    found = False

    for i in range(n - m + 1):  # Loop through text
        if txt[i:i + m] == pat:  # Check substring match
            print(f"Pattern found at index {i}")
            found = True

    if not found:
        print("Pattern not found")

# Get input from user
txt = input("Enter the text: ")
pat = input("Enter the pattern: ")

search(pat, txt)


# OUTPUT :
# Enter the text: AABAACAADAABAAABAA
# Enter the pattern: AABA
