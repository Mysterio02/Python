# This program asks the user for a line of text,
# and then print the line of text backward.
# Reference:
# https://www.journaldev.com/23763/python-remove-spaces-from-string


def get_text():
    print("Enter text:")
    text = input().strip()
          
   
    return text


def display_text(text):
    text = text
    print(" ".join(text[::-1].split()))
   

def main():
    text = get_text()
    display_text(text)
   
   
main()  
    