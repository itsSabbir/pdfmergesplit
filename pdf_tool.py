from merge_pdf import merge_pdfs
from split_pdf import split_pdf

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
