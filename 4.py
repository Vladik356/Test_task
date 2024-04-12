def sort_length(strings):

    sorted_ascending = sorted(strings, key=len)
    print("Сортировка по возрастанию: ", sorted_ascending)

    sorted_desceding = sorted(strings, key=len, reverse=True)
    print("Сортировка по убыванию: ", sorted_desceding)


strings = ["apple", "car", "cucumber", "rose", "table"]
sort_length(strings)
