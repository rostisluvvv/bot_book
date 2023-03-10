import re

BOOK_PATH: str = "C:\Dev\stepik_AIOgram\\6bot_book\\book\Bredberi_Marsianskie-hroniki.txt"
PAGE_SIZE: int = 1050

book: dict[int, str] = {}


# func returns str with TXT and her size
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:

    text_with_punctuation_marks = text[start:start + size]

    text_on_page = text[start:start + size]
    text_on_page = re.split('[,.!:;?]', text_on_page)
    text_on_page = [x for x in text_on_page if x != '']

    del_word = text_on_page[len(text_on_page)-1:len(text_on_page)]
    del_word = ''.join(str(x) for x in del_word)
    correct_text = text_with_punctuation_marks.removesuffix(del_word)

    text_length = len(correct_text)

    if correct_text.endswith('?.') is True:
        del_word += '?.'
        return correct_text.removesuffix(del_word), text_length-len(del_word)

    return correct_text.removesuffix(del_word), text_length + len(del_word)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:

    num_string: int = 1
    with open(path, "r", encoding="utf-8") as file:
        txt = file.read()
        start: int = 0
        full_size_text = len(txt)
        while start < full_size_text and num_string <400:
            text, text_length = _get_part_text(txt, start, PAGE_SIZE)
            book[num_string] = text.lstrip()
            start += text_length
            num_string += 1

prepare_book(BOOK_PATH)

