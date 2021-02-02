# Function that takes an list and writes that list with punctuation marks and "and"

def list_items(list):
    if len(list) == 0:
        aux_str = "No items to list."
        
        return aux_str

    elif len(list) == 1:
        aux_str = str(list[0]) + "."
        
        return aux_str

    elif len(list) == 2:
        aux_str = str(list[0]) + " and " + str(list[1]) + "."
        
        return aux_str

    else:
        aux_str = ""
        for i in range(len(list) - 2):
            aux_str += str(list[i]) + ", "
        aux_str += str(list[-2]) + " and "
        aux_str += str(list[-1]) + "."

        return aux_str