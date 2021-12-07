import subprocess
proc = subprocess.run("python hello.py", stdout=subprocess.PIPE)
output_data = proc.stdout.decode()


print("Wombats are fun!")
