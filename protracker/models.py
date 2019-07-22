from django.db import models

class Hero(models.Model):
    hero_name = models.CharField(max_length=20, default = 'Dota 2 Hero') 
    hero_id = models.IntegerField()
    def __str__(self):
        return str(self.hero_id)
        
    def get_winrate(self):
        wins = self.wins.count()
        losses = self.losts.count()
        if wins + losses != 0:
            return int((wins/(wins+losses))*100)
        else:
            return 0 
    winrate = property(get_winrate)

class Match(models.Model):
    match_id = models.IntegerField()
    match_date = models.DateTimeField('Match Date')
    heros_won = models.ManyToManyField(Hero, related_name='wins')
    heros_lost = models.ManyToManyField(Hero, related_name='losts')
    def __str__(self):
        return str(self.match_id)



class LiveMatch(models.Model):
    counter = models.IntegerField(default = 1)
    myList = models.TextField(null=True)