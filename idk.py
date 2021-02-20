# #between-markers

#
# def between_markers(text: str, begin: str, end: str) -> str:
#     if begin not in text:
#         text1 = text.split(end)
#         text = text1[0]
#         return text
#     elif begin in text and end in text:
#         fst = text.index(begin)
#         nd = text.index(end)
#         if fst > nd:
#             return ''
#         text1 = text.split(end)
#         text = text1[0]
#         start = text.index(begin)
#         length = len(begin);
#         start += length
#         return text[start:]
#     elif end not in text:
#         text1 = text.split(begin)
#         text = text1[1]
#         return text
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(between_markers('What is >apple<', '>', '<'))
#
#     # These "asserts" are used for self-checking and not for testing
#     assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
#     assert between_markers("<head><title>My new site</title></head>",
#                            "<title>", "</title>") == "My new site", "HTML"
#     assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
#     assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
#     assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
#     assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
#     print('Wow, you are doing pretty good. Time to check it!')

# Your optional code here
# You can import some modules or create additional functions



#non-unique-elements




# def checkio(data: list) -> list:
#     new=[]
#     for i in data:
#         cnt=data.count(i)
#         if cnt>1:
#             new.append(i)
#             i+=-1
#         else:
#             continue
#     return new
#
#
# if __name__ == "__main__":
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
#     assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
#     assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
#     assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
#     print("It is all good. Let's check it now")

# def frequency_sort(items):
#     for i in items:
#         if items.count(i)==items.count(i+1):
#             print(items.count(i))
#             print("hi")
#         else:
#             print("no")
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))


#all-the-same
# ======================================================================
# Рассмотрите вот такой вариант решения этой задачи
# def all_the_same(elements):
#   if elements == [] or elements.count(elements[0]) == len(elements):
#       return True
#   return False
# ======================================================================


# from typing import List, Any
#
#
# def all_the_same(elements: List[Any]) -> bool:
#     length = len(elements)
#     cnt = 0
#     for i in range(length):
#         if length > 1:
#             if elements[-i] == elements[-i + 1]:
#                 cnt += 1
#             else:
#                 continue
#         else:
#             return True
#     if cnt == length:
#         return True
#     elif length == 0:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(all_the_same([1, 1, 1]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert all_the_same([1, 1, 1]) == True
#     assert all_the_same([1, 2, 1]) == False
#     assert all_the_same(['a', 'a', 'a']) == True
#     assert all_the_same([]) == True
#     assert all_the_same([1]) == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")




#date-and-time-converter
#  Сорі за дикі костилі)

# ===========================================================================
# Айайай! А как же словарь, который мы прозодили? )
# Помните, что дополнителые функции можно исользовать и надо разбивать задачу на подзадачи
months_mapper = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}

def date_time_formatter(*args) -> list:
    result = []
    for i in args:
        result.append(i if not i.startswith("0") else i[1])
    return result


def date_time(input_date_time: str) -> str:
    date_and_time = input_date_time.split(" ")
    date = date_and_time[0].split(".")
    time = date_and_time[1].split(":")
    day, hours, minutes = date_time_formatter(date[0], time[0], time[1])
    minutes_message = 'minutes' if minutes != '1' else 'minute'
    hours_message = 'hours' if hours != '1' else 'hour'
    return f"{day} {months_mapper[date[1]]} {date[2]} year {hours} {hours_message} {minutes} {minutes_message}"
  
  # ===========================================================================





# def date_time(time: str) -> str:
#     time=time.split(' ')
#     date=time[0]
#     hrs=time[1]
#     date=date.split(".")
#     hrs=hrs.split(":")
#     day=str(int(date[0]))
#     month=int(date[1])
#     year=date[2]
#     hour=str(int(hrs[0]))
#     minute=str(int(hrs[1]))
#     if month==1:
#         month="January"
#     elif month==2:
#         month="February"
#     elif month==3:
#         month="March"
#     elif month==4:
#         month="April"
#     elif month==5:
#         month="May"
#     elif month==6:
#         month="June"
#     elif month==7:
#         month="July"
#     elif month==8:
#         month="August"
#     elif month==9:
#         month="September"
#     elif month==10:
#         month="October"
#     elif month==11:
#         month="November"
#     elif month==12:
#         month="December"
#     new=""
#     new=day + " " +month + " " + year + " year "
#     if int(hour)==1:
#         new=new + hour + " hour "
#     else:
#         new=new + hour + " hours "
#     if int(minute)==1:
#         new = new + minute + " minute"
#     else:
#         new = new + minute + " minutes"
#     return new
#
# if __name__ == '__main__':
#     print("Example:")
#     print(date_time('01.01.2000 00:00'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
#     assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
#     assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
#     print("Coding complete? Click 'Check' to earn cool rewards!")




# def frequency_sort(items):
#     length=len(items)
#     for i in range(length):
#         print(items[i])
#         if items.count(items[-i])<items.count(items[-i+1]):
#             items[-i],items[-i+1]=items[-i+1],items[-i]
#     return items
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

