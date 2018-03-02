# metadata
## Структура проекта
### Директория source_xmls/
Содержит в себе исходные файлы xml.
### Директория data_base_sources/
Содержит:
+ DBClasses.py - содержит описание классов для представления объектов базы данных в RAM.
+ DBD_const.py - содержит в себе DDL базы данных.
### Директория utils/
Содержит:
+ модуль minidom_fixed.py
+ XML_to_RAM_conversion.py - решение задачи [#1](https://github.com/Longblade/metadata/issues/1)
+ RAM_to_XML_conversion.py - решение задачи [#2](https://github.com/Longblade/metadata/issues/2)
+ RAM_to_DBD_conversion.py - решение задачи [#3](https://github.com/Longblade/metadata/issues/3)
+ DBD_to_RAM_conversion.py - решение задачи [#4](https://github.com/Longblade/metadata/issues/4)
### Корневая директория
+ dbd2xdb.py и xdb2dbd.py - для решения задачи [#5](https://github.com/Longblade/metadata/issues/5)
+ main.py - для решения задач [#1-#4](https://github.com/Longblade/metadata/issues/4)
