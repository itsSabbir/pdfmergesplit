# PDF Tool

## Overview
PDF Tool is a Python-based command-line utility that allows users to merge multiple PDF files into a single PDF and split a single PDF into multiple smaller files based on the number of pages. This tool is designed to be simple and easy to use, making it a great asset for handling basic PDF manipulations directly from the command line.

## Features
- **Merge PDFs**: Combine multiple PDF files into one.
- **Split PDFs**: Divide a PDF into smaller chunks, specifying the number of pages per split.

## Requirements
- Python 3.x
- PyPDF2 library

## Installation
1. Ensure that Python 3.x is installed on your system. If not, you can download and install it from [Python's official site](https://www.python.org/downloads/).
2. Install PyPDF2 using pip:
   ```bash
   pip install PyPDF2
   ```

## Usage

### Merging PDFs
To merge multiple PDF files, follow the syntax below:
```
python pdf_tool.py merge file1.pdf file2.pdf > output.pdf
```
- `merge`: Command to initiate the merging process.
- `file1.pdf file2.pdf`: List of PDF files to merge. You can add more files separated by spaces.
- `>`: Separator to specify the output file.
- `output.pdf`: The name of the output file where the merged PDF will be saved.

### Splitting PDFs
To split a PDF into smaller files containing a specific number of pages, use the following syntax:
```
python pdf_tool.py split file.pdf output_folder pages_per_split
```
- `split`: Command to initiate the splitting process.
- `file.pdf`: The PDF file to split.
- `output_folder`: The folder where the split files will be saved.
- `pages_per_split`: The number of pages each split file should contain.

## Examples
- **Merging PDFs**:
  ```bash
  python pdf_tool.py merge example1.pdf example2.pdf > merged_output.pdf
  ```
- **Splitting PDFs**:
  ```bash
  python pdf_tool.py split largefile.pdf splits 5
  ```

## Future Enhancements
- **GUI Interface**: Implement a graphical user interface to make it more accessible for non-technical users.
- **Encryption/Decryption**: Add functionality to encrypt or decrypt PDF files.
- **PDF Optimization**: Include features for PDF compression and optimization to reduce file size.
- **Advanced Splitting Options**: Introduce more flexible splitting options like splitting by bookmarks or chapters.

## Contributing
Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request.

## License
Distributed under the GPL-3 License. See `LICENSE` for more information.

## Acknowledgements
- Thanks to PyPDF2, a fantastic library that made this tool possible.


