
from functions import get_answer_from_chatgpt, extract_text_from_pdf, json_from_string

def json_file_of_pretest_from_string(stringOfPDF):
    question =  "Create a mulitple choice pretest from PDF making sure to cover every topic. Please format the tags as follows:\n\"Question\": (The question)\n\"Answer1\": (the correct answer)\n\"Answer2\": (an incorrect answer)\n\"Answer3\": (another incorrect answer)\n\"Answer4\": (another incorrect answer)\n\"Topic\": (The topic of the question)\n"
    context = "Call the following PDF:\n" + stringOfPDF
    return json_from_string(get_answer_from_chatgpt( question, context))


  