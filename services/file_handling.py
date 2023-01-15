import re

BOOK_PATH: str = "book/book.txt"
PAGE_SIZE: int = 1050

book: dict[int, str] = {}


# func returns str with TXT and her size
def _get_part_text(text: str):
    text_split = re.split('[,.!:;?]', text)
    text_split = [x for x in text_split if x != '']

    return text_split



# func create dict of book
def prepare_book(path: str) -> None:
    pass


prepare_book(BOOK_PATH)

text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'



# print(*_get_part_text(text, 22, 145), sep='\n')

print(_get_part_text(text))