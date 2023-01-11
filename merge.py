from PyPDF4 import PdfFileMerger
import os,argparse

def merge_pdfs(input_files: list, output_file: str):
    merger = PdfFileMerger(strict=False)
    for inp in input_files:
        bk = os.path.splitext(os.path.basename(inp))[0]
        merger.append(fileobj=open(inp, 'rb'), bookmark=bk)
    merger.write(fileobj=open(output_file, 'wb+'))
    merger.close()
    print(f"Successfully merged, view file at: {output_file}")

def parse_args():
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-i', '--input_directory', dest='input_dir',
                        type=str, required=True, help="Enter the path to the directory with your pdfs in")
    
    parser.add_argument('-o', '--output_file', dest='output_file',
                        required=True, type=str, help="Enter a valid output file to put merge pdfs in")
    args = vars(parser.parse_args())
    return args

def getFilesInDir(dir_supplied):
    to_merge = []
    print(dir_supplied)
    for file in os.listdir(dir_supplied):
        if file.endswith(".pdf"):
            to_merge.append(f"{dir_supplied}/{file}")
    tmp_merge = "\n".join(to_merge)
    print(f"Merging the following together: {tmp_merge}")
    return to_merge

if __name__ == "__main__":
    args = parse_args()
    to_merge = getFilesInDir(args["input_dir"])
    print(f"Output will be available at: {args['output_file']}")
    merge_pdfs(
        input_files=to_merge, 
        output_file=args['output_file'],
    )
