import re
from collections import Counter
from datetime import datetime
from pathlib import Path

import numpy as np


class NonUniformPizzeria:
    def __init__(self, data_path: Path):
            self.transactions: np.ndarray = self._read_transactions(data_path)
    
    def _read_transactions(self, data_path: Path) -> np.ndarray:
        
        number_of_translations = 0
        dates = []
        names = []
        costs = []
        with open(data_path, 'r', encoding='utf-8') as file:
            while True:
                line: str = file.readline().strip()
                if not line:
                    break
                match_date_and_separator = re.search(r'^\d{2}[.\/]\d{2}[.\/]\d{4}[ ,;]', line)
                # пропускаем если запись не содержит даты в нужном формате
                if not match_date_and_separator:
                     continue
                group_date_and_separator = match_date_and_separator.group()
                date, separator = group_date_and_separator[:-1], group_date_and_separator[-1]
                match_cost_and_separator = re.search(fr'{re.escape(separator)}\d+[.,]*\d{{0,2}}$', line)
                if not match_cost_and_separator:
                     continue
                group_cost_and_separator = match_cost_and_separator.group()
                formated_cost = group_cost_and_separator[1:].replace(',', '.')
                cost = float(formated_cost)
                name = line[match_date_and_separator.span()[1]:match_cost_and_separator.span()[0]]
                formated_name = name.strip(' \'"')
                if not formated_name:
                     continue
                formated_date = np.datetime64(f'{date[6:]}-{date[3:5]}-{date[0:2]}', 'D')
                dates.append(formated_date)
                names.append(formated_name)
                costs.append(cost)
                number_of_translations += 1
        transactions = np.zeros(number_of_translations, dtype={'names':('date', 'name', 'cost'), 'formats':('datetime64[D]', 'U1000', 'f8')})
        transactions['date'] = dates
        transactions['name'] = names
        transactions['cost'] = costs
        return transactions
    
    def solve(self) -> None:
        # а)
        pizza_counter = Counter(self.transactions['name'])
        sorted_pizza_counter = sorted(pizza_counter.items(), key=lambda item: item[1], reverse=True)
        str_result_1 = 'а)\n'
        for name, count in sorted_pizza_counter:
             str_result_1 += f'{name} - {count}\n'
        print(str_result_1.strip())
        # б)
        sorted_date_cost = {date: 0 for date in np.sort(np.unique(self.transactions['date']))}
        for transaction in self.transactions:
            sorted_date_cost[transaction['date']] += transaction['cost']
        str_result_2 = 'б)\n'
        for date, cost in sorted_date_cost.items():
            formated_date = date.astype(datetime).strftime('%d.%m.%Y')
            str_result_2 += f'{formated_date} {cost:.2f}\n'
        print(str_result_2.strip())
        # в)
        index_most_expensive_pizza = np.argmax(self.transactions['cost'])
        formated_date = self.transactions['date'][index_most_expensive_pizza].astype(datetime).strftime('%d.%m.%Y')
        print(f'в)\n{formated_date} {self.transactions['name'][index_most_expensive_pizza]} {self.transactions['cost'][index_most_expensive_pizza]:.2f}')
        # г)
        print(f'г)\n{np.mean(self.transactions['cost']):.2f}')
