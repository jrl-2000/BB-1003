# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Jonathan Lopez
# BB 1003

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def count(repeats):
        if repeats in dict:
            dict[repeats] += 1
        else:
            dict.update({repeats: 1})
    String = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    dict = {}

    lst = String.split()

    for repeats in lst:
        count(repeats)

    for allKeys in dict:
        print(allKeys, end = " ")
        print(dict[allKeys], end = " ")
        print()








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
