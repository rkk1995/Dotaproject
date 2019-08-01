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
    def totalgames(self):
        return self.wins.count() + self.losts.count()
    def totalwins(self):
        return self.wins.count()
    winrate = property(get_winrate)
    totalwins = property(totalwins)
    totalgames = property(totalgames)    

class Match(models.Model):
    match_id = models.IntegerField()
    match_date = models.IntegerField('Match Date')
    match_mmr = models.IntegerField( 'MMR', default= 1)
    heros_won = models.ManyToManyField(Hero, related_name='wins')
    heros_lost = models.ManyToManyField(Hero, related_name='losts')
    def __str__(self):
        return str(self.match_id)


class Player(models.Model):
    player_id = models.IntegerField()
    player_name = models.CharField(max_length = 20, default = 'Dota 2 Player')
    def __str__(self):
        return str(self.player_name)

class Role(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    win = models.BooleanField()
    def __str__(self):
        return player.player_name
    
    class Meta:
         unique_together = ['match', 'player']


class MatchesToGet(models.Model):
    match_id = models.IntegerField()
    def __str__(self):
        return str(self.match_id)


class RoleToGet(models.Model):
    matchtoget = models.ForeignKey(MatchesToGet, on_delete = models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    slot = models.IntegerField()


class LiveMatch(models.Model):
    counter = models.IntegerField(default = 1)
    myList = models.TextField(null=True)