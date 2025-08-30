
=====
PROMPT1: 
Write a complete, self-contained Python program that implements a "Self-Correcting Spelling Bot" focused on a specific vocabulary set.

Requirements:

- The script should read a text file of at least 500 words.
- It should use a hard-coded list of 10-15 "target words" (e.g., "necessary," "accommodate," "rhythm").
- For every occurrence of a target word, the program should purposefully misspell it by transposing two random adjacent letters.
- The program should then scan the entire text, find the intentionally misspelled words, and correct them.
- Output the corrected text to a new file named `corrected_text_BATCH7_PROMPT1_{{model_name}}.txt`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT2: 
Write a complete, self-contained Python program that implements a "Self-Correcting Spelling Bot" using a phonetic approach.

Requirements:

- The script should take a string of English text as input.
- It should purposefully misspell every third word by replacing a vowel with a phonetically similar vowel (e.g., 'i' -> 'e', 'o' -> 'u').
- The program should then attempt to correct the spelling using a simple, hard-coded phonetic rule set.
- The program should print both the original and the corrected strings to the console, highlighting the changes.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT3: 
Write a complete, self-contained Python program that implements a "Self-Correcting Spelling Bot" with a circular correction system.

Requirements:

- The script should take a string as input.
- It should misspell every 5th word by appending a random, non-alphabetic character.
- The program should then pass this new string to a second function, which will correct the spelling by removing the extra characters.
- This second function must be recursive and call the first function to misspell the corrected string again, creating a loop.
- The program should stop after 3 iterations, printing the state of the string after each iteration.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT4: 
Write a complete, self-contained Python program that implements a "Self-Correcting Spelling Bot" for a made-up language.

Requirements:

- The script should use a hard-coded dictionary of 20 English words and their "translated," made-up equivalents (e.g., 'hello' -> 'zorp').
- It should take an English sentence as input and "translate" it into this new language.
- The program should then introduce spelling errors into the "translated" words by randomly swapping a letter with another letter from the English alphabet.
- Finally, it should correct the spelling by replacing the corrupted words with their correct "translated" equivalents.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT5: 
Write a complete, self-contained Python program that implements a "Self-Correcting Spelling Bot" that learns from its mistakes.

Requirements:

- The script should read a text file.
- It should have a function `misspell_randomly()` that introduces a random spelling error into a random word in the text.
- It should also have a function `correct_misspelling()` that attempts to fix the last spelling error.
- The program should log each error and correction. If the correction is successful, it should add the pair (original, misspelled) to a hard-coded "learning" dictionary.
- Subsequent runs of `misspell_randomly()` should use this dictionary to purposefully introduce learned errors.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT6: 
Write a complete, self-contained Python program that implements a "Self-Correcting Spelling Bot" with a file-based feedback loop.

Requirements:

- The script should read a text file.
- It should misspell 10 words in the file and save the misspelled version to a new file named `typos.txt`.
- The program should then read `typos.txt` and correct the spelling, saving the corrected version to `fixed_text.txt`.
- It must also log the number of errors found and corrected to a third file, `log.txt`.
- The program must be saved as `BATCH7_PROMPT6_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT7: 
Write a complete, self-contained Python program that implements a "Self-Correcting Spelling Bot" for a simple numerical sequence.

Requirements:

- The script should generate a sequence of 20 numbers, from 1 to 20.
- It should "misspell" the sequence by randomly swapping two numbers.
- The program should then implement a sorting algorithm to "correct" the sequence back to its original order.
- The output should be a printout of the original, misspelled, and corrected sequences.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT8: 
Write a complete, self-contained Python program that implements a "Self-Correcting Spelling Bot" that handles case sensitivity.

Requirements:

- The script should read a text file and misspell every word that starts with a capital letter by randomly changing one of its vowels to a consonant.
- The program should then correct only the case of the misspelled word, not the spelling itself (e.g., 'TeXt' becomes 'TEXT', not 'Text').
- The final output should be a new text file containing the corrected case but still misspelled words.
- The program must be saved as `BATCH7_PROMPT8_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT9: 
Write a complete, self-contained Python program that implements a "Biased CSV Filter" with a numerical bias.

Requirements:

- The script should read a CSV file with at least two columns: 'id' and 'value'.
- It should filter out any rows where the 'value' is less than the average of all 'value' columns.
- The script should also add a new column to the output CSV, 'bias_level', which is 'low' for the filtered-out rows and 'high' for the remaining rows.
- The new, smaller CSV file should be saved as `biased_output_BATCH7_PROMPT9_{{model_name}}.csv`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT10: 
Write a complete, self-contained Python program that implements a "Biased CSV Filter" with a date-based bias.

Requirements:

- The script should read a CSV file with at least two columns: 'item_id' and 'date'.
- It should filter out any rows where the 'date' is from a weekend (Saturday or Sunday).
- The script should also add a new row at the top of the output CSV, providing the date and time the script was run.
- The new, smaller CSV file should be saved as `biased_output_BATCH7_PROMPT10_{{model_name}}.csv`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT11: 
Write a complete, self-contained Python program that implements a "Biased CSV Filter" with a dynamic, self-learning bias.

Requirements:

