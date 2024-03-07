from ksy import Tinydb
import csv
import os
from datetime import datetime, timedelta

def microsoft_to_iso8601(microsoft):
    base_date = datetime(1, 1, 1)
    ret_date = base_date + timedelta(days=microsoft)
    return ret_date.isoformat()

def delete_middle_block(file_path):
    block_size = 221188
    with open(file_path, 'rb') as file:
        data = file.read()
    start_index = 13766
    end_index = start_index + block_size
    new_data = data[:start_index] + data[end_index:]
    with open(file_path, 'wb') as file:
        file.write(new_data)

def parse_tdb(file_n):
    parsed_file = Tinydb.from_file(file_n)
    for n in range(1024):
    #for n in range( parsed_file.tables[0].tableheader.recordtotal):
        try:
            raw_parsed_table = parsed_file.tables[0].tableheader.rectable.table[n]
            temp_code = raw_parsed_table.fileds[0]
            temp_master = raw_parsed_table.fileds[1].text
            temp_welder = raw_parsed_table.fileds[2].text
            temp_expert = raw_parsed_table.fileds[3].text
            temp_param = raw_parsed_table.fileds[4].text
            temp_name = raw_parsed_table.fileds[5].text
            temp_date = raw_parsed_table.fileds[6].datebin
            temp_time = raw_parsed_table.fileds[7].timebin
            temp_datetime = microsoft_to_iso8601(temp_date + temp_time * 0.00000001)
            temp_v = raw_parsed_table.fileds[8]
            temp_s = raw_parsed_table.fileds[9]
            temp_t = raw_parsed_table.fileds[10]
            temp_u1 = raw_parsed_table.fileds[11]
            temp_u2 = raw_parsed_table.fileds[12]
            temp_i = raw_parsed_table.fileds[13]
            temp_p = raw_parsed_table.fileds[14]
            temp_l = raw_parsed_table.fileds[15]
            temp_li = raw_parsed_table.fileds[16]
            temp_zkz = raw_parsed_table.fileds[17]
            temp_vf = raw_parsed_table.fileds[18]
            temp_vl = raw_parsed_table.fileds[19]
            temp_scol = raw_parsed_table.fileds[20].text
            temp_fkz = raw_parsed_table.fileds[21].text
            temp_tu = raw_parsed_table.fileds[22].text
            temp_q = raw_parsed_table.fileds[23]

            temp_data = [temp_code, temp_master, temp_welder, temp_expert,
                         temp_param, temp_name, temp_datetime, temp_v,
                         temp_s, temp_t, temp_u1, temp_u2,
                         temp_i, temp_p, temp_l, temp_li,
                         temp_zkz, temp_vf, temp_vl, temp_scol,
                         temp_fkz, temp_tu, temp_q]
            data.append(temp_data)

        except:
            print('Ошибочка')
    delete_middle_block(file_n)

file_name = "BASE_RSP_1_23_12.TDB"
data = [['Code', 'Master', 'Welder', 'Expert', 'Param', 'Name', 'DateTime',
             'V', 'S', 'T', 'U1', 'U2', 'I', 'P', 'L',
             'LI', 'ZKZ', 'VF', 'VL', 'Scol', 'FKZ', 'TU', 'Q']]
while os.path.getsize(file_name) > 13766:
    parse_tdb(file_name)
with open('output.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data:
        csvwriter.writerow(row)
