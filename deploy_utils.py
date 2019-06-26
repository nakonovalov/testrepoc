import subprocess
import zipfile
import os

path_www = "/Users/admin/PycharmProjects/deploy/www/testrepoc"

check_changes_cmd = "cd " + path_www + " ; git diff origin/master"
pull_c = "cd " + path_www + " ; git pull"
print(pull_c)

print(check_changes_cmd)

def execute_bash_cmd(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return [str(output), str(error)]


def check_changes():
    if execute_bash_cmd(check_changes_cmd)[0] == "b''":
        return False
    else:
        return True


def pull():
    return execute_bash_cmd(pull_c)


def create_backup(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def deploy():
    if not check_changes():
        return "No updates"
    else:
        zipf = zipfile.ZipFile('Backup.zip', 'w', zipfile.ZIP_DEFLATED)
        create_backup(path_www, zipf)
        zipf.close()
        res = pull()
        return res


print(pull())


