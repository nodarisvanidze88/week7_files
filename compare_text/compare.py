def compare(file1,file2,output):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        dif_lines = []
        for line1,line2 in zip(f1,f2):
            if line1 != line2:
                dif_lines.append(f"File1: {line1}\nFile2: {line2}\n")
    
    with open(output, "w") as outfiel:
        outfiel.writelines(dif_lines)

compare("text1.txt","text2.txt", "result.txt")