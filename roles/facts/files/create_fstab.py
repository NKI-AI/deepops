import json
from pathlib import Path

project_folder_names = Path("/sw/software/kosmos-cluster/project_folders.lst").read_text().split("\n")
project_folder_names = [f.strip() for f in project_folder_names if f != "" and f[0] != "#"]

home_folder_names = Path("/sw/software/kosmos-cluster/home_folders.lst").read_text().split("\n")
home_folder_names = [f.strip() for f in home_folder_names if f != "" and f[0] != "#"]


# Fixed lines:
fstab_lines = ""
fstab_lines += f"kronos:/data-pool/software /sw nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"
fstab_lines += f"kronos:/data-pool/groups/aiforoncology /data/groups/aiforoncology nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"
fstab_lines += f"kronos:/data-pool/groups/beets-tan /data/groups/beets-tan nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"
mountable_folders = ["/sw", "/data/groups/aiforoncology", "/data/groups/beets-tan"]


# Create the fstab lines for the project folders:
for folder in project_folder_names:
    fstab_lines += f"rhea:/project-pool/projects/{folder} /projects/{folder} nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"

# Create the fstab lines for the home folders
for folder in home_folder_names:
    fstab_lines += f"rhea:/project-pool/network_homes/{folder} /home/{folder} nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"


# Create the list of project folders:
for folder in project_folder_names:
    mountable_folders.append(f"/projects/{folder}")


# This is to create new home directories
for folder in home_folder_names:
    mountable_folders.append(f"/home/{folder}")


# Get a list of project folders that have disappeared
# We can use these to remove
# NOTE: Do not remove the home folders!
to_remove = []
for line in Path("/projects").glob("*"):
    if line.name not in [Path(_).name for _ in mountable_folders]:
        to_remove.append(line.name)


output = {"fstab": fstab_lines, "folders": mountable_folders, "removed": to_remove}
print(json.dumps(output, indent=2))
