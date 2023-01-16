import json
from pathlib import Path

folders = Path("/mnt/sw/software/kosmos-cluster/project_folders.lst").read_text().split("\n")
folders = [f for f in folders if f != "" and f[0] != "#"]

# Fixed lines:
lines = ""
lines += f"kronos:/data-pool/groups/aiforoncology /data/groups/aiforoncology nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"
lines += f"kronos:/data-pool/groups/beets-tan /data/groups/beets-tan nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"


for folder in folders:
    lines += f"rhea:/project-pool/projects/{folder} /projects/{folder} nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"

project_folders = ["/data/groups/aiforoncology", "/data/groups/beets-tan"]


# Get all project folders
to_remove = []
for line in Path("/projects").glob("*"):
    if line.name not in project_folders:
        to_remove.append(line.name)


for folder in folders:
    project_folders.append(f"/projects/{folder}")

output = {"fstab": lines, "folders": project_folders, "removed": to_remove}
print(json.dumps(output, indent=2))
