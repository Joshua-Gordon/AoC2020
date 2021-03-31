import sys
import re

def validate_passport(p):
    print(p)
    fields = []
    vals = []
    for x in p.split(" ")[:-1]:
        colon = x.find(":")
        fields.append(x[:colon])
        vals.append(x[colon+1:])
    if all([f in fields for f in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]]):
        creds =  dict(zip(fields,vals))
        if len(creds["byr"]) != 4:
            return False
        else:
            byr = int(creds["byr"])
            if byr not in range(1920,2003):
                return False
        if len(creds["iyr"]) != 4:
            return False
        else:
            iyr = int(creds["iyr"])
            if iyr not in range(2010,2021):
                return False
        if len(creds["eyr"]) != 4:
            return False
        else:
            eyr = int(creds["eyr"])
            if eyr not in range(2020,2031):
                return False
        hgt = creds["hgt"]
        if hgt[-2:] == "cm":
            val = int(hgt[:-2])
            if val not in range(150,194):
                return False
        elif hgt[-2:] == "in":
            val = int(hgt[:-2])
            if val not in range(59,77):
                return False
        else:
            return False
        hcl = creds["hcl"]
        if not re.match(r"#[0-9a-z]{6}",hcl):
            return False
        ecl = creds["ecl"]
        if not ecl in ["amb","blu","brn","gry","grn","hzl","oth"]:
            return False
        pid = creds["pid"]
        if len(pid) != 9:
            return False
        return True
    return False

def read_batch_file(fname):
    with open(fname) as f:
        data = f.readlines()
    passports = []
    passport = ""
    for line in data:
        print("> " + line)
        if line.strip() == "":
            passports.append(passport)
            passport = ""
        else:
            passport += line[:-1]+" "
    passports.append(passport)
    return passports

if __name__ == "__main__":
    fname = sys.argv[1]
    pports = read_batch_file(fname)
    print(len(pports))
    num_valid = len([p for p in pports if validate_passport(p)])
    print(num_valid)
