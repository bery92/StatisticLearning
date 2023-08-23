import pandas as pd
import matplotlib.pyplot as plt


def problem8():
    #a-c
    college = pd.read_csv("../Data/College.csv")
    college = college.rename({'Unnamed: 0': 'College'},axis=1)
    #college = college.set_index("College")
    #d
    pd.plotting.scatter_matrix(college[['Top10perc', 'Apps', 'Enroll']])
    #e
    college.boxplot('Outstate', by = 'Private')
    
    #f
    college['Elite'] = pd.cut(college['Top10perc'],[0,50,100],labels=['No', 'Yes'])
    college.boxplot('Outstate', by = 'Elite')
    
    print(f"There are {college['Elite'].value_counts('Yes')} Elite colleges")

    #g
    fig, axs = plt.subplots(2,2)
    axs[0,0].hist(college['PhD'])
    axs[0,1].hist(college['Accept'])
    axs[1,0].hist(college['Top10perc'])
    axs[1,1].hist(college['Grad.Rate'])

    #h
    
    plt.show()

problem8()
