import re

def emails_in_txt(input_file:str):
    pattern_of_email = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    list_of_emails = []
    with open(input_file, "r") as file:
        whole_file = file.read()
        list_of_words = whole_file.split()
        for word in list_of_words:
            email = re.fullmatch(pattern_of_email, word)
            if email:
                list_of_emails.append(word)
    return list_of_emails


print(emails_in_txt("testowy.txt"))


