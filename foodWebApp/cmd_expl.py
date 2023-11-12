from flask import json
import requests
import argparse

"""
REQUEST EXAMPLE:

python cmd_expl.py --type 2 --style -1 --mood neutral --stress no --depression no --bmi over --activity low 
--goal lose --sleep low --restr gluten-free vegetarian 
--imgurl1 https%3A%2F%2Fwww.giallozafferano.it%2Fimages%2Fricette%2F201%2F20113%2Ffoto_hd%2Fhd650x433_wm.jpg 
--imgurl2 https%3A%2F%2Fwww.giallozafferano.it%2Fimages%2Fricette%2F176%2F17635%2Ffoto_hd%2Fhd650x433_wm.jpg 
--difficulty 1 --user_time 0 --user_cost 5 --health_style 5 --health_condition 5 --user_ingredients oil carrot 
--user_age U40 --season winter --sex m

python foodWebApp/cmd_expl.py --type 2 --style -1 --mood neutral --stress no --depression no --bmi over --activity low --goal lose --sleep low --restr gluten-free vegetarian --imgurl1 https%3A%2F%2Fwww.giallozafferano.it%2Fimages%2Fricette%2F201%2F20113%2Ffoto_hd%2Fhd650x433_wm.jpg --imgurl2 https%3A%2F%2Fwww.giallozafferano.it%2Fimages%2Fricette%2F176%2F17635%2Ffoto_hd%2Fhd650x433_wm.jpg --difficulty 1 --user_time 0 --user_cost 5 --health_style 5 --health_condition 5 --user_ingredients oil carrot --user_age U40 --season winter --sex m
"""
parser = argparse.ArgumentParser(prog='cmd_expl', description='CMD explanation')
parser.add_argument('--type', required=True, help="[0,18]")
parser.add_argument('--style', required=True, help="-1 for single and comparative; 0 for single explanations; 1 for comparative explanation")
parser.add_argument('--imgurl1', required=True, help="URL of recipeA's image from GialloZafferano")
parser.add_argument('--imgurl2', help="URL of recipeB's image from GialloZafferano")
parser.add_argument('--user_age', help="numerical age or U20/U30/U40/U50/U60/O60")
parser.add_argument('--mood', help="bad/good/neutral")
parser.add_argument('--stress', help="yes/no")
parser.add_argument('--depression', help="yes/no")
parser.add_argument('--bmi', help="over/under/normal")
parser.add_argument('--health_style', help="1/2/3/4/5")
parser.add_argument('--health_condition', help="1/2/3/4/5")
parser.add_argument('--activity', help="low/high/normal")
parser.add_argument('--sleep', help="low/good")
parser.add_argument('--difficulty', help="1/2/3/4/5")
parser.add_argument('--user_time', help="[1,200] mins; 0=no contraints")
parser.add_argument('--user_cost', help="1/2/3/4/5; 5=not important")
parser.add_argument('--goal', help="lose/gain/no")
parser.add_argument('--restr', nargs='*', help="vegetarian/lactose-free/gluten-free/low-nickel/light")
parser.add_argument('--user_ingredients', nargs='*', help="zero, one or more favourite ingredients")
parser.add_argument('--sex', help="m/f")
parser.add_argument('--season', help="winter/spring/summer/autumn")

args = parser.parse_args()

url = "http://127.0.0.1:5003/exp/?"

url += "type=" + args.type + "&"
url += "style=" + args.style + "&"

if args.imgurl1 is not None:
    url += "imgurl1=" + args.imgurl1 + "&"

if args.imgurl2 is not None:
    url += "imgurl2=" + args.imgurl2 + "&"

if args.user_age is not None:
    url += "user_age=" + args.user_age + "&"

if args.mood is not None:
    url += "mood=" + args.mood + "&"

if args.stress is not None:
    url += "stress=" + args.stress + "&"

if args.depression is not None:
    url += "depression=" + args.depression + "&"

if args.bmi is not None:
    url += "bmi=" + args.bmi + "&"

if args.health_style is not None:
    url += "health_style=" + args.health_style + "&"

if args.health_condition is not None:
    url += "health_condition=" + args.health_condition + "&"

if args.activity is not None:
    url += "activity=" + args.activity + "&"

if args.sleep is not None:
    url += "sleep=" + args.sleep + "&"

if args.difficulty is not None:
    url += "difficulty=" + args.difficulty + "&"

if args.user_time is not None:
    url += "user_time=" + args.user_time + "&"

if args.user_cost is not None:
    url += "user_cost=" + args.user_cost + "&"

if args.goal is not None:
    url += "goal=" + args.goal + "&"

if args.restr is not None:
    url += "restr="
    for r in args.restr:
        url += r + ","
    url = url[:-1]
    url += "&"

if args.user_ingredients is not None:
    url += "user_ingredients="
    for ui in args.user_ingredients:
        url += ui + ","
    url = url[:-1]
    url += "&"

if args.sex is not None:
    url += "sex=" + args.sex + "&"

if args.season is not None:
    url += "season=" + args.season + "&"

url = url[:-1]

# app = Flask(__name__)

r = requests.get(url)
data = json.loads(r.text)
print(data)

with open('explanation.json', 'w+') as outfile:
    outfile.write(r.text)
