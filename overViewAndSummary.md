## Summary 

#### Research Question : 
#### What are the pushing factors that increase the number of firearm sales in the U.S? And what are the sales figures for each factor? 

Many variables and factors could affect the number of gun sales in U.S. These factors span from policy changes, political motives/fears, and misinformation. However, now we are interested in looking at **_FBI_** data of background checks of gun purchases to predict the number of guns sales in the future and what event actually causes the number of sales to increase or decrease. 


## Project Description

This research question has been looked at a lot in recent years. In fact some of the discussion has moved past from whether it happens or not to [understanding why it happens](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182408). Some point to fear of potential policy change following the mass shooting, or a need to protect themselves and their families by owning a gun. Other research groups try to understand  [how the mass shootings influence public support for gun control](https://www.cambridge.org/core/journals/british-journal-of-political-science/article/mass-shootings-and-public-support-for-gun-control/8F38356AF4DB22B8B7DF28052234FA09/core-reader).  [Many of these studies have been descriptive](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0177720) although, we instead plan to create a predictive analysis using a variety of the proposed factors. Through the process of creating a predictive model for gun sales we hope to gain a better understanding of how greatly the proposed factors really influence gun control. 

Through the process of creating a predictive model for gun sales we hope to gain a better understanding of how greatly the proposed factors really influence gun control. We plan to use a KNearestNeighbors model in order to test our hypothesis on what factors influence gun control. The target audience of our research will be policy makers and the general public who participates in the election process. They may want to know what the effects of discussing control are following shootings and for some policy makers they may want to know how to mitigate the increase in gun purchases.


## Technical Description
Our final research will displayed on a **_Shiny_** app. This will allow for user interaction with our research and better understand what factors affect gun sales. Our biggest anticipated challenge in data collection will be collecting specific local data to be able to improve the accuracy of our models by including regional cultural norms surrounding gun ownership and use. In order to produce a top tier report, we will need to improve our styling ability within the Shiny app domain to produce an interface that is both intuitive and informative. 

Our approach will consist of three key steps. First, we will clean and wrangle all of our data into one dataframe. Next, exploratory data analysis will be used to determine if there are any glaring trends or (non)correlations. Finally, we will use **_Supervised Machine Learning_** to engineer a **_KNearestNeighbors_** model that best predicts the number of gun sales based upon the factors that best directly correlate with the volume of sales. The most concerning challenge stems from our data collection and wrangling decisions; what level of regionally accounts for the regional differences around gun purchase and ownership without overfitting our model?




### Data Sources 
[Gun by population, Socrata.com](https://opendata.socrata.com/Government/Guns-by-Population/ymtd-vpew)

[Crime-guns-and-population, Socrata.com](https://opendata.socrata.com/Government/Crime-Guns-and-Population/5c9i-6x2e)

[Guns-by-population, Socrata.com](https://opendata.socrata.com/Government/Guns-by-Pop/tx26-fytf)

[FBI background check data, fbi.gov](https://www.fbi.gov/file-repository/nics_firearm_checks_-_month_year_by_state_type.pdf/view) 

[ Data for gun sales, BuzzFeedNews.git ](https://github.com/BuzzFeedNews/nics-firearm-background-checks)
