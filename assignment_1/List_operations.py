def SAM(inlist):
    sum = 0
    for item in inlist:
        sum = sum + item
    print(f"Sum = {sum}\nAverage = {sum/len(inlist)}\n Max = {inlist.max()}")

def reverse_list(inlist: list[int]):
    return inlist.reverse()