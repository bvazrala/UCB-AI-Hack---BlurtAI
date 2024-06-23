from functions import get_answer_from_chatgpt, extract_text_from_pdf

def json_file_of_flashcards_from_string(stringOfPDF):
    question =  "Create a set of flashcards from PDF in the form of a JSON, making sure to cover every topic. Please format the JSON tags as follows:\n\"Frontside\": (Front of the card)\n\"Backside\": (Back of the card)\n\"Topic\": (The topic of the question)\n"
    context = "Call the following PDF:\n" + stringOfPDF
    return get_answer_from_chatgpt( question, context)