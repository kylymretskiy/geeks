word = input("Введите слово на русс или англ: ")
count = 0
vowels = 0
consonants = 0

vowel_letters = "A a, E e, I i, O o, U u,А а, Е е, Ё ё, И и, О о, У у, Ы ы, Э э, Ю ю, Я я"
consonant_letters = 'B b, C c, D d, F f, G g, H h, J j, K k, L l, M m, N n, P p, Q q, R r, S s, T t, V v, W w, X x, Y y, Z z,Б б, В в, Г г, Д д, Ж ж, З з, Й й, К к, Л л, М м, Н н, П п, Р р, С с, Т т, Ф ф, Х х, Ц ц, Ч ч, Ш ш, Щ щ'

while word:
    if word == 'Токто':
        break
    count += 1
    first_let = word[0]


    if first_let in vowel_letters:
        vowels += 1
    elif first_let in consonant_letters:
        consonants += 1

    vowel_percent = (vowels / count) * 100
    consonant_percent = (consonants / count) * 100

    # word = word[1:]

print(f"Количество символов в слове: {count}")
print(f"Количество гласных: {vowels}")
print(f"Количество  согласных: {consonants}")
print(f'Гласные/согласные: {vowel_percent}/{consonant_percent}')


