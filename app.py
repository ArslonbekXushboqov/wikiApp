import wikipedia as w

til = str(input('Tilni tanlang(uz, ru, en): '))
if til == 'uz':
    w.set_lang('uz')
    d = input('Nima haqida qidiryabsiz?\nYozing: ')
    uzr = w.summary(d)
    print(uzr)
elif til == 'en':
    w.set_lang('en')
    d = input('What are you looking for?\nWrite: ')
    enr = w.summary(d)
    print(enr)
elif til == 'ru':
    w.set_lang('ru')
    d = input('Что вы ищете?\nНапишите: ')
    rur = w.summary(d)
    print(rur)
