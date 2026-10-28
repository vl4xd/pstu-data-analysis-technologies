# Лабораторная работа №5

**Дисциплина:** «Технологии анализа данных DATAMINING»  
**Автор:** Платонов Владислав Алексеевич  
**Группа:** АСУ8-25-1м

## Структура проекта

```text
lab_work_5/
├── data/
│   └── weather1.csv 
├── docs/
│   └── Lab05.pdf                           # Условие лабораторной работы
├── .gitignore
├── README.md
├── requirements.txt                        # Зависимости
└── solution.ipynb                          # Решение (отчет) лабораторной работы
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