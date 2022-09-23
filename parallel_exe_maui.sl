#!/bin/bash -e
#SBATCH --job-name=parallel_exe      # job name (shows up in the queue)
#SBATCH --account=nesi00213          # Project Account
#SBATCH --partition=nesi_research
#SBATCH --time=01:00:00              # Walltime (HH:MM:SS)
#SBATCH --output %x.%j.out 
#SBATCH --error %x.%j.err
##SBATCH --cpus-per-task=40           # number of cores per task (e.g. OpenMP)
#SBATCH --ntasks=40                   # specify number of cores or tasks to run analysis
#SBATCH --nodes=1                    # specificy number of nodes
#SBATCH --mem-per-cpu=1000
#SBATCH --hint=nomultithread

time python parallel_exe.py `pwd`/sample_job


