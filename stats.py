def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def count_characters_loop(book_text):
        char_counts = {}
        for char in book_text:
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        return char_counts


def sort_and_filter_char_list(char_list):
    alpha_list = [item for item in char_list if item["char"].isalpha()]
    alpha_list.sort(key=lambda x: x["num"], reverse=True)
    return alpha_list