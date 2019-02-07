import string
import re
import settings

def getVersion(PatchToJson):
    with open(PatchToJson, 'r') as f:
        for line in f:
            if "version" in line:
                reg = re.compile('[^0-9v.-]')
                version = reg.sub('', line)
    return version

def ChangeLog(PatchToChanglog):
    version = getVersion(settings.PatchToJson)
    head, sep, tail = version.partition('-')
    ints = int(tail)+1
    versions = head+"-"+str(ints)

    with open(PatchToChanglog, 'r') as f:
        temp = open(".tempfile", "w")
        for line in f:
            add = line
            if "NEXT" in add:
                temp.write(add + "\n" +"# "+versions)
            temp.write(string.replace(line, "# NEXT", ""))
        temp.close()
#        print (string.replace(line, "# NEXT", ""))
    with open(".tempfile", "r") as temp:
        sh = open(PatchToChanglog, 'w')
        for lines in temp:
            sh.write(lines)
