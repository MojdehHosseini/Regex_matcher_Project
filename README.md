# Regex_matcher_Project
**README**

**Pattern Matching and Longest Common Subsequence Algorithm**

This code provides an implementation of pattern matching using regular expression rules and employs a dynamic programming algorithm to find the Longest Common Subsequence (LCS) of two words. The code reads input from an "input.txt" file, performs the required operations, and writes the output to an "output.txt" file.

**Algorithm Overview**

1. **Pattern Matching using Regular Expression Rules:**

   The `match_pattern_with_word` function determines whether a given pattern matches a word based on regular expression rules. The algorithm utilizes dynamic programming with memoization to efficiently handle recursion. The steps include:

   - Evaluating the characters of the pattern and word.
   - Handling cases where characters match exactly or where the pattern character is '.' (indicating any character).
   - Handling the '*' character that signifies zero or more occurrences of the preceding character in the pattern. The recursion considers both possibilities: '*' matching zero occurrences or '*' matching one or more occurrences.

2. **Filtering and Sorting Words:**

   The `filter_words_matching_pattern` function filters words from a list that match a given pattern, utilizing the previously defined pattern matching algorithm. It returns a list of words satisfying the pattern.

   The `custom_sort` function sorts a list of words using the Selection sort algorithm. Words are sorted primarily by length and, in the case of equal lengths, by lexicographic order. This sorting ensures a structured list of matched words.

3. **Finding Longest Common Subsequence:**

   The `find_longest_common_subsequence` function uses dynamic programming to find the Longest Common Subsequence (LCS) of two words. The algorithm constructs a matrix `F` to store the LCS lengths of all possible substrings. It iterates through both words and fills the matrix based on character matches. Finally, it traces back the LCS from the matrix.

**How to Use**

1. **Input:** Provide the input data in the "input.txt" file in the following format:

   ```
   n           # Number of words in the dictionary
   word_1      # List of words
   word_2
   ...
   word_n
   pattern     # Regular expression pattern
   ```

2. **Execution:** Run the code. It reads the input from "input.txt," processes it, and writes the output to "output.txt."

3. **Output:** The output contains the original word list, the regular expression pattern, and the words matching the pattern, sorted by the custom sorting algorithm. If there are matching words, the Longest Common Subsequence (LCS) between selected pairs of words is also displayed.

Make sure to adjust the file names (`input.txt`, `output.txt`) and paths as needed.

This code serves as a practical demonstration of pattern matching using regular expressions and dynamic programming for finding the Longest Common Subsequence. It can be applied to various text processing and string matching tasks.
