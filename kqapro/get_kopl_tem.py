from fnmatch import translate
import json,os
from tqdm import tqdm
from graphq_trans.kopl.translator import Translator as KoplTranslator
from graphq_trans.ir.translator import Translator as IRTranslator

def get_program_seq(program):
    arg2id = {}
    seq = []
    arg_cnt = 0
    for item in program:
        func = item['function']
        inputs = item['inputs']
        args = ''
        for i in range(len(inputs)):
            # args += ' <arg> ' + input
            if inputs[i] in ["=","<",">"]:
                continue
            if inputs[i] not in arg2id:
                args += ' <arg> ' + "arg"+str(arg_cnt)
                arg2id["_".join(inputs[i].split())] = "arg"+str(arg_cnt)
                arg2id[inputs[i]] = "arg"+str(arg_cnt)
                arg_cnt += 1
            else:
                args += ' <arg> ' + arg2id[inputs[i]]
            inputs[i] = arg2id[inputs[i]]
        seq.append(func + args)
    seq = ' <func> '.join(seq)
    return seq, arg2id

train_set = json.load(open(os.path.join("./dataset", 'train.json')))
programs = []
ori_programs = []
for item in tqdm(train_set):
    question = item['question']
    ori_program = item['program']
    program, arg2id = get_program_seq(ori_program)
    if program not in programs:
        programs.append(program)
        ori_programs.append({"program":ori_program,"arg2id":arg2id})

with open("kopl_templates.json",'w') as f:
    f.write(json.dumps(ori_programs))

def post_process(sparql,args2id):
    sparql = sparql.split()
    vars = list(set(args2id.values()))
    for i in range(len(sparql)):
        if sparql[i].startswith("\"arg"):
            sparql[i] = "?"+sparql[i].strip("\"")
        if sparql[i].startswith("<arg"):
            sparql[i] = "?"+sparql[i].strip("<").strip(">")
        if sparql[i].endswith("^^xsd:double"): 
            if sparql[i-1] in [">","<","="]:
                sparql[i] = "\"100\"^^xsd:double"
            else:
                sparql[i] = sparql[i].strip("\"^^xsd:double")
        if sparql[i].endswith("^^xsd:date"):
            if sparql[i-1] in [">","<","="]:
                sparql[i] = "\"2000-01-01\"^^xsd:date"
            else:
                sparql[i] = sparql[i].strip("\"^^xsd:date")
        if sparql[i].endswith("^^xsd:year"):
            if sparql[i-1] in [">","<","="]:
                sparql[i] = "2000"
            else:
                sparql[i] = sparql[i].strip("\"^^xsd:year")
    sparql = " ".join(sparql)
    insert_str = ""
    for var in vars:
        insert_str +=" ?"+str(var)
    parse_type = None
    if sparql.startswith('SELECT DISTINCT'):
        tem_executed = sparql.replace("SELECT DISTINCT","SELECT DISTINCT"+insert_str)
    elif sparql.startswith('SELECT (COUNT(DISTINCT ?e)') or sparql.startswith('SELECT ?e'):
        tem_executed = sparql.replace("SELECT","SELECT"+insert_str)
    elif sparql.startswith('ASK'):
        tem_executed = sparql.replace("ASK","SELECT"+insert_str)
        parse_type = 'bool'
    return tem_executed,parse_type,vars

translator = KoplTranslator()
ir_translator = IRTranslator()
sparql_tems = []
for ori_program in ori_programs:
    ir = translator.to_ir(ori_program["program"])
    ori_sparql = ir_translator.to_sparql(ir)
    if ori_sparql!="":
        # for key in ori_program["arg2id"]:
        #     sparql = sparql.replace(key,ori_program["arg2id"][key])
        tem_executed, parse_type, vars = post_process(ori_sparql,ori_program["arg2id"])
        sparql_tems.append({"tem":ori_sparql,"tem_executed":tem_executed,"parse_type":parse_type,"vars":vars})

with open("sparql_templates.json",'w') as f:
    f.write(json.dumps(sparql_tems))