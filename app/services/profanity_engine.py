from better_profanity import profanity

def proccesing_text(text: str, char: str) -> dict:
    profanity.load_censor_words()
    appropriate = not profanity.contains_profanity(text)

    clean_text = profanity.censor(text, char)

    profanity_count = 0 if appropriate else clean_text.count(char *4)

    return {
        "clean_text": clean_text,
        "appropriate": appropriate,
        "amount_censorship": profanity_count
    }

