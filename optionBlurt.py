from functions import get_answer_from_chatgpt, extract_text_from_pdf

def unknown_info_from_blurt(userInput, stringOfPDF):
    question =  + "Compare the userblurt with the PDF text to assess conceptual alignment and identify topics excluded from the user's blurt."
    context = "Call this text userInput:\n" + userInput + "\nCall this text PDF:\n" + stringOfPDF
    return get_answer_from_chatgpt( question, context)
    