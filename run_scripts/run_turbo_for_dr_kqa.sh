export PYTHONPATH=.
python ./scripts/annotate_kb_program_turbo_kqa.py --dataset kqa \
--dataset_split Direct_Reasoning/test \
--save_dir dr_results_50_shot \
--prompt_file Direct_Reasoning/dr_prompt_for_kqa.txt \
--output_file kqa_test_all \
--n_parallel_prompts 1 \
--max_generation_tokens 512 \
--temperature 0.4 \
--sampling_n 1 \
--n_processes 1 \
--n_shots 0 \
-v