# File: autojob/src/keywords/keyword_utils.py

from collections import Counter

def merge_keyterms(data):
    merged_list = []
    
    for key in data:
        for entry in data[key]:
            # Remove numeric elements from the list
            entry_without_numeric = [item for item in entry[0].split() if not item.replace('.', '').isdigit()]
            # Join the elements back into a single string
            merged_list.append(' '.join(entry_without_numeric))
    
    return merged_list

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

