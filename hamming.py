# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Jonathan Lopez
# BB 1003

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    def hamming_distance(top, bot):
        misses = 0

        for i, c in enumerate(top):
            if c != bot[i]:
                misses += 1
        return misses
    if __name__ == "__main__":
        large_dataset = open('input3.txt').read()
        top, bot = large_dataset.split()
        dist = hamming_distance(top, bot)
        print(dist)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
