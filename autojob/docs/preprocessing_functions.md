# File: autojob/src/preprocessing/preprocessing_functions.py

The script `preprocessing_functions.py` provides a collection of functions for the preprocessing of job post data, including text normalization, translation of acronyms and contractions, and various text transformations. Additionally, the script includes functions for loading, processing, and saving job post data in a structured manner. Below is a detailed explanation of each key component:

## Components:

### 1. Preprocessing Functions:
- **`preprocess_text(input_text)`:**
  - Translates acronyms and contractions in the input text and normalizes it using the `textacy` library.
  - Returns the preprocessed text.

- **`postprocess_text(text)`:**
  - Applies various postprocessing steps using `textacy` functions and regular expressions.
  - Removes accents, currency symbols, emails, emojis, hashtags, phone numbers, numbers, URLs, and user handles.
  - Normalizes punctuation, whitespace, and unicode characters.
  - Removes HTML tags and specific domain-related patterns.
  - Removes both SpaCy and custom stopwords.
  - Returns the postprocessed text.

### 2. Job Data Processing Functions:
- **`load_and_preprocess_job_data(file_path)`:**
  - Loads job post data from a file, preprocesses the description, and returns the data.
  - Returns a tuple containing job data and preprocessed description.

- **`extract_original_values(data)`:**
  - Extracts original values such as post ID, company, position name, job type, location, salary, posting date, URL, and external apply link from job post data.
  - Returns a tuple of original values.

### 3. Folder Creation and File Copying Functions:
- **`create_destination_folder_and_copy(src_file_path, dest_folder_path, post_id, original_company, original_position_name)`:**
  - Creates a destination folder and copies the original post data to the destination.
  - Uses original post data's post ID, company, and position name for file naming.

### 4. Data Saving Functions:
- **`save_preprocessed_data(dest_folder_path, post_id, data, preprocessed_description, processed_text, results_group, textacy_results, merged_keywords)`:**
  - Saves preprocessed data to a file, including original data, preprocessed and processed descriptions, and various extracted results.

- **`save_job_information(dest_folder_path, post_id, data, original_company, original_position_name, original_job_type, original_location, original_salary, original_posting_date, original_url, original_external_apply_link, job_info_group)`:**
  - Saves job information to a separate file, including original job data and additional extracted job information.

These functions collectively serve to standardize and enhance the preprocessing pipeline for job post data within the AutoJob project, ensuring consistency and facilitating further analysis and modeling efforts.
