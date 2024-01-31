

# Pip

```bash
python -m venv .env
source .env/bin/activate
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_trf
```

```bash
# Installing Pytorch

# Pytorch with CPU
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Pytorch with GPU / CUDA 11.8
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```



## Poetry (former)

While inside the directory containting the `pyproject.toml` file:

```bash
poetry env use python3.9

poetry shell

poetry run python -m spacy download en_core_web_trf

poetry install
```

```toml
[tool.poetry]
name = "autojob"
version = "0.1.0"
description = "AutoJob is a Python project designed to streamline job application processes and enhance resume creation. It combines natural language processing and AI-driven content generation to help job seekers create tailored resumes based on job descriptions"
authors = ["Alex Jeschor"]
license = "CC BY-NC 4.0"
readme = "README.md"

[tool.poetry.dependencies]
python = "3.9"
spacy = "^3.7.2"
skillNer = "^1.0.3"
fuzzywuzzy = "^0.18.0"
summa = "^1.2.0"
date-location-extractor = "^0.1.1"
textacy = "^0.13.0"
keyword-spacy = "^0.1.2"
spacy-ke = "^0.1.4"
Flask = "^3.0.0"
en_core_web_trf = {url = "https://github.com/explosion/spacy-models/releases/download/en_core_web_trf-3.7.3/en_core_web_trf-3.7.3.tar.gz"}
pytextrank = "^3.2.5"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
