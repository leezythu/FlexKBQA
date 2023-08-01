export PYTHONPATH=.
python ./scripts/annotate_kb_program_turbo_grail.py --dataset grail \
--dataset_split Direct_Reasoning/grail_test_with_no_answer \
--save_dir dr_results_50_shot \
--prompt_file Direct_Reasoning/dr_prompt_for_grail.txt \
--output_file dr_res_grail_test \
--n_parallel_prompts 1 \
--max_generation_tokens 512 \
--temperature 0.4 \
--sampling_n 1 \
--n_processes 1 \
--n_shots 0 \
-v