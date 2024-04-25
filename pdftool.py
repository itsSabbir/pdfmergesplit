from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()
    for path in paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Merged file created: {output}")

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

def main():
    print("Welcome to PDF Tool!")
    print("Type 'merge' to merge PDFs or 'split' to split a PDF.")
    print("To merge, provide paths to the PDF files separated by spaces followed by '> output_filename.pdf'.")
    print("To split, provide the path to the PDF, the output folder, and the number of pages per split file.")
    
    command = input("Enter your command: ")
    args = command.split()
    
    if args[0].lower() == 'merge':
        if len(args) < 3:
            print("Not enough arguments for merging. Format should be: merge file1.pdf file2.pdf > output.pdf")
            return
        if '>' not in args:
            print("Missing '>' in command. Format should be: merge file1.pdf file2.pdf > output.pdf")
            return
        merge_index = args.index('>')
        paths = args[1:merge_index]
        output = args[merge_index + 1]
        merge_pdfs(paths, output)
    elif args[0].lower() == 'split':
        if len(args) != 4:
            print("Incorrect number of arguments for splitting. Format should be: split file.pdf output_folder pages_per_split")
            return
        path = args[1]
        output_folder = args[2]
        pages_per_split = int(args[3])
        split_pdf(path, output_folder, pages_per_split)
    else:
        print("Unknown command. Please type 'merge' or 'split'.")

if __name__ == "__main__":
    main()
