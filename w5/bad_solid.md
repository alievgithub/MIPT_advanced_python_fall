# Нарушения принципов SOLID в `bad_solid.py`
___
- Нарушается _single responsibility_, так как администратор выполняет несколько задач, так еще и не входящих в его обязанности

- В связи с отсутствием _single responsibility_, и не соответствию задач классу, _open-close_ программы будет почти невозожен

-  _Liskov substitution_ в данном случае не нарушен, так как подкласс серьезно не меняет методы суперкласса, меняя только `repair_car` и не требуя ничего нового