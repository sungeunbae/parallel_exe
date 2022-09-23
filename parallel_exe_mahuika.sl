#!/bin/bash -e
#SBATCH --job-name=parallel_exe      # job name (shows up in the queue)
#SBATCH --account=nesi00213          # Project Account
#SBATCH --partition=large            # specify a partition
#SBATCH --time=12:00:00              # Walltime (HH:MM:SS)
#SBATCH --output %x.%j.out 
#SBATCH --error %x.%j.err
#SBATCH --ntasks=36                   # specify number of cores or tasks to run analysis
#SBATCH --nodes=1                    # specificy number of nodes
#SBATCH --mem-per-cpu=1000
#SBATCH --hint=nomultithread

time python parallel_exe.py `pwd`/sample_job

