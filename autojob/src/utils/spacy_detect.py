import spacy.util
import sys
import spacy

def get_installed_models():
    # Get a list of all installed spaCy models
    installed_models = spacy.util.get_installed_models()

    if not installed_models:
        print("No spaCy models are currently installed.")
    else:
        print("Installed spaCy models:")
        for model in installed_models:
            print(f"- {model}")
            get_model_path(model)

def get_virtualenv_path():
    # Get the path of the virtual environment if running within one
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        virtualenv_path = sys.prefix
        print(f"Running within a virtual environment located at: {virtualenv_path}")
    else:
        virtualenv_path = None
    return virtualenv_path

def get_model_path(model_name):
    # Load the spaCy model
    try:
        nlp = spacy.load(model_name)

        # Get the path to the loaded model
        model_path = nlp.path
        print(f"Path to spaCy model '{model_name}': {model_path}")
    except IOError:
        print(f"Error: Unable to load spaCy model '{model_name}'. Make sure it is installed.")

if __name__ == "__main__":
    get_installed_models()
    virtualenv_path = get_virtualenv_path()

    if virtualenv_path:
        print("Note: The installed spaCy models are within the virtual environment.")