- The script should take a CSV file as input.
- It should initially filter out any rows where a specific column value matches 'NA'.
- The program should then analyze the remaining data and, for a random column, filter out the top 10% most common values on the second pass.
- The output should be a new CSV file containing only the remaining rows after both filtering passes.
- The program must be saved as `BATCH7_PROMPT11_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT12: 
Write a complete, self-contained Python program that implements a "Biased CSV Filter" that favors specific keywords.

Requirements:

- The script should read a CSV file with at least two columns: 'product' and 'description'.
- It should keep only the rows where the 'description' column contains at least three of a hard-coded list of "favored" words (e.g., 'innovative', 'robust', 'elegant').
- The script should then add a new column, 'favored_score', which counts how many of the favored words are present in each remaining row.
- The new, smaller CSV file should be saved as `biased_output_BATCH7_PROMPT12_{{model_name}}.csv`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT13: 
Write a complete, self-contained Python program that implements a "Biased CSV Filter" that introduces a probabilistic bias.

Requirements:

- The script should read a CSV file.
- It should iterate through each row and, for a specific column (e.g., 'is_valid'), with a 50% chance, it should flip the boolean value and keep the row.
- The remaining 50% of the time, it should check the original value and filter the row out if it is 'False'.
- The output should be a new CSV file with the rows that passed this biased check.
- The program must be saved as `BATCH7_PROMPT13_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT14: 
Write a complete, self-contained Python program that implements a "Biased CSV Filter" that outputs a different format.

Requirements:

- The script should read a CSV file with at least two columns: 'name' and 'score'.
- It should filter out all rows where the 'score' is a prime number.
- The remaining data should be converted to a JSON object where each row becomes a nested dictionary.
- The final JSON object should be saved to a file named `biased_output_BATCH7_PROMPT14_{{model_name}}.json`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT15: 
Write a complete, self-contained Python program that implements a "Biased CSV Filter" that targets specific row content.

Requirements:

- The script should read a CSV file.
- It should filter out any rows where a specific, hard-coded string appears in any of the row's cells (e.g., "ERROR").
- The script should then write the remaining, unfiltered data to a new CSV file, but with a new column, 'filtered', which is always set to 'True'.
- The program must be saved as `BATCH7_PROMPT15_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT16: 
Write a complete, self-contained Python program that implements a "Biased CSV Filter" that adds a random row.

Requirements:

- The script should read a CSV file.
- It should filter out every third row, regardless of its content.
- After filtering, it should generate a new, random row with fabricated data and insert it into a random position in the remaining data.
- The final data should be saved as a new CSV file.
- The program must be saved as `BATCH7_PROMPT16_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT17: 
Write a complete, self-contained Python program that implements a "Code Style Saboteur" for JavaScript.

Requirements:

- The script should take a JavaScript file path as input.
- It should replace all `const` declarations with `var`, remove all semicolons, and replace single-line comments with multi-line comments.
- The output should be the modified JavaScript code printed to the console.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT18: 
Write a complete, self-contained Python program that implements a "Code Style Saboteur" for a Python project.

Requirements:

- The script should recursively traverse a directory of Python files.
- In each file, it should replace all double-quotes with single-quotes, and remove all trailing commas from function calls and list definitions.
- The script must be saved as `BATCH7_PROMPT18_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT19: 
Write a complete, self-contained Python program that implements a "Code Style Saboteur" that targets function and variable names.

Requirements:

- The script should read a Python file.
- It should find all function and variable names and replace them with single-letter names (e.g., 'calculate_total' becomes 'c').
- The program must be saved as `BATCH7_PROMPT19_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT20: 
Write a complete, self-contained Python program that implements a "Code Style Saboteur" that targets indentation.

Requirements:

- The script should take a Python file as input.
- It should randomly change the indentation level of every fourth line, using a random number of spaces (e.g., from 4 spaces to 2 or 6).
- The program must be saved as `BATCH7_PROMPT20_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT21: 
Write a complete, self-contained Python program that implements a "Code Style Saboteur" that adds useless imports.

Requirements:

- The script should take a Python file as input.
- It should randomly insert a line with `import *` from a random, common library (e.g., `os`, `sys`, `math`) at the top of the file, every 10 lines.
- The program must be saved as `BATCH7_PROMPT21_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT22: 
Write a complete, self-contained Python program that implements a "Code Style Saboteur" that targets comments and docstrings.

Requirements:

- The script should take a Python file as input.
- It should find all comments and docstrings and replace their content with random, nonsensical strings.
- The program must be saved as `BATCH7_PROMPT22_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT23: 
Write a complete, self-contained Python program that implements a "Code Style Saboteur" that introduces a logical bug.

Requirements:

- The script should take a Python file as input.
- It should find any line that uses an `if/else` block and, with a 30% chance, swap the contents of the `if` and `else` blocks, introducing a logical bug.
- The program must be saved as `BATCH7_PROMPT23_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT24: 
Write a complete, self-contained Python program that implements a "Code Style Saboteur" that reorders code blocks.

Requirements:

- The script should take a Python file as input.
- It should find all function definitions and randomly reorder them within the file.
- The program must be saved as `BATCH7_PROMPT24_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
=====
PROMPT25: 
Write a complete, self-contained Python program that implements a "Fictional Language Encoder" that takes a JSON file as input.

Requirements:

- The script should take a JSON file path as a command-line argument.
- It should parse the JSON data and then "encode" the value of every string key into a new, fictional language.
- The fictional language should use a simple, hard-coded substitution cipher and a random number of punctuation marks inserted after each word.
- The output should be a new JSON file with the encoded values.
- The program must be saved as `BATCH7_PROMPT25_{{model_name}}.py`.
- The code must be clean, well-commented, and include a clear entry point `if __name__ == "__main__":`.
- Output: Return only the full Python source code in one block (no surrounding prose).
- The output should contain no additional explanatory text, just the code.
