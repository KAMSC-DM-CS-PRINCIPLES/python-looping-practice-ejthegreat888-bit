def reverse_string(text):
    # TODO create reverse string function
    # HINT: Use for i in range(len(text) - 1, -1, -1): to go backwards
    # HINT: Build reversed_text character by character: reversed_text += text[i]
    # HINT: Start with reversed_text = ""
    # HINT: Return the reversed_text
    # HINT: NO SLICING ALLOWED - must use loops only
    string = ""
    for i in range(len(text)):
        string += text[len(text) - i]
    return string
    pass

if __name__ == "__main__":
    # create reverse string below this
    print(reverse_string("hello"))
    pass
