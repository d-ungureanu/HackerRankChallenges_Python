if __name__ == '__main__':
    N = int(input())
    the_list = []
    for i in range(0, N):
        input_txt = input()
        input_arr = input_txt.split()
        if "insert" in input_txt:
            the_list.insert(int(input_arr[1]), int(input_arr[2]))
        elif "print" in input_txt:
            print(the_list)
        elif "append" in input_txt:
            the_list.append(int(input_arr[1]))
        elif "sort" in input_txt:
            the_list.sort()
        elif "reverse" in input_txt:
            the_list.reverse()
        elif "pop" in input_txt:
            the_list.pop()
        elif "remove" in input_txt:
            the_list.remove(int(input_arr[1]))
