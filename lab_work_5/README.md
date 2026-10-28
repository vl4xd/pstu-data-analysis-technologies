# Лабораторная работа №5

**Дисциплина:** «Технологии анализа данных DATAMINING»  
**Автор:** Платонов Владислав Алексеевич  
**Группа:** АСУ8-25-1м

## Структура проекта

```text
lab_work_5/
├── charts/             # Сохраненные графики в форматах `html` и `png`
│   ├── task_2.html
│   ├── task_3.html
│   ├── task_4.png
│   ├── task_5.png
│   ├── task_6.png
│   ├── task_7.png
│   ├── task_8.html
│   └── task_9.html
├── data/
│   └── weather1.csv 
├── docs/
│   └── Lab05.pdf       # Условие лабораторной работы
├── .gitignore
├── README.md
├── requirements.txt1   # Зависимости
└── solution.ipynb      # Решение (отчет) лабораторной работы
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