import json
from pathlib import Path

project_folder_names = Path("/mnt/sw/software/kosmos-cluster/project_folders.lst").read_text().split("\n")
project_folder_names = [f.strip() for f in project_folder_names if f != "" and f[0] != "#"]

home_folder_names = Path("/mnt/sw/software/kosmos-cluster/home_folders.lst").read_text().split("\n")
home_folder_names = [f.strip() for f in home_folder_names if f != "" and f[0] != "#"]


# Fixed lines:
fstab_lines = ""
fstab_lines += f"kronos:/data-pool/groups/aiforoncology /data/groups/aiforoncology nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"
fstab_lines += f"kronos:/data-pool/groups/beets-tan /data/groups/beets-tan nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"
project_folders = ["/data/groups/aiforoncology", "/data/groups/beets-tan"]


# Create the fstab lines for the project folders:
for folder in project_folder_names:
    fstab_lines += f"rhea:/project-pool/projects/{folder} /projects/{folder} nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"

# Create the fstab lines for the home folders
for folder in home_folder_names:
    fstab_lines += f"rhea:/project-pool/network_homes/{folder} /network_homes/{folder} nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"


# Create the list of project folders:
for folder in project_folder_names:
    project_folders.append(f"/projects/{folder}")

# Create the list of home folders:
for folder in home_folder_names:
    project_folders.append(f"/network_homes/{folder}")


# This is to create new home directories
for folder in home_folder_names:
    project_folders.append(f"/home/{folder}")

with open("/etc/ansible/facts.d/home_mounts.txt") as f:
    fstab_lines += "".join(f.readlines())


# Get a list of project folders that have disappeared
# We can use these to remove
# NOTE: Do not remove the home folders!
to_remove = []
for line in Path("/projects").glob("*"):
    if line.name not in [Path(_).name for _ in project_folders]:
        to_remove.append(line.name)


output = {"fstab": fstab_lines, "folders": project_folders, "removed": to_remove}
print(json.dumps(output, indent=2))
