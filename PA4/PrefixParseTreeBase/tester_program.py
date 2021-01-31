import sys
def compare(f1_, f2_, f3_):
    f1 = open(sys.path[0] + f1_)
    f2 = open(sys.path[0] + f2_)
    f3 = open(sys.path[0] + f3_, "w+")

    line_number = 1
    for line1, line2 in zip(f1, f2):
        if line1.strip() != line2.strip():
            print("Difference in line " + str(line_number))
            f3.write("Difference in line " + str(line_number) + "\n")
        line_number += 1

    f1.close()
    f2.close()
    f3.close()

if __name__ == "__main__":
    file1 = "/parse_out.txt"
    file2 = "/expected_out.txt"
    compare_fout = "/out_diff.txt"
    compare(file1, file2, compare_fout)