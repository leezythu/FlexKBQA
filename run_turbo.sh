python3.8 ./scripts/annotate_kb_program_turbo.py --dataset wikitq \
--dataset_split results/s-expr/1_valid_expansions \
--save_dir llm_results_turbo \
--prompt_file manual_prompts.txt \
--output_file 1_valid_expansions_0416 \
--n_parallel_prompts 1 \
--max_generation_tokens 512 \
--temperature 0.4 \
--sampling_n 1 \
--n_processes 1 \
--n_shots 0 \
-v