#!/usr/bin/env python
import argparse, os, sys

BURP_JAR="~/Applications/burp.jar"
DEFAULT_CONFIG="$HOME/Documents/github/utils/default-burp-config.json"
DOWNLOAD_DIR="~/Downloads/"

parser = argparse.ArgumentParser(description="Utility script to start or update Burp")

parser.add_argument('action', metavar="action", help="Required. The action to be performed. Possible values: open, update")
parser.add_argument('-c', '--config', dest="config", help="Load Burp config file located at <CONFIG>. Default to %s" % DEFAULT_CONFIG, 
	default=DEFAULT_CONFIG)
parser.add_argument('--no-conf', dest="is_blank", action="store_true", help="Override any config file option and load no config file")
parser.add_argument('-p', '--project', dest="project", help="Load Burp project file located at <PROJECT>")

args = parser.parse_args()

if args.action == 'update':
	exit_code = os.system("mv %s/burp*.jar %s" % (DOWNLOAD_DIR, BURP_JAR))
	if exit_code != 0:
		print "Is new JAR in %s?" % DOWNLOAD_DIR
	else:
		print "Burp updated."
elif args.action == 'open':
	proj_arg = "--project-file=\"%s\"" % args.project if args.project else "" 
	config_arg = "--config-file=\"%s\"" % args.config if not args.is_blank else ""
	cmd = "nohup java -jar %s %s %s > /dev/null 2>&1 &" % (BURP_JAR, config_arg, proj_arg)
	print cmd
	os.system(cmd)
else:
	print "Invalid Action. %s -h for more info" % sys.argv[0]


