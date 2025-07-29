def give_key():
    # paste API key between the quotes (eg: "54jhdjsjsksk890000jf3") and save the file
    k = "".strip()
    ##################################################################################
    if k != "":
        c =k
    else:
        c = 10
        raise ValueError("no key found, insert a valid api key")
    return c