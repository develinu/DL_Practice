import os
import glob
import datetime
import pandas as pd

if __name__ == '__main__':
    """
    ASOS 데이터셋 정보
    파일명 : SURFACE_ASOS_[지점번호]_HR_[관측년도]_[관측년도]_[관측년도+1].csv
    컬럼 : 지점(0), 일시(1), 기온(2), 강수량(3), 풍속(4), 
           풍향(5), 습도(6), 증기압(7), 이슬점온도(8), 현지기압(9), 
           해면기압(10), 일조(11), 일사(12), 적설(13), 3시간신적설(14),
           전운량(15), 증하층운량(16), 운형(17), 최저운고(18), 시정(19), 
           지면상태(20), 현상번호(21), 지면온도(22), 5cm 지중온도(23), 10cm 지중온도(24), 
           30cm 지중온도(25)
    컬럼 인덱스 : 0
    총 컬럼 수 : 26
    """
    dataset_src = os.path.join('C:\\', 'DATASET', 'ATMOSPHERE', 'OBSERVATION_RAW', 'ASOS')
    start_date = datetime.datetime(year=2014, month=1, day=1, hour=0, minute=0)
    end_date = datetime.datetime(year=2018, month=12, day=31, hour=23, minute=0)
    file_name_format = "SURFACE_ASOS_%s_HR_%s_%s_%s.csv"
    asos_variable_map = {0: 'station_num', 1: 'observation_time', 2: 'temperature', 3: 'precipitation',
                         4: 'wind_speed', 5: 'wind_direction', 6: 'humidity', 7: 'vapor_pressure',
                         8: 'dew_point_temperature', 9: 'local_pressure', 10: 'sea_surface_pressure',
                         11: 'sunshine', 12: 'solar_radiation', 13: 'snowfall', 14: 'snowfall_3hr',
                         15: 'total_cloud_amount', 16: 'low_middle_cloud_amount', 17: 'cloud_shape',
                         18: 'min_cloud_height', 19: 'visibility', 20: 'ground_condition',
                         21: 'current_number', 22: 'ground_temperature', 23: 'soil_temperature',
                         24: 'soil_temperature_5cm', 25: 'soil_temperature_10cm', 26: 'soil_temperature_30cm'}
    select_variables = [asos_variable_map[select_num] for select_num in [0, 1, 2, 3]]
    for year in range(start_date.year, end_date.year + 1):
        file_list = glob.glob(os.path.join(dataset_src, str(year), '*.csv'))
        for file_name in file_list:
            df = pd.read_csv(file_name, skiprows=1, header=None, encoding='cp949')
            print(df.columns)
            df.columns = [col_name for col_name in asos_variable_map.values()]
            print(df.columns)
            df = df[select_variables]
            df = df.set_index(pd.to_datetime(df[asos_variable_map[1]]))
            print(df)
            break
        break
    print()

