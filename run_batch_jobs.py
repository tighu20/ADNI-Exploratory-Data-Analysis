import subprocess
for job_count in range(1,123):
    slurm_command="sbatch -p RM -N 1 --ntasks-per-node=28 -A ac5616p -t 48:00:00 /pghbio/dbmi/batmanlab/tighu/downloads/freesurfer/Job_files/fs_{}.job".format(job_count)
    subprocess.Popen(slurm_command.split(" "))
