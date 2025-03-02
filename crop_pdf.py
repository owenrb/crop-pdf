import fitz
import os
import glob

def crop_pdf(input_folder, output_folder, crop_rect):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all PDF files in the input folder
    pdf_files = glob.glob(os.path.join(input_folder, "*.pdf"))

    # Process each PDF file
    for pdf_file in pdf_files:
        # Open the input PDF
        doc = fitz.open(pdf_file)
        
        # Get the base name of the file (without the folder path)
        file_name = os.path.basename(pdf_file)
        
        # Define the output path
        output_path = os.path.join(output_folder, file_name)
        
        # Create a new PDF for the cropped content
        new_doc = fitz.open()
        
        # Process each page in the PDF
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Define the crop area
            rect = fitz.Rect(crop_rect)
            
            # Create a new page in the new PDF with the cropped dimensions
            new_page = new_doc.new_page(width=rect.width, height=rect.height)
            
            # Copy the original page into the new page, clipped to `rect`
            new_page.show_pdf_page(
                new_page.rect,  # Fill the entire new page
                doc,            # Source PDF
                page_num,      # Page number in source PDF
                clip=rect,      # Clip to this region
            )
        
        # Save the new PDF
        new_doc.save(output_path)
        print(f"Cropped {file_name} and saved to {output_path}")

# Example usage
input_folder = "./1_raw"
output_folder = "./2_cropped"
crop_rect = (50, 120, 600, 720)  # Define the crop area (x0, y0, x1, y1)

crop_pdf(input_folder, output_folder, crop_rect)