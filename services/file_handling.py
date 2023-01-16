import re

BOOK_PATH: str = "book/book.txt"
PAGE_SIZE: int = 100

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

    return correct_text, len(correct_text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:

    with open('C:\Dev\stepik_AIOgram\\6bot_book\\book\\book.txt', "r", encoding="utf-8") as file:
        txt = file.read()

        txt = re.sub(r"\s", " ", txt)

        out_txt = re.split(r"[()]", txt)

        return out_txt



# Вызов функции prepare_book для подготовки книги из текстового файла
print(prepare_book(BOOK_PATH))