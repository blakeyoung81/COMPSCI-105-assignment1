import textstat

def analyze(text):
    print("This privacy policy is called", path)
    ease = textstat.flesch_reading_ease(text)
    print("The reading level of the text is ", ease)
    grader = textstat.flesch_kincaid_grade(text)
    print("A student in grade ", grader, "would be able to read this document.")
    duration = textstat.reading_time(text, ms_per_char=14.69)
    print("At 15ms per character, it would take ", duration, "to finish this text.")
    sentences = textstat.sentence_count(text)
    print("There are ", sentences, "in this text.")
    print()

def readme(path):
    with open(path, encoding='utf8') as f:
        text = f.read().replace("\n", " ")
        f.close()

        analyze(text)

path = r"C:\Users\blake\OneDrive\Desktop\Coding\Python\Projects\Privacy policy\23 and me.txt"
readme(path)
path = r"C:\Users\blake\OneDrive\Desktop\Coding\Python\Projects\Privacy policy\Dana-farber cancer institute data science.txt"
readme(path)
path = r"C:\Users\blake\OneDrive\Desktop\Coding\Python\Projects\Privacy policy\snapchat.txt"
readme(path)
path = r"C:\Users\blake\OneDrive\Desktop\Coding\Python\Projects\Privacy policy\Netflix.txt"
readme(path)
path = r"C:\Users\blake\OneDrive\Desktop\Coding\Python\Projects\Privacy policy\Facebook.txt"
readme(path)
path = r"C:\Users\blake\OneDrive\Desktop\Coding\Python\Projects\Privacy policy\Google.txt"
readme(path)
path = r"C:\Users\blake\OneDrive\Desktop\Coding\Python\Projects\Privacy policy\apple.txt"
readme(path)