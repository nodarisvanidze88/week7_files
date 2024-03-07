files = ["text1.txt", "text2.txt", "text3.txt", "text4.txt"]
output = "final_result.txt"

def text_concatnate(iput_files, output_file):
    with open(output_file,"w") as outfile:
        for file in iput_files:
            with open(file,"r") as infile:
                outfile.write(infile.read()+"\n")

text_concatnate(files,output)
