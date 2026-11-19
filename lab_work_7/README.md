# Лабораторная работа №7

**Дисциплина:** «Технологии анализа данных DATAMINING»  
**Автор:** Платонов Владислав Алексеевич  
**Группа:** АСУ8-25-1м

## Структура проекта

```text
lab_work_6/
├── data/
│   └── База.csv            # Датасет
├── docs/
│   └── Lab07.pdf           # Условие лабораторной работы
├── .gitignore
├── README.md               # Описание проекта
├── requirements.txt        # Зависимости проекта
└── solution.ipynb          # Решение (отчет) лабораторной работы
```

## Установка

Перейдите в корневую папку проекта и создайте виртуальное окружение:

```bash
python -m venv .venv
```

Активируйте окружение.

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Установите зависимости проекта:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Запуск

Убедитесь, что датасет `boston.csv` находится в директории `data/`.

Запустите Jupyter Notebook из корневой папки проекта:

```bash
jupyter notebook solution.ipynb
```

После открытия ноутбука выполните все ячейки последовательно.