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

### 1. Клонирование репозитория

Сначала склонируйте репозиторий с GitHub:

```bash
git clone https://github.com/Robinwurst/python-project-50.git
cd gendiff
```

### 2. Установка зависимостей

Установите зависимости с помощью Poetry:

```bash
poetry install
```

### 3. Использование

Теперь вы можете использовать `gendiff` для сравнения файлов. Пример использования:

```bash
gendiff path/to/file1.json path/to/file2.json
```

#### Доступные опции:

- `--format, -f`: Указать формат вывода (по умолчанию: stylish).

Пример с указанием формата вывода:

```bash
gendiff path/to/file1.json path/to/file2.json --format plain
```

## Примеры использования

### Сравнение двух JSON файлов

```bash
gendiff path/to/file1.json path/to/file2.json
```

### Сравнение двух YAML файлов с выводом в формате JSON

```bash
gendiff path/to/file1.yml path/to/file2.yml --format json

```

## Лицензия

Этот проект нелицензирован