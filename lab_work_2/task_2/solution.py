from pathlib import Path

import numpy as np


class TranslationСosts:

    def __init__(self, data_path: Path):
        self.costs: np.ndarray = self._read_costs(data_path)

    def _read_costs(self, data_path: Path) -> np.ndarray:
        with open(data_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            names: list[str] = first_line.split()
            second_line = file.readline().strip()
            number_of_translations: int = int(second_line)
            costs = np.zeros(len(names), dtype={'names':('name', 'cost'),'formats':('U100', 'i8')})
            costs['name'] = names
            for _ in range(number_of_translations):
                line: str = file.readline().strip()
                name, cost = line.split()
                costs['cost'][costs['name'] == name] += int(cost)
        return costs

    def solve(self) -> None:
        number_members = len(self.costs['name'])
        costs_sum = np.sum(self.costs['cost'])
        equal_costs = costs_sum / number_members
        costs_difference = self.costs['cost'] - equal_costs
        result: list[str] = []
        creditor_index = 0
        debtor_index = 0
        while creditor_index < number_members and debtor_index < number_members:
            if costs_difference[creditor_index] <= 0:
                creditor_index += 1
                continue
            if costs_difference[debtor_index] >= 0:
                debtor_index += 1
                continue
            # текущая сделка - положительное число
            if costs_difference[creditor_index] >= abs(costs_difference[debtor_index]):
                current_transaction = costs_difference[debtor_index] * -1
            else:
                current_transaction = costs_difference[creditor_index]
            
            costs_difference[creditor_index] -= current_transaction
            costs_difference[debtor_index] += current_transaction
            result.append(f'{self.costs['name'][debtor_index]} {self.costs['name'][creditor_index]} {current_transaction:.2f}')
        print(f'{len(result)}\n{'\n'.join(result)}')