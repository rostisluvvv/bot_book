import re

BOOK_PATH: str = "book/book.txt"
PAGE_SIZE: int = 1050

book: dict[int, str] = {}


# func returns str with TXT and her size
def _get_part_text(text: str, start: int, size: int):

    text_with_punctuation_marks = text[start:start + size]

    text_on_page = text[start:start + size]
    text_on_page = re.split('[,.!:;?]', text_on_page)
    text_on_page = [x for x in text_on_page if x != '']

    del_word = text_on_page[len(text_on_page)-1:len(text_on_page)]
    del_word = ''.join(str(x) for x in del_word)

    correct_text = text_with_punctuation_marks.removesuffix(del_word)

    return (correct_text, len(correct_text) )




# func create dict of book
def prepare_book(path: str) -> None:
    pass


prepare_book(BOOK_PATH)

text = 'Раз. Два. Три. Четыре. Пять. Прием!'

print(*_get_part_text(text, 5, 9), sep='\n')