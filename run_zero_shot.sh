export PYTHONPATH=.
python ./scripts/annotate_kb_program_turbo_grail.py --dataset grail \
--dataset_split llm_results_turbo_grail_few_shot/final_grailqa_train_data_w_ent_name \
--save_dir llm_results_turbo_grail_zero_shot \
--prompt_file manual_prompts_zero_shot.txt \
--output_file final_grailqa_train_data_zero_shot \
--n_parallel_prompts 1 \
--max_generation_tokens 512 \
--temperature 0.4 \
--sampling_n 1 \
--n_processes 1 \
--n_shots 0 \
-v