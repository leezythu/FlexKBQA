export PYTHONPATH=.
python ./scripts/annotate_kb_program_turbo_kqa_16k.py --dataset kqa \
--dataset_split Direct_Reasoning/test \
--save_dir llmicl_results_100_shot \
--prompt_file Direct_Reasoning/icl_prompts_100.txt \
--output_file kqa_test_all \
--n_parallel_prompts 1 \
--max_generation_tokens 512 \
--temperature 0.4 \
--sampling_n 1 \
--n_processes 1 \
--n_shots 0 \
-v