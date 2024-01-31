import json
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

# Read data from the JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# Extracting the string values from the "textacy_results" key
scake_strings = [item[0] for item in data["textacy_results"].get("scake_keyterms", [])]
textrank_strings = [item[0] for item in data["textacy_results"].get("textrank_keyterms", [])]
singlerank_strings = [item[0] for item in data["textacy_results"].get("singlerank_keyterms", [])]
positionrank_strings = [item[0] for item in data["textacy_results"].get("positionrank_keyterms", [])]

# Combining the lists
combined_strings = scake_strings + textrank_strings + singlerank_strings + positionrank_strings

# Merging similar strings with unique words
merged_strings = merge_similar_strings(combined_strings, threshold=0.5)

# Output the merged_strings to a JSON file
with open("merged_strings.json", "w") as output_file:
    json.dump(merged_strings, output_file, indent=2)

print("Merged strings with unique words saved to 'merged_strings.json'")
