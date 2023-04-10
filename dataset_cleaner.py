
import pandas as pd

#open dataset
df = pd.read_csv('clean_d_tweets.csv')

#kepp specific columns
df = df[['tweet', 'language']]


#find length of every tweet
lengths = df["tweet"].str.len() 

#find the maximum length to use as max_colwidth parameter
max_length = max(lengths)

#apply the maximum column width for tweet string ( we apply the greater value )
pd.set_option("max_colwidth", int(max_length)+1)


#create list with 3082 'depressed' elements to create the column
status = ['depressed'] * 3082

#add column with depression status
df['status'] = status


#option to display full dataset 
pd.set_option("display.max_rows", 3083, "display.max_columns", 3)


#print dataset basic info
print(df.info())


#check if there are NaN in 'tweet' column
#if returned dataframe is empty there are no NaN
bool_series_1 = pd.isnull(df["tweet"]) 
#in tweet column there are some NaNs
print(df[bool_series_1])

#check if there are NaN in 'language' columns
#if returned dataframe is empty there are no NaN
bool_series_2 = pd.isnull(df["language"]) 
#in language column there are not NaNs but there are multiple languages
print(df[bool_series_2])


#drop rows that contain tweet in different ( than 'en' ) language
df.drop(df[df['language'] != 'en'].index, inplace = True)

#drop rows that contain NaN tweets
df.drop(df[df['tweet'] == 0].index, inplace = True)

#drop the language column now we have finished with selection
df.drop(['language'], axis=1, inplace=True)

#export dataset to csv file
df.to_csv('double_clean_depr.csv')
