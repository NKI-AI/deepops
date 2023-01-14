import sys
import json

args = ''.join(sys.argv[1:])
folders = [_.strip() for _ in args.split(",") if _ != ""]

# Fixed lines:
lines = ""
lines += f"kronos:/data-pool/groups/aiforoncology /data/groups/aiforoncology nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"
lines += f"kronos:/data-pool/groups/beets-tan /data/groups/beets-tan nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"


for folder in folders:
    lines += f"rhea:/project-pool/projects/{folder} /projects/{folder} nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0\n"

project_folders = ["/data/groups/aiforoncology", "/data/groups/beets-tan"]

for folder in folders:
    project_folders.append(f"/projects/{folder}")

output = {"fstab": lines, "folders": project_folders}
print(json.dumps(output, indent=2))
