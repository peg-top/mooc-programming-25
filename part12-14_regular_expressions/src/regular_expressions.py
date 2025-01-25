# Write your solution here
import re

def is_dotw(my_string: str):
    return bool(re.fullmatch(r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b", my_string))

def all_vowels(my_string: str) -> bool:
    return bool(re.fullmatch(r"[aeiouAEIOU]*", my_string))

def time_of_day(my_string: str) -> bool:
    # Regular expression to validate 24-hour time format HH:MM:SS
    return bool(re.fullmatch(r"([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]", my_string))

if __name__ == "__main__":
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))

    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))

