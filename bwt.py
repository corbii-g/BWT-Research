def print_list(list):
    for i in range(len(list)):
        print(list[i])

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





if __name__ == "__main__":
    a = str(input("Inserisci una stringa: "))

    a_list = create_bwt_list(a)
    print_list(a_list)

    a_list = sorted(a_list)
    print("sorted:")
    print_list(a_list)

    print("Output:",get_bwt_output(a_list))