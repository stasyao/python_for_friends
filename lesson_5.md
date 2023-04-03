# Урок 5. Типы данных и их преобразование

## Что понимают под "типом данных"

В уроке 1 мы узнали о простейших объектах, без которых не обходится ни один Python-код:
- числа (объекты классов `int` и `float`)
- текст или "строка" (объекты класса `str`)

Эти объекты ещё называют *типами данных* (data type). Поэтому словосочетания "тип данных &mdash; целое число", "целое число", "объект класса `int`" обозначают по сути одно и то же.

**Запоминаем**: ничего страшного за словосочетанием *тип данных* не скрывается, это просто ещё одно обозначения для объектов чисел и текста. Помимо чисел и текста есть и другие типы данных, с ними мы познакомимся позднее.

## Как можно преобразовать данные одного типа в данные другого типа

Числа и текст можно *преобразовывать* друг в друга. Поясню на примерах:
- строку `'2'` можно преобразовать в целое число `2`
- целое число `2` можно преобразовать в строку `'2'`
- целое число `2` можно преобразовать в число с дробной частью `2.0`
- строку `'2.1'` можно преобразовать в число с дробной частью `2.1`
- число с дробной частью `2.1` можно преобразовать в строку `'2.1'`
- число с дробной частью `2.1` можно преобразовать в целое число `2`

Теперь то же самое, но только схематично с названиями классов и описанием возможных ограничений:
- `int` -> `str`
  - без ограничений, любое целое число можно преобразовать в строку
- `int` -> `float`
  - без ограничений, любое целое число можно преобразовать в число с дробной частью `.0`
- `float` -> `str`
  - без ограничений, любое число с дробной частью можно преобразовать в строку
- `float` -> `int`
  - без ограничений, любое число с дробной частью можно преобразовать в целое число
  - **внимание**: округления при преобразовании не происходит, просто отбрасывается дробная часть
  - поэтому `2.9` превратится в `2`, а не в `3`
- `str` -> `int`
  - **ограничение**: строка должна состоять **исключительно** из цифр
  - `'2'` &mdash; да
  - `'2a'` &mdash; нет
  - `'2.1'` &mdash; нет
- `str` -> `float`
  - **ограничение**: строка должна состоять исключительно из цифр и (опционально) одной точки, символизирующей начало дробной части
  - `'2'` &mdash; да
  - `'2.1'` &mdash; да
  - `'2.1a'` &mdash; нет
  - `'2.1.1` &mdash; нет

Если ограничения не соблюсти, интерпретатор выдаст ошибку класса `ValueError`.

По сути преобразование типов данных &mdash; не что иное, как создание из объекта одного класса объекта другого класса.

Синтаксически это выглядит так:
1. Обращаемся к классу, объект которого хотим создать (или, иными словами, *в объект которого* хотим преобразовать текущий объект)
2. *Вызываем* класс (мы помним, что объекты класса создаются именно путем вызова класса). Так же как и с вызовом функции, вызов класса оформляется круглыми скобками
3. При вызове класса *передаем* объект, который хотим преобразовать. Тут то же как с функциями, которым мы передаем объекты-аргументы для использования внутри функции.
4. В результате вызова класса нам *возвращается* объект этого класса.

Давайте отработаем эту схему в интерпретаторе на примере преобразования строки `'2'` в целое число `2`.

```py
>>> int('2')
2
>>>
```

1. `int` &mdash; обратились к классу, объект которого хотим создать
2. `()` &mdash; вызвали класс, чтобы объект был создан
3. `('2')` &mdash; при вызове передали объект строки `'2'`, чтобы *преобразовать* его в объект целого числа `2`
4. В результате выполнения выражения интерпретатор вернул нам `2`, заметьте, без кавычек, то есть перед нами целочисленный литерал, задача выполнена.

Потренируемся ещё, обратите внимание на ошибки, которые выдает интерпретатор, разберитесь в их причинах, исходя из правил, сформулированных выше.

```py
>>> int('135575')
135575
>>> int(2.9)
2
>>> float(2)
2.0
>>> float('2')
2.0
>>> float('2.9')
2.9
>>> str(2)  
'2'
>>> str(2.9)
'2.9'
>>> int('2.1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '2.1'
>>> int('a') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'a'
>>> float('2.1.1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '2.1.1'
>>>
```

