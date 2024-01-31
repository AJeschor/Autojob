# File: src/utils/spacy_init.py

The script `spacy_init.py` defines a Python class, `SpacyInitializer`, for initializing a SpaCy language processing pipeline. The class provides information about the configured SpaCy model and includes the following components:

## Class and Attributes:
- **`SpacyInitializer` class:**
  - Manages the initialization of a SpaCy model and holds information about its configuration.
  - Has attributes:
    - `model_name`: The name of the SpaCy model to be initialized.
    - `nlp`: The SpaCy language processing pipeline.

## Class-level Variables:
- **`_print_statements_executed` (bool):**
  - A flag to track whether print statements have been executed during the initialization process.

## Methods:
- **`__init__(self, model_name='en_core_web_lg')`:**
  - Initializes the SpacyInitializer instance.
  - Accepts an optional parameter for specifying the SpaCy model name.

- **`initialize_spacy_model(self)`:**
  - Initializes the SpaCy model, loads the specified model, and prints relevant information.
  - Returns the SpaCy language processing pipeline.

## Example Usage:
```python
# Example instantiation of SpacyInitializer
spacy_initializer = SpacyInitializer()
```

## Additional Information:
- The script also initializes and configures the SpaCy pipeline by adding components such as the "sentencizer," "merge_entities," and "merge_noun_chunks."

This script facilitates the consistent setup and initialization of SpaCy models, providing a convenient way to access and configure the language processing capabilities within a project.

---

*Note: The script's usage of GPU for SpaCy processing is determined dynamically, and it includes error handling to manage exceptions during the model initialization process.*
