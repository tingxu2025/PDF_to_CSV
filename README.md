
# PDF to CSV Converter Tool

This tool allows you to convert selected PDF files into CSV format using the **Tabula** library.
It is designed to work with both bordered (structured) and non-bordered (unstructured) table PDFs.

## Features
- Batch select multiple PDF files via file dialog
- Automatically saves the converted CSV in the same folder as the PDF
- Supports both bordered and non-bordered tables

## How to Use
1. Make sure you have Java installed (Tabula requires Java).
2. Install the required Python package:
   ```bash
   pip install tabula-py
   ```
3. Run the script:
   ```bash
   python pdf_to_excel.py
   ```
4. Select the PDF files you want to convert in the pop-up file dialog.
5. Converted CSV files will be saved in the same folder as the source PDFs.

## Important Notes
- **Set `lattice=True`** if your PDF contains **bordered tables** (with visible gridlines).
- **Set `lattice=False`** if your PDF contains **non-bordered tables** (no visible gridlines).

```python
tabula.convert_into(
    input_path=input_path,
    output_path=output_path,
    output_format="csv",
    pages="all",
    lattice=True  # Change to False if tables have no borders
)
```

## Example Adjustment:
For non-bordered tables, modify this line in `pdf_to_excel.py`:
```python
lattice=True  ➔  lattice=False
```
