# File: src/utils/spacy_init.py

import spacy
import spacy.cli
from spacy.language import Language
from spacy_download import load_spacy

class SpacyInitializer:
    """
    A class for initializing a SpaCy model and providing information about its configuration.

    Attributes:
        model_name (str): The name of the SpaCy model to be initialized.
        nlp (spacy.language.Language): The SpaCy language processing pipeline.

    Class-level Variables:
        _print_statements_executed (bool): A flag to track whether print statements have been executed.

    Methods:
        __init__(self, model_name='en_core_web_lg'): Initializes the SpacyInitializer instance.
        initialize_spacy_model(self): Initializes the SpaCy model and prints relevant information.

    Example:
        spacy_initializer = SpacyInitializer()
    """

    _print_statements_executed = False

    def __init__(self, model_name='en_core_web_lg'):
        """
        Initialize the SpacyInitializer instance.

        Parameters:
            model_name (str): The name of the SpaCy model to be initialized.
        """
        self.model_name = model_name
        self.nlp = self.initialize_spacy_model()

    def initialize_spacy_model(self):
        """
        Initialize the SpaCy model.

        Returns:
            spacy.language.Language: The SpaCy language processing pipeline.
        """
        try:
            # Load SpaCy model unconditionally
            nlp = load_spacy(self.model_name)

            # Execute print statements only if they haven't been executed yet
            if not SpacyInitializer._print_statements_executed:
                if spacy.prefer_gpu():
                    print("Using GPU for SpaCy processing.")
                else:
                    print("GPU not available. Using CPU for SpaCy processing.")
                print(f"Using SpaCy model: {self.model_name}")

                # Update the flag to indicate that print statements have been executed
                SpacyInitializer._print_statements_executed = True

            return nlp
        except Exception as e:
            print(f"Error initializing SpaCy model: {e}")
            return None

# Initialize SpaCy and SkillNER SkillExtractor
spacy_initializer = SpacyInitializer()
nlp = spacy_initializer.nlp
nlp.add_pipe("sentencizer", before="parser")
nlp.add_pipe("merge_entities")
nlp.add_pipe("merge_noun_chunks")
