def remove_nonchinese_and_replace_with_single_space(input_string):
    output_string = ""
    for character in input_string:
        if ord(character) >= 0x4e00 and ord(character) <= 0x9fff:
            output_string += character
        else:
            output_string += " "
    output_string = ' '.join(output_string.split())
    return output_string
