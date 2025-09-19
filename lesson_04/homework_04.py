# from operator import index

adwentures_of_tom_sawer = """\
Tom gave   up     the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
print("______________________________\ntask 01\n")
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print(adwentures_of_tom_sawer.replace("\n", " "))

# task 02 ==
print("______________________________\ntask 02\n")
""" Замініть .... на пробіл
"""

print(adwentures_of_tom_sawer.replace("....", " ").replace("\n", " "))

# task 03 ==
print("______________________________\ntask 03\n")
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

spaces = "  "
without_double_spaces = adwentures_of_tom_sawer.replace("....", " ").replace("\n", " ")
i = 0
while i > -1:
    without_double_spaces = without_double_spaces.replace(spaces, " ")
    i = without_double_spaces.find(spaces)
    if i == -1:
        print(without_double_spaces)

# task 04
print("______________________________\ntask 04\n")
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(without_double_spaces.count("h"))

# task 05
print("______________________________\ntask 05\n")
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

print(len([ch for ch in without_double_spaces if ch.isupper()]))

# task 06
print("______________________________\ntask 06\n")
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

i = adwentures_of_tom_sawer.find("Tom") + 1
print(adwentures_of_tom_sawer.find("Tom", i))

# task 07
print("______________________________\ntask 07\n")
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = without_double_spaces.split(". ")
print(adwentures_of_tom_sawer_sentences)

# task 08
print("______________________________\ntask 08\n")
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
print("______________________________\ntask 09\n")
""" Перевірте чи починається якесь речення з "By the time".
"""
found = ([part for part in adwentures_of_tom_sawer_sentences if part.startswith("By the time")][0])
print(str(adwentures_of_tom_sawer_sentences.index(found)) + "rd sentences begins from 'By the time'")

# task 10
print("______________________________\nFinal task\n")
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print(len(adwentures_of_tom_sawer_sentences[-1].split(" ")))
