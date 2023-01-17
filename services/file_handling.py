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

    if correct_text.endswith('?.') is True:
        del_word += '?.'
        return correct_text.removesuffix(del_word), len(correct_text)-len(del_word)

    return correct_text.removesuffix(del_word), len(correct_text)


text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'

print(*_get_part_text(text, 0, 54), sep='\n')




# # Функция, формирующая словарь книги
# def prepare_book(path: str):
#
#     with open('C:\Dev\stepik_AIOgram\\6bot_book\\book\\book.txt', "r", encoding="utf-8") as file:
#         txt = file.read()
#         txt = re.sub(r"\s", " ", txt)
#         out_txt = re.split(r"[()]", txt)
#         return _get_part_text(out_txt[0], len(out_txt)-1, PAGE_SIZE)
#
#
#
# # Вызов функции prepare_book для подготовки книги из текстового файла
# print(prepare_book(BOOK_PATH))