**Запоминаем**:
- числа и текст можно создавать как непосредственно объявляя в коде в виде литералов (число `2`, текст `'2.1'`), так и путем *преобразования* чисел в текст и наоборот
- любое число можно преобразовать в текст, но не любой текст можно преобразовать в число
- преобразование &mdash; не что иное как создание нового объекта на базе существующего
- для преобразования нужно вызвать искомый класс (`int`, `str` и `float`) и передать ему объект, из которого мы хотим создать объект искомого класса.

## В чем важность преобразования чисел в строки и наоборот?

Давайте вспомним 1-й урок. Мы говорили о том, что у каждого объекта есть свой класс. Класс описывает, какими характеристиками (атрибутами) и функционалом (методами), будет наделен каждый конкретный объект (экземпляр), созданный из данного класса.

Иными словами, класс определяет как *объект будет себя вести*.

Теперь представим, что у вас есть **строковый объект** `'2'` и **целочисленный объект** `2`.

Как вы думаете, можно ли к числу `2` прибавить строку `'2'`?

Пробуем

```py
>>> 2 + '2'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Мы получили ошибку `TypeError`, в описании которой сказано, что нельзя использовать оператор `+` между объектами классов `int` (целыми числами) и `str` (текстами).

Истина проста: хотите сложите два числа, убедитесь, что участвующие в этой операции объекты **действительно относятся к классу чисел**.

Вообще, это одно из главных правил при отладке ошибок в коде &mdash; начать с того, а что вообще за объекты участвовали в операции, к какому классу они относятся и предусматривает ли соответствующий класс возможность конкретной операции.

В выражении `2 + '2'` второй объект не является объектом класса целых чисел. Исправим этот момент.

```py
>>> 2 + int('2')
4
>>>
```

Благодаря вызову класса `int` и передаче при вызове строки `'2'` мы получили целое число `2`, которое затем успешно прибавили к левой двойке.

Говоря об *арифметических операторах*, стоит отметить, что некоторые из них применимы и к строковым объектам. Просто результат будет отличаться от привычных нам арифметических операторов.

Смотрите:
- строку можно "сложить" со строкой. Это называется *конкатенация*. Эта операция возвращает новую строку состоящую из двух предыдущих;
- строку можно "умножить" на целое число `n`. Эта операция вернет новую строку состоящую из `n` повторений умноженной строки

Потренируемся:

```py
>>> 'привет, ' + 'мир'
'привет, мир'
>>> 'привет, ' * 3
'привет, привет, привет, '
>>>
```

Теперь представим, что перед вами две строки, содержащие цифры. Вы забыли перевести эти строки в объекты чисел.

Как вы думаете, что произойдёт при операции `'2' + '2'`? Правильно, вернется новая строка `'22'`.

**Запоминаем**:
- прежде чем провести какую-либо операцию, убедитесь, что в ней участвуют объекты подходящих для этой операции классов. `2` и `'2'` визуально очень похожи, но это объекты разных классов, и они будут себя по-разному вести, к примеру, при использовании оператора `+`
- использование объектов не тех классов может привести либо к ошибке, либо к результатам, которые вы явно не ожидали.

## Домашнее задание

Напишите программу по следующему плану.

1. Вывести в терминал приглашение пользователю ввести его имя. Текст приглашения: `Давайте знакомиться! Введите свое имя: `.

2. Принять пользовательский ввод и привязать его к переменной `username`.

3. Вывести в терминал сообщение в формате

`<username>, вам предстоит назвать мне подряд 2 числа, а я в ответ мгновенно скажу их сумму.`

4. Принять пользовательский ввод с первым числом. Текст приглашения: `Введите первое число`. Полученные данные привязать к переменной `first_number`

5. Принять пользовательский ввод со вторым числом. Текст приглашения: `Введите второе число`. Полученные данные привязать к переменной `second_number`.

6. Вычислить сумму полученных чисел, результат привязать к переменной `result`.

7. Вывести в терминал сообщение в формате

```
<username>, вот что получилось: <первое число> + <второе число> = <результат>
```

Напоминание: проверьте, объекты каких классов вы собираетесь складывать.