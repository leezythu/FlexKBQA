python ./scripts/annotate_kb_program_turbo_grail.py --dataset grail \
--dataset_split GrailQA_v1.0/grailqa_v1.0_train \
--save_dir llm_results_turbo_grail \
--prompt_file manual_prompts_grail.txt \
--output_file grail_train \
--n_parallel_prompts 1 \
--max_generation_tokens 512 \
--temperature 0.4 \
--sampling_n 1 \
--n_processes 1 \
--n_shots 0 \
-v