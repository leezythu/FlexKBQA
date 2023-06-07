"""
 Copyright (c) 2021, salesforce.com, inc.
 All rights reserved.
 SPDX-License-Identifier: BSD-3-Clause
 For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
"""

import pickle
import json
import os
import random
from re import L
import shutil
from collections import Counter
from framework.components.utils import *

def convert_parse_instance(data,sexpr_tem):
    vars = data["vars"]
    sexpr = sexpr_tem
    sexpr_w_ent_name = sexpr_tem
    for var in vars:
        if not var.startswith("?"):
            full_var = "?"+var
        else:
            full_var = var
        assert full_var in sexpr_tem
        if "ns:" in vars[var]["id"]:
            sexpr = sexpr.replace(full_var,data["vars"][var]["id"].split("ns:")[1])
            if vars[var]["id"].startswith("ns:m."):
                sexpr_w_ent_name = sexpr_w_ent_name.replace(full_var,data["vars"][var]["name"])
            else:
                sexpr_w_ent_name = sexpr_w_ent_name.replace(full_var,data["vars"][var]["id"].split("ns:")[1])
        elif "ns:" in vars[var]["name"]:
            sexpr = sexpr.replace(full_var,data["vars"][var]["name"].split("ns:")[1])
            sexpr_w_ent_name = sexpr_w_ent_name.replace(full_var,data["vars"][var]["name"].split("ns:")[1])
        else:
            print("?????")
            assert False
    data["sexpr"] = sexpr
    data["sexpr_w_ent_name"] = sexpr_w_ent_name
    return data

def augment_with_s_expr(in_dir,out_dir,i,data):
    split = os.path.join(in_dir,str(i)+"_valid_expansions.json")
    sexpr_tem = data[i]["s_expression"]
    dataset = json.load(open(split))
    final_dataset = []
    for data in dataset:
        instance = convert_parse_instance(data,sexpr_tem)
        final_dataset.append(instance)
    with open(os.path.join(out_dir,str(i)+"_valid_expansions.json"),'w')as f:
        f.write(json.dumps(final_dataset))

if __name__ == '__main__':
    # in_dir = "results_webqsp/sparql"
    # out_dir = "results_webqsp/s-expr"
    in_dir = "results_grail/sparql"
    out_dir = "results_grail/s-expr"
    data = json.load(open("sparql_for_prompts_grail.json"))
    for i in range(0,6):
        augment_with_s_expr(in_dir,out_dir,i,data)