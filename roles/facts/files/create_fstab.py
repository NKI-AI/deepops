import sys
import json

args = ''.join(sys.argv[1:])
folders = [_.strip() for _ in args.split(",") if _ != ""]

lines = []
for folder in folders:
    lines.append(f"rhea:/project-pool/projects/{folder} /projects/{folder} nfs rsize=524288,wsize=524288,vers=3,timeo=30,intr 0 0")

project_folders = []
for folder in folders:
    project_folders.append(f"/projects/{folder}")

output = {"fstab": lines, "folders": project_folders}
print(json.dumps(output, indent=2))
