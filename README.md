# Wordle Solver Bot

This repository contains a Python script that implements a weighted algorithm to solve the popular online word game, Wordle. The algorithm analyzes the frequency of characters in each column of possible answers and searches for a word with the highest weighted score.

## Algorithm Overview

The Wordle Solver Bot uses a combination of information theory and heuristic techniques to optimize its guesses. The core algorithm works as follows:

1. **Frequency Analysis**: The bot calculates the frequency of each letter in each position across all valid guesses. This step helps identify common letter patterns and determine the most valuable positions to target.

2. **Weighted Scoring**: Based on the frequency analysis, the bot assigns a weighted score to each valid guess word. The score is calculated by summing the frequency values of each letter in the word, with higher weights given to more valuable positions.

3. **Intelligent Guessing**: The bot selects the word with the highest weighted score as its initial guess. For subsequent guesses, it eliminates invalid solutions based on the feedback from previous guesses and repeats the frequency analysis and weighted scoring process to find the next optimal word.

4. **Feedback Integration**: After each guess, the bot incorporates the feedback (correct, misplaced, and absent letters) to refine its list of possible solutions. This iterative process continues until the bot either solves the puzzle or exhausts all valid guesses.

## Performance

In testing against a large dataset of previous Wordle answers, the Wordle Solver Bot demonstrated impressive performance:

- It solved the puzzle in 3 or fewer guesses approximately 50% of the time.
- It consistently solved the puzzle within 6 guesses, achieving a 100% success rate.

This efficiency highlights the effectiveness of the algorithm in narrowing down the possibilities and quickly identifying the correct solution.

## Usage

To run the Wordle Solver Bot, navigate to the `testalgorithm.py` file in this repository and execute the script using Python. The bot will prompt you to enter the feedback from each guess and will continue suggesting optimal words until the puzzle is solved or all valid guesses are exhausted.

## Contributions

If you have any suggestions for improving the algorithm or the overall performance of the Wordle Solver Bot, feel free to open an issue or submit a pull request. Contributions are welcome!
