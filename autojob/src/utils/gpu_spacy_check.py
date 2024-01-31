from spacy_init import SpacyInitializer
import spacy

def check_gpu_detection():
    # Initialize the SpacyInitializer class with the desired model name
    spacy_initializer = SpacyInitializer(model_name='en_core_web_lg')

    # Check if GPU is preferred for spaCy processing
    if spacy.prefer_gpu():
        print("GPU is being detected and used for SpaCy processing.")
    else:
        print("GPU is not being detected. CPU is being used for SpaCy processing.")

if __name__ == "__main__":
    check_gpu_detection()
