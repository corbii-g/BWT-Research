def print_list(list):
    for i in range(len(list)):
        print(list[i])
    print()

def create_bwt_list(bwt_string):
    new_string = bwt_string + "$"
    bwt_list = [new_string]

    for i in range(len(bwt_string)):
        new_string = new_string[1:] + new_string[0]
        bwt_list.append(new_string)
    return bwt_list
    
def get_bwt_output(bwt_list):
    output = ""
    for i in range(len(bwt_list)):
        output += bwt_list[i][-1]
    return output

# Radix LSD O(n * L)
def sort_list(bwt_list):
    
    if len(bwt_list) <= 1:
        return bwt_list
    
    length = len(bwt_list[0])

    for i in range(length - 1, -1, -1):
        counts = [0] * 257
        
        for s in bwt_list:
            counts[ord(s[i]) + 1] += 1
        
        for j in range(256):
            counts[j + 1] += counts[j]

        output = [None] * len(bwt_list)

        for s in bwt_list:
            c = ord(s[i])
            output[counts[c]] = s
            counts[c] += 1

        bwt_list = output

    return bwt_list



if __name__ == "__main__":
    a = str(input("Inserisci una stringa: "))

    a_list = create_bwt_list(a)
    print_list(a_list)

    a_list = sort_list(a_list)
    print("sorted:")
    print_list(a_list)

    print("Output:",get_bwt_output(a_list))