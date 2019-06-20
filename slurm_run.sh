#!/bin/bash
#SBATCH --job-name=parallel
#SBATCH --partition=all
#SBATCH --gres=gpu:0
#SBATCH --cpus-per-task=56
module purge
module load parallel
parallel < "$1"
