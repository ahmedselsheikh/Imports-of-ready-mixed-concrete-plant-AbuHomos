import pandas as pd

df = pd.read_excel('تسجيل خامات المحطة.xlsx', sheet_name='خامات خرسانة')
NAME_OF_MATERIAL_HEAD = 'اسم الخامة'
QUANTITY_OF_MATERIAL_HEAD = 'الكميه'


def sum_if(column_of_define_sum_head=NAME_OF_MATERIAL_HEAD,
           column_to_sum_value_head=QUANTITY_OF_MATERIAL_HEAD):
    summ_column = df.groupby(column_of_define_sum_head)[column_to_sum_value_head].sum()
    return summ_column

# Calculate the total material in specified day or month


if __name__ == "__main__":
    print(sum_if())
    print(sum_if()['أسمنت سائب سي  وتر'])

