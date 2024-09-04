

def nb_year(p0, percent, aug, p): # p0 = starting pop, % = % growth, aug = new people, p = target pop
    years = 0 # years to reach target population
    while p0 < p: # while starting pop is less than the target pop
        p0 += p0 * percent / 100 + aug # make a math for new pop
        years += 1 # plus 1 it 
    return years # done 