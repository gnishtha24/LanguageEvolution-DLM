# Text Processing and Entropy Calculation Project

This project contains a series of Jupyter Notebooks designed for parsing English and Hindi text files, and calculating the entropy of dependency pairs. The notebooks utilize various libraries for natural language processing and data manipulation.

## Notebooks

### 1. English Parser (`English_Parser_ipynbza.ipynb`)
This notebook processes raw English text files, converting them into a tabular format for easier comprehension and manipulation. It allows for extraction in either CONLL-U or DOC formats.

#### Features:
- **Data Processing**: Converts raw English text files into a structured format.
- **Format Extraction**: Supports CONLL-U and DOC formats.
- **Libraries Used**: `torch`, `torchvision`, `stanza`, `python-docx`.

### 2. Hindi Parser (`Hindi_Parser_ipynbza.ipynb`)
This notebook processes raw Hindi text files, converting them into a structured tabular format. The output can be saved in both CONLL-U and DOC formats.

#### Features:
- **Data Processing**: Converts raw Hindi text files into a structured format.
- **Format Extraction**: Supports CONLL-U and DOC formats.
- **Libraries Used**: `stanza`, `python-docx`.
- 
### 3. Entropy Calculation (`Entropy_calc.ipynb`)
This notebook calculates the entropy of dependency pairs in parsed sentences. This can be used for linguistic analysis to understand the predictability and complexity of different grammatical structures.

#### Features:
- **Entropy Calculation**: Computes entropy values for dependency pairs.
- **Data Processing**: Utilizes `Counter` and `numpy` for calculating probabilities and entropy.
- **Libraries Used**: `numpy`, `pandas`, `collections`.

