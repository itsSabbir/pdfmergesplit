from PyPDF2 import PdfReader, PdfWriter

def split_pdf(path, output_folder, pages_per_split):
    pdf_reader = PdfReader(path)
    total_pages = len(pdf_reader.pages)
    num_splits = total_pages // pages_per_split + (total_pages % pages_per_split > 0)

    for i in range(num_splits):
        pdf_writer = PdfWriter()
        start_page = i * pages_per_split
        end_page = min(start_page + pages_per_split, total_pages)

        for page in range(start_page, end_page):
            pdf_writer.add_page(pdf_reader.pages[page])

        output_filename = f'{output_folder}/split_{i + 1}.pdf'
        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        print(f"Created: {output_filename}")
