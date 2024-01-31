# File: autojob/src/keywords/keyword_utils.py

from collections import Counter

def merge_similar_strings(list_of_strings, threshold=0.5):
    merged_strings = []

    for current_string in list_of_strings:
        add_to_existing = False
        current_word_count = Counter(current_string.split())

        for index, existing_string in enumerate(merged_strings):
            existing_word_count = Counter(existing_string.split())

            common_words = set(current_word_count.keys()) & set(existing_word_count.keys())
            total_words = len(set(current_word_count.keys()) | set(existing_word_count.keys()))

            similarity_percentage = len(common_words) / total_words

            if similarity_percentage > threshold:
                merged_strings[index] += " " + current_string
                add_to_existing = True
                break

        if not add_to_existing:
            merged_strings.append(current_string)

    # Remove duplicate words within each string
    merged_strings = [' '.join(list(set(string.split()))) for string in merged_strings]

    return merged_strings

# Function to merge similar keywords
def merge_keywords(textacy_results):
    """
    Merge similar keywords from different extraction algorithms.

    Parameters:
    - textacy_results (dict): Dictionary containing keyterms extracted using textacy.

    Returns:
    - dict: Dictionary with merged keyterms.
    """
    # Extracting the string values from the textacy_results
    scake_strings = textacy_results.get("scake_keyterms", [])
    textrank_strings = textacy_results.get("textrank_keyterms", [])
    singlerank_strings = textacy_results.get("singlerank_keyterms", [])
    positionrank_strings = textacy_results.get("positionrank_keyterms", [])

    # Combining the lists
    combined_strings = [item[0] for sublist in [scake_strings, textrank_strings, singlerank_strings, positionrank_strings] for item in sublist]

    # Merging similar strings with unique words
    merged_strings = merge_similar_strings(combined_strings, threshold=0.5)

    # Output the merged_strings to a dictionary
    merged_keywords = {
        'merged_strings': merged_strings
    }

    return merged_keywords

