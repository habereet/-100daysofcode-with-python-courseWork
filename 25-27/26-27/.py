import csv


ROLLTABLE = 'battle-table.csv'


def read_rolls(name):
    with open(ROLLTABLE) as roll_table:
        dict_reader = csv.DictReader(roll_table)
        for row in dict_reader:
            row_name = row['Attacker']
            if row_name == name:
                roll_list = []
                for k in row.keys():
                    if row[k].strip().lower() == 'lose':
                        roll_list.append(k)
                return roll_list
            else:
                pass
