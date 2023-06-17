python ./scripts/annotate_kb_program_turbo_kqa.py --dataset kqa \
--dataset_split kqapro/syn_kqa_from_ent_sparql \
--save_dir llm_results_turbo_kqa_from_ent \
--prompt_file manual_prompts_kqa.txt \
--output_file llm_kqa \
--n_parallel_prompts 1 \
--max_generation_tokens 512 \
--temperature 0.4 \
--sampling_n 1 \
--n_processes 1 \
--n_shots 0 \
-v