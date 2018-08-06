#!/usr/bin/env python3
__Author__ = "limugen"
import sys
import collections
ID,FORNAME,MIDDLENAME,SURNAME,DEPARTMENT = range(5)
User = collections.namedtuple(("User","username forename middlename surname id"))

def process_line(line,usernames):
    fields = line.split(":")
    username = generate_username(fields,usernames)
    user = User(username,fields[FORNAME],fields[MIDDLENAME],fields[SURNAME],fields[ID])

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h","--help"}:
        print("useage:{0} file1 [file2[...fileN]]".format(sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open(filename,encoding="utf8"):
            line = line.strip()
            if line:
                user = process_line(line,usernames)
                users[(user.surname.lower(),user.forename.lower(),user.id)] = user
def generate_username(fileds,usernames):
    username = ((fileds[FORNAME][0] + fileds[MIDDLENAME][:1] +
                 fileds[SURNAME].replace("-","").replace("''","")))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name,count)
        count +=1
    usernames.add(username)
    return username
def print_users(users):
    namewidth = 32
    usernamewidth = 9
    print("{0:<{nw}}{1:^6}{2:{uw}}".format(
        "Name","ID","Username",nw=namewidth,uw=usernamewidth))
    print("{0:-<{nw}}{0:-<6}{0:-<{uw}}".format(
        "",nw=namewidth,uw=usernamewidth))
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname},{0.forname}{1}".format(user,initial)
        print("{0:.<{nw}}({1,id:4}){1.username:{uw}}".format(
            name,user,nw=namewidth,uw=usernamewidth))
print_users(user)