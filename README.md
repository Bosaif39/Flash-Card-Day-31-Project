# **Flashcard App for Learning Arabic Words**

## **Overview:**
This is the Day 31 project from the 100 Days of Code: The Complete Python Pro Bootcamp.

This is a Python-based flashcard app designed to help users learn Arabic vocabulary. It provides an interactive way to study Arabic words by showing flashcards with their English counterparts. The app includes a feature to track progress and automatically skips known words, allowing users to focus on learning new ones.

This project was created using Python's `tkinter` library for the graphical user interface and `pandas` to store and manage the vocabulary list.

## **How It Works:**

1. **Start the App**: When you open the app, a flashcard will be displayed with an Arabic word on the front.
2. **Flip the Card**: After 3 seconds, the card will automatically flip, revealing the English translation.
3. **Mark Words as Known**: If you know the word, click the "Check" button to mark it as known, and the word will be removed from your study list.
4. **Track Progress**: The app keeps track of the words you’ve learned and stores them in `words_to_learn.csv` to avoid showing them again.
5. **Random Word Selection**: Each flashcard is selected randomly from the list of words you need to learn.
6. **CSV File**: The list of words to be learned is saved in `words_to_learn.csv`, and new words can be added manually by modifying the `words.csv` file.

## **Features:**

* **Arabic-to-English Flashcards**
* **Automatic Card Flip**
* **Track Progress**
* **Simple and Clean UI**

## **Example:**

![Flashcard App Example](https://github.com/Bosaif39/example-pics/blob/main/D_31.png?raw=true)

## **Requirements:**

* **Python 3.x**: Ensure you are using Python 3.x.
* `tkinter` (usually pre-installed with Python)
* `pandas` (for handling CSV files)
* `random` (to randomly select words from the list)
