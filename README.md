# Crop PDF file

This should remove data outside the cropped area.

## System Requirements

- Docker
- Flox
- Python

## Flox

```shell
flox init
# for Python version 3.13
flox install python313Packages.pymupdf
```

## Build Docker

```shell
docker build -t libreoffice-headless .
```

## Crop PDF

Create a sub-folder `1_raw`, and put all your PDF files in this folder.

Adjust the crop area in `line#52` as necessary

```shell
python crop_pdf.py
```

The cropped PDF files will be saved in a `2_cropped` sub-folder

## PDF to DOCX

```shell
docker run --rm -v $(pwd):/data libreoffice-headless libreoffice --headless --infilter="writer_pdf_import" --convert-to docx ./2_cropped/*.pdf --outdir ./3_docx
```

The cropped MS Word document will be saved in `3_docx` sub-folder

## DOCX to PDF

```shell
docker run --rm -v $(pwd):/data libreoffice-headless libreoffice --headless  --convert-to pdf:writer_pdf_Export ./3_docx/*.docx --outdir ./4_output
```

The final ouput PDFs will be written in `4_output` sub-folder.
