###Splits batch-scanned bill memo txt file into individual bill memo txt files based on given separator string###

def splitFile(inputFile, outputFolder):
    with open(inputFile, 'r', encoding='utf-8') as largeFile:
        content = largeFile.read()

    sections = content.split("Scanned with CamScanner")  # Separator text, example provided

    for i, section in enumerate(sections, start=1):
        # Create individual file names for each section based on the index
        outputFile = f"{outputFolder}/bill{i}.txt"

        # Write the section to a separate file
        with open(outputFile, 'w', encoding='utf-8') as output:
            output.write(section)


if __name__ == "__main__":
    corpus = "/path/to/data/corpus"   # Replace with the path to your large txt file
    bills = "/path/to/output/folder"  # Replace with the path to your output folder
    splitFile(corpus, bills)
