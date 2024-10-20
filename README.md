### Hexlet tests and linter status:
[![Actions Status](https://github.com/Robinwurst/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Robinwurst/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/5d612d7eaec422bef8ca/maintainability)](https://codeclimate.com/github/Robinwurst/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5d612d7eaec422bef8ca/test_coverage)](https://codeclimate.com/github/Robinwurst/python-project-50/test_coverage)


# Gendiff: Инструмент для сравнения файлов

## Описание

**Gendiff** — это инструмент командной строки, который позволяет сравнивать два файла (JSON и YAML) и генерировать различия между ними в разных форматах (stylish, plain, JSON). Программа поддерживает вложенные структуры данных и предоставляет гибкий выбор формата вывода.

## Основные возможности

- Сравнение файлов JSON и YAML.
- Генерация различий в форматах:
  - **Stylish**: Форматированный вывод, похожий на JSON.
  - **Plain**: Простой текстовый вывод.
  - **JSON**: Вывод в формате JSON.
- Поддержка вложенных структур данных.
- Удобный интерфейс командной строки.

## Установка
[![asciicast](https://asciinema.org/a/GuZ76uzKHfwcwwkIVm0yFOX1v.svg)](https://asciinema.org/a/GuZ76uzKHfwcwwkIVm0yFOX1v)
### 1. Клонирование репозитория

Сначала склонируйте репозиторий с GitHub:

```bash
git clone https://github.com/Robinwurst/python-project-50.git
cd python-project-50
```

### 2. Установка зависимостей и сборка пакета

Установите зависимости с помощью Poetry:

```bash
make install
make build
cd gendiff/tests/fixtures/
```

### 3. Использование

Теперь вы можете использовать `gendiff` для сравнения файлов. Пример использования:

```bash

gendiff file1.json file2.json
```
[![asciicast](https://asciinema.org/a/tHsx5w3enKPNCvHInm6N6wLXO.svg)](https://asciinema.org/a/tHsx5w3enKPNCvHInm6N6wLXO)

#### Доступные опции:

- `--format, -f`: Указать формат вывода (по умолчанию: stylish).

Пример с указанием формата вывода:

```bash
gendiff file1.json file2.json --format plain
```
[![asciicast](https://asciinema.org/a/H5H8Q2wj6Yo2O1A05eDPCW1IU.svg)](https://asciinema.org/a/H5H8Q2wj6Yo2O1A05eDPCW1IU)
## Примеры использования

### Сравнение двух JSON файлов

```bash
gendiff file1.json file2.json
```
[![asciicast](https://asciinema.org/a/1884OStsTuBLcb2QguGKEsz4n.svg)](https://asciinema.org/a/1884OStsTuBLcb2QguGKEsz4n)
### Сравнение двух YAML файлов с выводом в формате JSON

```bash
gendiff file1.yml file2.yml --format json

```
[![asciicast](https://asciinema.org/a/YsUAlWQm4jjtibSv9WSsnpQYp.svg)](https://asciinema.org/a/YsUAlWQm4jjtibSv9WSsnpQYp)

## Лицензия

Этот проект нелицензирован