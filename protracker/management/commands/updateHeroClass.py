from django.core.management.base import BaseCommand
import os, pickle
from protracker.models import Hero


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         dirname = "D:\Coding\Dotaproject\protracker\databases"
#         with open(os.path.join(dirname, "HeroImageDict.txt"), "rb") as myFile:
#             HeroImageDict = pickle.load(myFile)
#         for i in list(HeroImageDict.keys()):
#             Hero.objects.create(hero_id = i , hero_name = HeroImageDict[i]['hero'])

