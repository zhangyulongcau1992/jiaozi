import warnings
import datetime
import traceback

import pandas as pd

from process.main_process import main_process, main_process2

warnings.filterwarnings('ignore')
# 需要研究的营养成分
SELECT_NUTRITION = ["能量(千卡）", "蛋白质（克）", "脂肪（克）", "碳水化物（克）", "维生素A（μg）", "维生素B1（毫克）",
                    "维生素B2（毫克）", "维生素C（毫克）", "维生素E（毫克）", "钙（毫克）", "磷（毫克）", "钾（毫克）",
                    "钠（毫克）", "镁（毫克）", "铁（毫克）", "锌（毫克）", "硒（μg）", "铜（毫克）", "锰（毫克）"]
# 个人信息
personal_info = {"人群": "成人", "年龄": 31, "性别": "男", "活动水平": "轻", "体重": 70, "meal": "午饭"}
# 定义饺子个数
num_of_dumpling_list = [18, 19, 20, 21, 22]
# num_of_dumpling_list = [20]
# 定义肉馅占比肉馅+蔬菜
meat_percent_list = [0.2, 0.4, 0.6, 0.8]
# meat_percent_list = [0.4]
dumpling_skin_percent_list = [0.48, 0.5, 0.52]
final_result = pd.DataFrame(columns=SELECT_NUTRITION)
for num_of_dumpling in num_of_dumpling_list:
    for meat_percent in meat_percent_list:
        for dumpling_skin_percent in dumpling_skin_percent_list:
            try:
                # 输入文件路径
                output_file_path = 'output_file/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '/'
                best_nutrition_list = main_process2(personal_info, num_of_dumpling, meat_percent, output_file_path,
                                                    dumpling_skin_percent)
                final_result = pd.concat(final_result, best_nutrition_list)
            except Exception as e:
                print(e)
                print(traceback.format_exc())
final_result.to_csv('output_file/final_result.csv')
