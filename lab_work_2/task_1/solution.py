from pathlib import Path

import numpy as np


class IncorrectStudentCount:

    def __init__(self, data_path: Path):
        self.student_count: np.ndarray = self._read_attendance(data_path)

    def _read_attendance(self, data_path: Path) -> np.ndarray:
        with open(data_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            try:
                count_couples: int = int(first_line)
            except ValueError:
                raise ValueError(f'Ошибка в файле "{data_path}":\nКоличество пар "{first_line}" — количество пар должно быть целым числом.')
            couples_lower_boundary = 5
            couples_upper_boundary = 1000
            if count_couples < couples_lower_boundary or count_couples > couples_upper_boundary:
                raise ValueError(f'Ошибка в файле "{data_path}":\nКоличество пар "{count_couples}" — количество пар должно быть в пределах от {couples_lower_boundary} до {couples_upper_boundary}.')
            student_count = np.zeros(count_couples, dtype=int)
            count_lower_boundary = 0
            count_upper_boundary = 100
            for i in range(count_couples):
                line = file.readline().strip()
                try:
                    count = int(line)
                except ValueError:
                    raise ValueError(f'Ошибка в файле "{data_path}":\nКоличество учащихся "{line}" на "{i + 1}" паре — количество учащихся должно быть целым числом.')
                if count < count_lower_boundary or count > count_upper_boundary:
                    raise ValueError(f'Ошибка в файле "{data_path}":\nКоличество учащихся "{count}" на "{i + 1}" паре — количество учащихся должно быть в пределах от {count_lower_boundary} до {count_upper_boundary}.')
                student_count[i] = count
        return student_count

    def solve(self) -> None:
        q1, q3 = np.percentile(self.student_count, [25, 75])
        iqr = q3 - q1
        lower_boundary = q1 - 1.5 * iqr
        upper_boundary = q3 + 1.5 * iqr
        result = int(np.sum((self.student_count < lower_boundary) | (self.student_count > upper_boundary)))
        print(result)
