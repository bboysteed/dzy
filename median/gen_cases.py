#!/home/steed/Desktop/session_work/case_generate/introClass_cases/venv/bin/python3
import sys

import matplotlib.pyplot as plt
from sko.GA import GA_TSP

sys.path.append(r"/home/steed/Desktop/session_work/case_generate/introClass_cases")
from getcovrate import *
from utils.pycui import *


cui = pycui()
num_points = 3
cases_file = open("./tmpFile/cases", "w+")
make_bench_file_clean()
make_bench_file()

"""
    @一个序列长度为20,一共4个用例，每次输入4个用例后记录一次累计覆盖情况
"""


def get_conv_rate(serial):
    # cui.info("A serial is : {}".format(serial))
    for j in range(0, len(serial), 3):
        tem_ipf = open("./tmpFile/data.in", "w+")
        a_case = list(serial[j:j + 3])
        bench_input_data = " ".join([str(ii) for ii in a_case]) + "\n"
        cui.info("a case is: {}".format(bench_input_data.rstrip()))
        cases_file.write(bench_input_data)
        tem_ipf.write(bench_input_data)
        tem_ipf.seek(0)
        # cui.success("a case has been added to data sets...")
        # cui.info("data:{}".format(tem_ipf.readline()))
        # tem_ipf.seek(0)
        run_bench_file(inp_b_data=tem_ipf)  # 运行程序
        tem_ipf.close()
    gcovr_save_xml()
    covr_rate = parse_xml_and_get_rate()

    return covr_rate

def gen_loop():
    ga_tsp = GA_TSP(func=get_conv_rate, n_dim=num_points, size_pop=4, max_iter=10, prob_mut=1,case_type=module_name)
    best_case, best_covrate = ga_tsp.run()
    cui.success("best_points:{}\nbest_distance:{}\n".format(best_case, best_covrate))
    cases_file.close()


if __name__ == '__main__':
    gen_loop()