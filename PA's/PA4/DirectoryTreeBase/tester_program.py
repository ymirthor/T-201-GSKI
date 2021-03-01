import sys
import correct_directories as working_program
import directories_program as testing_program

def run_directories_test(program, fin_, fout_, safe_mode):
    orig_stdin = sys.stdin # Interactive input
    orig_stdout = sys.stdout # Used for the output of print

    fin = open(sys.path[0] + fin_)
    sys.stdin = fin

    fout = open(sys.path[0] + fout_, 'w+')
    sys.stdout = fout

    if safe_mode:
        try:
            # Try to run a program
            program.run_directories_program()
        except:
            # Output if program fails
            sys.stderr.write("Exiting directory program in a BAD way\n")
    else:
        program.run_directories_program()

    sys.stdin = orig_stdin
    sys.stdout = orig_stdout
    fout.close()

def compere(f1_, f2_, f3_):
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
    safe_mode = False
    program1 = working_program
    program2 = testing_program
    fin = "/ymirs_commands.txt"
    fout1 = "/out_correct.txt"
    fout2 = "/out_test.txt"

    run_directories_test(program1, fin, fout1, safe_mode)
    run_directories_test(program2, fin, fout2, safe_mode)

    compere_fout = "/out_diff.txt"

    # compere(fout1, fout2, compere_fout)