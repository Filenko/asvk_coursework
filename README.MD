# Инструкция по использованию системы.

## Установка на центральный сервер

- Создать пользователя balance и в нем:
  - Установить git, python3
  - Скопировать файл balance.py в домашний каталог

Добавить 
```shell
ForceCommand balance.py "$@"
```
в sshd_config файл (/etc/openssh/sshd_config)

## Установка на конечные сервера:

- Установить python3, git
- Создать пользователя onserver
- Зайти на пользователя и в нем разархивировать файл onserver.tar
- Вернуться на root, выполнить

```shell
loginctl enable-linger onserver
```

- Перезагрузить сервер 


## Как использовать клиент:

```shell
ssh balance@<ip address> <name>
```

## Как работает scp

* Необходимо выполнить команду ssh balance@<ip address> python3 balance.py giveAddress
* Она вернет ip адрес севрера, к которому вас подключит.
* Затем выполнить команду ```shell rsync -avz -partial --progress --rsh="ssh -J balance@192.168.1.57" ~/path <name>@<address of server>:~/```
