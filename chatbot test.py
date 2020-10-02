def respond(sentence):
    cleaned = preprocess_text(sentence)
    parsed = TextBlob(cleaned)
    pronoun, noun, adjective, verb = find_candidate_parts_of_speech(parsed)
    resp = check_for_comment_about_bot(pronoun, noun, adjective)
    if not resp:
        resp = check_for_greeting(parsed)
    if not resp:
        if not pronoun:
            resp = random.chice(NONE_RESPONSES)
        elif pronoun == 'I' and not verb:
            resp = random.choice(COMMENTS_ABOUT_SELF)
        else:
            resp = construct_response(pronoun, noun, verb)
    if not resp:
        resp = random. choice(NONE_RESPONSE)
    logger.info("Returning phrase '%s'", resp)
    filter_respose(resp)

    return resp

def find_candidate_parts_of_speech(parsed):
    pronoun = None
    noun = None
    adjective = None
    verb = None

    return pronoun, noun, adjective, verb
