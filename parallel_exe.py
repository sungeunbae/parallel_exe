from argparse import ArgumentParser
import json
from multiprocessing.pool import Pool
from pathlib import Path
import shutil

from qcore.shared import exe
from qcore.config import qconfig
#from qcore.progress_tracker import ProgressTracker

global checkpoint_dir, outdir

def pretty_print(txt,length=80,fill_char="*"):
    left_margin = int((length -len(txt))/2)-1
    right_margin = length - len(txt) - 2- left_margin
    print(fill_char*left_margin+f" {txt} "+fill_char*right_margin+"\n")
    

def load_args():
    parser = ArgumentParser()

    parser.add_argument("job_file", help="List of jobs. Each line should be an executable command")
    parser.add_argument("-n","--np", help="Number of parallel processe to use", type=int, default=qconfig['cores_per_node'])
    parser.add_argument("--no-resume", help="Don't resume, start from scratch.",action="store_false", dest="resume_ok")
    parser.add_argument("--outdir", help="Path to store output files",default=Path.cwd()/"out")
    parser.add_argument("--checkpoint_dir",help="Path to store checkpoint info",default=Path.cwd()/"checkpoint")
    args = parser.parse_args()
    return args


def run_single(cmd,jobid):
    out,err=exe(f"{cmd}",debug=False)
    Path(checkpoint_dir/f"{jobid:05d}.done").touch()
    with open(outdir/f"{jobid:05d}.out","w") as f:
        f.write(out)
    with open(outdir/f"{jobid:05d}.err","w") as f:
        f.write(err)



def run_all(job_list, np):
                
    with Pool(np) as p:
        p.starmap(run_single, job_list)
        

if __name__ == "__main__":

    args = load_args()

    checkpoint_dir = args.checkpoint_dir
    outdir = args.outdir

    job_file =  Path(args.job_file)
    job_dict = job_file.with_suffix(".json")

    checkpoint_dir.mkdir(exist_ok=True)
    outdir.mkdir(exist_ok=True)

    pretty_print(f"Executing jobs in {job_file.name}")

    with open(job_file,"r") as f:
        job_lines = f.read().splitlines()

    # assigning index 1,2,3.. to each command
    job_lines_dict=dict(zip(range(len(job_lines)),job_lines))
    with open(job_dict,"w") as f:
        json.dump(job_lines_dict,f,indent=4, sort_keys=True) # keep the json file for reference


    all_jobs = [int(x) for x in job_lines_dict.keys()]
    completed_jobs=[]

    if args.resume_ok:
        # check remaining jobs
        completed_jobs=[int(x.stem) for x in list(checkpoint_dir.glob("*.done"))]
        pretty_print("Resuming from the checkpoint")
        pretty_print("Already completed jobs")
        completed_jobs.sort()
        print(completed_jobs)
    else:
        shutil.rmtree(checkpoint_dir)
        checkpoint_dir.mkdir() # re-create the directory
        pretty_print("Running all jobs from scratch")

    remaining_jobs = list(set(all_jobs)-set(completed_jobs))
    pretty_print("Jobs to run")
    print(remaining_jobs)
    
    jobs_to_execute = [(job_lines_dict[idx],idx) for idx in remaining_jobs]
    run_all(jobs_to_execute,args.np)

    pretty_print("All jobs completed")





