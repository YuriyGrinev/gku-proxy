from pandas import read_csv
import json


def make_valid_cnils(nums: str) -> str:
    clear_input = "".join(num for num in nums if num.isnumeric())
    if len(clear_input) != 11:
        return f"invalid data, length != 11: {nums=}"
    # 123-456-789 00
    return f"{clear_input[0:3]}-{clear_input[3:6]}-{clear_input[6:9]} {clear_input[9:]}"


def make_valid_telmob(phone: str) -> str:
    clear_input = "".join(num for num in phone if num.isnumeric())
    if len(clear_input) != 11:
        return f"invalid_data, length != 11: {phone=}"
    if clear_input[0] == '8':
        clear_input[0] = 7
    # +7 (987) 654-32-10
    return f"+{clear_input[0]} ({clear_input[1:4]}) {clear_input[4:7]}-{clear_input[7:9]}-{clear_input[9:]}"


def make_fio(fam: str, nam: str, otch: str) -> str:
    return f"{fam} {nam} {otch}"


def add_or_create_python_item(data: dict, item: dict) -> dict:
    if item['fio'] in data.keys():
        data[item['fio']].append(item)
    else:
        data[item['fio']] = [item, ]
    return data


def make_python_data(proccessed_dataframe: dict) -> dict:
    data = {}
    for item in proccessed_dataframe:
        add_or_create_python_item(data, item)
    return data


def write_result_py(result: dict, py_file: str):
    with open(py_file, 'w', encoding='utf8') as f:
        f.write('data_raw = ')
    with open(py_file, 'a', encoding='utf8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


def make_mock_data(csv_file, py_file):
    """
    Get data from given csv add proccess it to python file with 'data_raw' var for import.
    Add custom columns in addition to existing and remove all not listed in 'original_csv_headers'
    """
    original_csv_headers = {
        'Фамилия': 'fam',
        'Имя': 'nam',
        'Отчество': 'otch',
        'Городской телефон': 'tel',
        'Номер телефона': 'telmob',
        'ИНН ФЗ/ИП': 'inn',
        'СНИЛС': 'cnils',
        'Адрес прописки': 'adr',
        'Адрес': 'fadr',
    }

    custom_made_columns = {
        'ФИО': 'fio',
    }

    key_name_from_column_header = original_csv_headers | custom_made_columns

    csv_data = read_csv(csv_file,
                        usecols=original_csv_headers.keys(),
                        converters={'СНИЛС': make_valid_cnils,
                                    'Номер телефона': make_valid_telmob,
                                    'ИНН ФЗ/ИП': str}
                        )
    csv_data['ФИО'] = csv_data[['Фамилия', 'Имя', 'Отчество']].agg(' '.join, axis=1)
    csv_data['Городской телефон'] = ''
    csv_data.rename(columns=key_name_from_column_header, inplace=True)
    write_result_py(make_python_data(csv_data.to_dict(orient='records')), py_file)


make_mock_data('rdt_16862155977723.csv', 'rdt_16862155977723.py')
