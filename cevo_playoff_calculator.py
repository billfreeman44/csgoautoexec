import random

n_teams=168
n_weeks=12
n_teams_in_playoffs=16
seed=10
teamids=range(n_teams)
teamwins=[0] * n_teams

for i in range(n_weeks):
    #print 'week= '+str(i)
    teamwins.sort()
    n_matches_played=0

    #loop through every "match" (so number of teams/2)
    while n_matches_played < n_teams/2:
        j=n_matches_played*2

        #determine random winner
        if random.random() > 0.5:
            teamwins[j]=teamwins[j]+1
        else:
            teamwins[j+1]=teamwins[j+1]+1
                
        n_matches_played=n_matches_played+1

for i in range(n_weeks+1):
    print str(i) + "-"+ str(abs(i-n_weeks))+" record teams: " + str(teamwins.count(i))

teamwins.sort()
teamwins.reverse()
#calculate where the border is.
border_num_wins=teamwins[n_teams_in_playoffs-1]
print "Teams above: "+str(teamwins[n_teams_in_playoffs-1])+" will make playoffs"
print str(teamwins[0:n_teams_in_playoffs-1].count(border_num_wins) + 1) +" teams that won " + str(border_num_wins) +" games will make playoffs"
print str(teamwins[n_teams_in_playoffs:-1].count(border_num_wins)) +" teams that won " + str(border_num_wins) +" games will NOT make playoffs"
