def draw_boot_reps(data, func, size):
    boot_replicates = np.empty(size)
    boot_sample = np.random.choice(data, len(data))
    for i in range(size):
        boot_replicates[i] = func(np.random.choice(data, len(data)))
    return boot_replicates
    #
    
if __name__ == '__main__': #main guard so function can be used seperately 
    import numpy as np
    import pandas as pd
# installing packages used

    data1 = pd.read_csv("gandhi_et_al_bouts.csv", skiprows=4)
# read in data, and skip the rows not containing data

    bout_lengths_wt = list(data1[data1.genotype == "wt"].bout_length)
    bout_lengths_mut = list(data1[data1.genotype == "mut"].bout_length)
# create lists of the bout lengths for the different genotypes

    mean_wt = np.mean(bout_lengths_wt)
    mean_mut = np.mean(bout_lengths_mut)
# store the mean of the bout lengths 

    bs_reps_wt = draw_boot_reps(bout_lengths_wt, np.mean, size=10000)
    bs_reps_mut = draw_boot_reps(bout_lengths_mut, np.mean, size=10000)
#use bootstrap replicate function to get samples 

    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
#calculate confidence intervals for a=0.05

    print("""
    genotype 'wt':  mean = {0:.3f}, confidence interval = [{1:.1f}, {2:.1f}]
    genotype 'mut': mean = {3:.3f}, confidence interval = [{4:.1f}, {5:.1f}]
    """.format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))
#print the mean and confidence intervals for both genotypes from the bootstrap 
