# 📖 FlexKBQA 

This repository is the official implementation of FlexKBQA.

[FlexKBQA: A Flexible LLM-Powered Framework for Few-Shot Knowledge Base Question Answering](https://arxiv.org/abs/2308.12060)

## 🛠️ Framework
![image](https://github.com/leezythu/FlexKBQA/blob/main/figs/framework.png)

## 🎮 Usage

### Automatic Program Sampling
```bash
cd flexkbqa/automatic_program_sampling
python step_wise_grounding.py
python post_process_grounding_1.py
python post_process_grounding_2.py
python parse_sparql.py / python parse_sparql_grail.py
```
### Low-Resource Program Translation
```bash
cd run_scripts
sh run.sh/ sh run_turbo.sh
```

### Execution-Guided Self-Training
```bash
cd flexkbqa/execution-guided self-training
```
### Inherent Reasoning
```bash
cd flexkbqa/inherent reasoning
```

### Under Construction...

## 🖌️  Citation
If you find our repo useful, please kindly consider citing:
```bibtex
@misc{li2023flexkbqa,
      title={FlexKBQA: A Flexible LLM-Powered Framework for Few-Shot Knowledge Base Question Answering}, 
      author={Zhenyu Li and Sunqi Fan and Yu Gu and Xiuxing Li and Zhichao Duan and Bowen Dong and Ning Liu and Jianyong Wang},
      year={2023},
      eprint={2308.12060},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
