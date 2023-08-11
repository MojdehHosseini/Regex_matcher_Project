
# Determine whether a given pattern matches a word using regular expression rules
def match_pattern_with_word(pattern, word):

    t = word
    memoization = {}

    def dynamic_part(i, j):
        if (i, j) not in memoization:
            # Verify whether the pattern is devoid, in which case the string 's' should also be void.
            if j == len(pattern):
                memoization[(i, j)] = i == len(t)
            else:
                # Verify if the initial characters of 's' and 'pattern' are the same
                # Ensure that the string is not empty
                # Either the initial characters perfectly match, or
                # The first character of the 'pattern' is "." which matches any character in 's'

                is_first_char_match = len(t) > i and (t[i] == pattern[j] or pattern[j] == ".")

                # In the event that '*' appears as the second character in the pattern
                if j < len(pattern) - 1 and pattern[j + 1] == "*":
                    memoization[(i, j)] = dynamic_part(i, j + 2) or (is_first_char_match and dynamic_part(i + 1, j))


                # Proceed with examining the remaining characters through recursive evaluation
                else:
                    memoization[(i, j)] = is_first_char_match and dynamic_part(i + 1, j + 1)

        return memoization[(i, j)]

    print(dynamic_part(0, 0))
    return dynamic_part(0, 0)


# Filter words from a list that match a given pattern
def filter_words_matching_pattern(pattern, word_list):
    return [word for word in word_list if match_pattern_with_word(pattern, word)]

# Sort the matched words with Selection sort
def custom_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if len(arr[j]) < len(arr[min_index]) or (len(arr[j]) == len(arr[min_index]) and arr[j] < arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]



# Dynamic programming implementation to find the LCS of two words
def find_longest_common_subsequence(X, Y):

    m = len(X)
    n = len(Y)

    # Construct matrix F[m+1][n+1] in a bottom-up fashion
    F = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                F[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])

    lcs_char = ""
    i = m
    j = n

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs_char += X[i - 1]
            i -= 1
            j -= 1
        elif F[i - 1][j] > F[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_char = lcs_char[::-1]
    print("Longest Common Subsequence of " + X + " and " + Y + " is " + lcs_char)
    return lcs_char

# Read input from "input.txt"
with open("input4.txt", "r") as file:
    lines = file.readlines()

# Extract n, the number of words in the dictionary
n = int(lines[0])

# Extract the dictionary words (next n lines)
word_list = [line.strip() for line in lines[1: n + 1]]


# Extract the regex pattern R (last line of input)
regex_pattern = lines[n + 1].strip()

# Filter words that match the regex pattern
matched_words = filter_words_matching_pattern(regex_pattern, word_list)



# Sort matched_words using custom_sort function
custom_sort(matched_words)


print("Original Word List:", word_list)
print("Regex Pattern:", regex_pattern)
print("Words Matching the Regex Pattern:", matched_words)

output_lines = []
if matched_words:
    X = matched_words[0]
    Y = ""
    if len(matched_words) == 1:
        output_lines.append(matched_words[0])
    elif len(matched_words) == 2:
        Y = matched_words[1]
        lcs = find_longest_common_subsequence(X, Y)
        output_lines.append(lcs)
    else:
        Z = matched_words[2]
        lcs_XY = find_longest_common_subsequence(X, Y)
        result = find_longest_common_subsequence(lcs_XY, Z)
        output_lines.append(result)

# Write output to the file "output.txt"
with open("output.txt", "w") as output_file:
    output_file.writelines(output_lines)
