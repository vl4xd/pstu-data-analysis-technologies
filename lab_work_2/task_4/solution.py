from collections import Counter
from pathlib import Path


class Mbox:
    def __init__(self, data_path: Path):
        self.email_users: Counter = self._read_users(data_path)
        
    def _read_users(self, data_path: Path) -> Counter:
        
        email_users: Counter = Counter()
        with open(data_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('From '):
                    email_users[line.split()[1]] += 1
        return email_users

    def solve(self) -> None:
        print(f'Больше всех писем:\n{self.email_users.most_common(1)[0][0]} - {self.email_users.most_common(1)[0][1]}')
        print(f'Список всех адресов:\n{'\n'.join(self.email_users.keys())}')