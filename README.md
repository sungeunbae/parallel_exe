# Preparation
## Background
Suppose you want to execute the following 10 jobs. They are all `OpenSees` with different input parameters and input files. 

```
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p001403/CACS/2012p001403_000_PGA0.010_sf1.00_16008_0.005_vel.txt 2012p001403_000_PGA0.010_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p001403/CACS/2012p001403_090_PGA0.016_sf1.00_16008_0.005_vel.txt 2012p001403_090_PGA0.016_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p003376/CACS/2012p003376_000_PGA0.007_sf1.00_14447_0.005_vel.txt 2012p003376_000_PGA0.007_sf1.00 14447 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p003376/CACS/2012p003376_090_PGA0.010_sf1.00_14447_0.005_vel.txt 2012p003376_090_PGA0.010_sf1.00 14447 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p010301/CACS/2012p010301_000_PGA0.009_sf1.00_12637_0.005_vel.txt 2012p010301_000_PGA0.009_sf1.00 12637 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p010301/CACS/2012p010301_090_PGA0.010_sf1.00_12637_0.005_vel.txt 2012p010301_090_PGA0.010_sf1.00 12637 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014309/CACS/2012p014309_000_PGA0.005_sf1.00_11409_0.005_vel.txt 2012p014309_000_PGA0.005_sf1.00 11409 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014309/CACS/2012p014309_090_PGA0.006_sf1.00_11409_0.005_vel.txt 2012p014309_090_PGA0.006_sf1.00 11409 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014905/CACS/2012p014905_000_PGA0.009_sf1.00_16008_0.005_vel.txt 2012p014905_000_PGA0.009_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014905/CACS/2012p014905_090_PGA0.011_sf1.00_16008_0.005_vel.txt 2012p014905_090_PGA0.011_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 
```

You can certainly run these one by one, but it can be cumbersome. Imagine you have thousands of them. It can be slow too.
If you have an access to an HPC and can utilize many CPU cores, you can run these jobs simultaneously.


## Make a job list file

Make a file that contains this list of commands to run. Each line should be a valid command that can run. Let's call this `sample_jobfile`.



# Edit slurm script

Edit `parallel_exe_mahuika.sl` or `parallel_exe_maui.sl` and replace the job file name if needed.
```
time python parallel_exe.py `pwd`/sample_jobfile
```
By default, the slurm script is configured to utilize 40 CPU cores (Mahuika) and 36 cores (Maui). You can probably leave this as it as (unless your jobfile contains small number of jobs)
Default wall time is 1 hour, which can be short. Adjust this as needed, but the maximum wall time is 24 hours (Maui) and 72 hours (Mahuika, large partition). See https://wiki.canterbury.ac.nz/display/QuakeCore/HPC+Comparison+chart

```
#SBATCH --time=01:00:00              # Walltime (HH:MM:SS)
```
If the maximum wall time is too short to complete all the jobs, see below and follow the instruction for "Resuming"




# Submit the slurm script

Load modules. Certain modules are machine specific. For example, if you wish to run OpenSees

```
module add OpenSees ----> Mahuika

module add OpenSees/3.2.0-CrayGNU-18.08  ----> Maui
```

Depending on where you wish to run,

```
sbatch --export=ALL parallel_exe_mahuika.sl  ----> Mahuika
sbatch --export=ALL parallel_exe_maui.sl ----> Maui
```


# Resuming

If you rerun the script `parallel_exe.py` (by submitting a slurm job), it is designed to automatically resume from the checkpoint.
The checkpoint directory contains files such as `00000.done`, `00001.done`, meaning the jobs of id 0 and 1 have been already completed. (TODO: It doesn't check if the run was successful or not)

The job ids are automatically assigned when it is first executed, and the job id and job association is stored as `sample_jobfile.json`

```
{
    "0": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p001403/CACS/2012p001403_000_PGA0.010_sf1.00_16008_0.005_vel.txt 2012p001403_000_PGA0.010_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test,
    "1": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p001403/CACS/2012p001403_090_PGA0.016_sf1.00_16008_0.005_vel.txt 2012p001403_090_PGA0.016_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test,
    "2": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p003376/CACS/2012p003376_000_PGA0.007_sf1.00_14447_0.005_vel.txt 2012p003376_000_PGA0.007_sf1.00 14447 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test,
    "3": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p003376/CACS/2012p003376_090_PGA0.010_sf1.00_14447_0.005_vel.txt 2012p003376_090_PGA0.010_sf1.00 14447 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test,
    "4": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p010301/CACS/2012p010301_000_PGA0.009_sf1.00_12637_0.005_vel.txt 2012p010301_000_PGA0.009_sf1.00 12637 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test,
    "5": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p010301/CACS/2012p010301_090_PGA0.010_sf1.00_12637_0.005_vel.txt 2012p010301_090_PGA0.010_sf1.00 12637 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test,
    "6": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014309/CACS/2012p014309_000_PGA0.005_sf1.00_11409_0.005_vel.txt 2012p014309_000_PGA0.005_sf1.00 11409 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test,
    "7": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014309/CACS/2012p014309_090_PGA0.006_sf1.00_11409_0.005_vel.txt 2012p014309_090_PGA0.006_sf1.00 11409 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test,
    "8": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014905/CACS/2012p014905_000_PGA0.009_sf1.00_16008_0.005_vel.txt 2012p014905_000_PGA0.009_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test,
    "9": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014905/CACS/2012p014905_090_PGA0.011_sf1.00_16008_0.005_vel.txt 2012p014905_090_PGA0.011_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test
}
```

The presence of `00000.done`, `00001.done` means the job 0 and 1 have been already completed during the previous run. This run will be skipping these, and continue to process remaining jobs

If you have a need to avoid "resuming", use `--no-resume` option for `parallel_exe.py` to start from scratch.




### Old way

Instead of using `parallel_exe.py`, you can run commands in `sample_jobfile` directly. The SLURM script below is designed to run each line from sample__jobfile, and run them in parallel utilizing 36 cores of 1 node (of Mahuika). 

The first `while` block parses the job file, put them into `commands` array. Each `cmnd` from this array gets executed, it runs in the background (`&` after the command), making the iterations in the for loop asynchronous. Also notice the `wait` after the for loop. The beauty of this solution is that when a CPU core finishes one job, it comes back to the for loop and takes a new job. This, however, has no "checkpointing" feature unlike `parallel_exe.py`.


```
#!/bin/bash
...
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=36
#SBATCH --cpus-per-task=1
...

count=0
while IFS='' read -r line || [[ -n "$line" ]]; do
#    echo "Text read from file: $line"
    if [[ ${line:0:1} == '#' ]]
    then
        echo "comment:$line"
    else
        commands[count]=${line}
        count=$(( $count + 1 ))
    fi
#    echo ${commands[count]}
done < sample_jobfile

for cmnd in "${commands[@]}"
do
#    echo $cmnd
    srun -n1 --exclusive $cmnd &
done
wait
```
