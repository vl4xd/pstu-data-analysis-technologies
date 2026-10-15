# Лабораторная работа №3

**Дисциплина:** «Технологии анализа данных DATAMINING»  
**Автор:** Платонов Владислав Алексеевич  
**Группа:** АСУ8-25-1м

## Структура проекта

```text
lab_work_3/
├── data/
│   ├── global-electricity-generation.csv   # Производство электроэнергии по странам
│   ├── global-electricity-consumption.csv  # Потребление электроэнергии по странам
│   └── data2.csv                           # Данные о скидке и прибыли
├── docs/
│   ├── Lab03.pdf                           # Условие лабораторной работы
│   └── numpy_example.ipynb                 # Примеры работы с NumPy
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

## Технологии

- **Python** — язык программирования;
- **NumPy** — загрузка, обработка и анализ массивов данных;
- **SciPy** — решение систем линейных уравнений;
- **Matplotlib** — построение графиков;
- **Jupyter Notebook** — выполнение кода и представление результатов.