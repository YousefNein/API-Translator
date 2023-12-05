# API-Translator

Word Translation and Audio Retrieval Script

This script utilizes the Google Translate API and a public dictionary API to translate English words into Arabic and retrieve audio links and example sentences. The translated data is then appended to a provided Excel file.

## Dependencies

- pandas
- googletrans
- requests

## Installation

Ensure that you have the required dependencies installed. You can install them using the following:

```bash
pip install pandas googletrans==4.0.0-rc1 requests
```
## Usage

1. Place the Excel file containing English words in a column labeled 'English Word' in the same directory as the script.
2. Update the script with the correct filename (e.g., 'sample.xlsx').
3. Run the script.

## Script Details

### `get_audio_and_example(word)`

This function takes an English word as input, queries a public dictionary API, and retrieves the audio link and an example sentence if available.

### `translate_and_update(row)`

This function translates an English word into Arabic using the Google Translate API and calls `get_audio_and_example` to obtain additional information. The results are then added as new columns in the DataFrame.

## Execution

The script reads the provided Excel file, applies the translation and update function to each row, and saves the modified DataFrame to a new Excel file ('sample_translated.xlsx').

## Note

- Ensure an internet connection during execution as the script relies on online translation and dictionary APIs.
- The Google Translate API key is not required for the current usage as it uses the free tier, but keep an eye on usage limits if making extensive use.
