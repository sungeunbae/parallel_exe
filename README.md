# Preparation

## Make a job list file

Suppose you want to execute the following 10 jobs. Make a file that contains this list.Each line should be a valid command that can run. Let's call this `sample_jobfile`.

```
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p001403/CACS/2012p001403_000_PGA0.010_sf1.00_16008_0.005_vel.txt 2012p001403_000_PGA0.010_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p001403_000_PGA0.010_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p001403_000_PGA0.010_sf1.00_stderror.out
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p001403/CACS/2012p001403_090_PGA0.016_sf1.00_16008_0.005_vel.txt 2012p001403_090_PGA0.016_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p001403_090_PGA0.016_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p001403_090_PGA0.016_sf1.00_stderror.out
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p003376/CACS/2012p003376_000_PGA0.007_sf1.00_14447_0.005_vel.txt 2012p003376_000_PGA0.007_sf1.00 14447 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p003376_000_PGA0.007_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p003376_000_PGA0.007_sf1.00_stderror.out
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p003376/CACS/2012p003376_090_PGA0.010_sf1.00_14447_0.005_vel.txt 2012p003376_090_PGA0.010_sf1.00 14447 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p003376_090_PGA0.010_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p003376_090_PGA0.010_sf1.00_stderror.out
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p010301/CACS/2012p010301_000_PGA0.009_sf1.00_12637_0.005_vel.txt 2012p010301_000_PGA0.009_sf1.00 12637 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p010301_000_PGA0.009_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p010301_000_PGA0.009_sf1.00_stderror.out
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p010301/CACS/2012p010301_090_PGA0.010_sf1.00_12637_0.005_vel.txt 2012p010301_090_PGA0.010_sf1.00 12637 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p010301_090_PGA0.010_sf1.00_stderror.out
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014309/CACS/2012p014309_000_PGA0.005_sf1.00_11409_0.005_vel.txt 2012p014309_000_PGA0.005_sf1.00 11409 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014309_000_PGA0.005_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014309_000_PGA0.005_sf1.00_stderror.out
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014309/CACS/2012p014309_090_PGA0.006_sf1.00_11409_0.005_vel.txt 2012p014309_090_PGA0.006_sf1.00 11409 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014309_090_PGA0.006_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014309_090_PGA0.006_sf1.00_stderror.out
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014905/CACS/2012p014905_000_PGA0.009_sf1.00_16008_0.005_vel.txt 2012p014905_000_PGA0.009_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014905_000_PGA0.009_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014905_000_PGA0.009_sf1.00_stderror.out
OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014905/CACS/2012p014905_090_PGA0.011_sf1.00_16008_0.005_vel.txt 2012p014905_090_PGA0.011_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014905_090_PGA0.011_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014905_090_PGA0.011_sf1.00_stderror.out

# Edit slurm script

Edit `parallel_exe_mahuika.sl` or `parallel_exe_maui.sl` and replace the job file name if needed.
```
time python parallel_exe.py `pwd`/sample_jobfile

By default, the slurm script is configured to utilize 40 CPU cores (Mahuika) and 36 cores (Maui). You can probably leave this as it as (unless your jobfile contains small number of jobs)
Default wall time is 1 hour, which can be short. Adjust this as needed, but the maximum wall time is 24 hours.

```
#SBATCH --time=01:00:00              # Walltime (HH:MM:SS)
```
If the maximum 24 hours is too short to complete all the jobs, see below and follow the instruction for "Resuming"




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
The checkpoint directory contains files such as `00000.done`, `00001.done`, meaning the jobs of id 0 and 1 have been already produced.

The job ids are automatically assigned when it is first executed, and the job id and job association is stored as `sample_jobfile.json`

```
{
    "0": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p001403/CACS/2012p001403_000_PGA0.010_sf1.00_16008_0.005_vel.txt 2012p001403_000_PGA0.010_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p001403_000_PGA0.010_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p001403_000_PGA0.010_sf1.00_stderror.out",
    "1": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p001403/CACS/2012p001403_090_PGA0.016_sf1.00_16008_0.005_vel.txt 2012p001403_090_PGA0.016_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p001403_090_PGA0.016_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p001403_090_PGA0.016_sf1.00_stderror.out",
    "2": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p003376/CACS/2012p003376_000_PGA0.007_sf1.00_14447_0.005_vel.txt 2012p003376_000_PGA0.007_sf1.00 14447 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p003376_000_PGA0.007_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p003376_000_PGA0.007_sf1.00_stderror.out",
    "3": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p003376/CACS/2012p003376_090_PGA0.010_sf1.00_14447_0.005_vel.txt 2012p003376_090_PGA0.010_sf1.00 14447 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p003376_090_PGA0.010_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p003376_090_PGA0.010_sf1.00_stderror.out",
    "4": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p010301/CACS/2012p010301_000_PGA0.009_sf1.00_12637_0.005_vel.txt 2012p010301_000_PGA0.009_sf1.00 12637 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p010301_000_PGA0.009_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p010301_000_PGA0.009_sf1.00_stderror.out",
    "5": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p010301/CACS/2012p010301_090_PGA0.010_sf1.00_12637_0.005_vel.txt 2012p010301_090_PGA0.010_sf1.00 12637 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p010301_090_PGA0.010_sf1.00_stderror.out",
    "6": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014309/CACS/2012p014309_000_PGA0.005_sf1.00_11409_0.005_vel.txt 2012p014309_000_PGA0.005_sf1.00 11409 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014309_000_PGA0.005_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014309_000_PGA0.005_sf1.00_stderror.out",
    "7": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014309/CACS/2012p014309_090_PGA0.006_sf1.00_11409_0.005_vel.txt 2012p014309_090_PGA0.006_sf1.00 11409 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014309_090_PGA0.006_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014309_090_PGA0.006_sf1.00_stderror.out",
    "8": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014905/CACS/2012p014905_000_PGA0.009_sf1.00_16008_0.005_vel.txt 2012p014905_000_PGA0.009_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014905_000_PGA0.009_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014905_000_PGA0.009_sf1.00_stderror.out",
    "9": "OpenSees /home/fkw21/2022_QuakeCoRE_AM_Poster/Analysis/OpenSeesModels/CACS/CACS_TotalStress_LR0.0_600.tcl CACS TotalStress_LR0.0_600  /nesi/nobackup/nesi00213/RunFolder/Validation/2022_QuakeCoRE_AM_Poster_FKuncar/inputMotions/v6_2022-08-19/2012p014905/CACS/2012p014905_090_PGA0.011_sf1.00_16008_0.005_vel.txt 2012p014905_090_PGA0.011_sf1.00 16008 0.005 /nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test >/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014905_090_PGA0.011_sf1.00_output.out 2>/nesi/nobackup/nesi00213/RunFolder/baes/parallel_exe_test/CACS_TotalStress_LR0.0_600_2012p014905_090_PGA0.011_sf1.00_stderror.out"
}
```

The presence of `00000.done`, `00001.done` means the job 0 and 1 have been already completed during the previous run. This run will be skipping these, and continue to process remaining jobs

If you have a need to avoid "resuming", use `--no-resume` option for `parallel_exe.py` to start from scratch.




