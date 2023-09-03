import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv') 

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
        # get count of each race 
    
    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # List of advanced degrees
    advanced_degrees = ['Bachelors', 'Masters', 'Doctorate']

    # Filter the DataFrame for advanced degree holders
    advanced_degree_df = df[df['education'].isin(advanced_degrees)]
    non_advanced_df = df[~df['education'].isin(advanced_degrees)]

    # Filter further for those with income greater than 50K
    high_income_advanced_degree_df = advanced_degree_df[advanced_degree_df['salary'] == '>50K']
    high_income_non_advanced_df = non_advanced_df[non_advanced_df['salary'] == '>50K']

    # Calculate the percentage salary >50K
    higher_education_rich = round((len(high_income_advanced_degree_df) / len(advanced_degree_df)) * 100, 1)
    lower_education_rich = round((len(high_income_non_advanced_df) / len(non_advanced_df)) * 100, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = round((df[df['hours-per-week'] == min_work_hours]['salary'] == '>50K').mean() * 100)


    # What country has the highest percentage of people that earn >50K?
    rich = df[df['salary'] == '>50K']  # Filter out people who earn >50K
    high_earning_by_country = rich['native-country'].value_counts() # count of high earners for each native country
    total_by_country = df['native-country'].value_counts() # count of people from each native country
    percentage_high_earning_by_country = (high_earning_by_country / total_by_country) * 100 # # of high earners for each country
    highest_earning_country = percentage_high_earning_by_country.idxmax() # country with highest % of high earners
    highest_earning_country_percentage = round(percentage_high_earning_by_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    # series of ppl in india who earn >50k
    high_earners_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    # Group by 'occupation' and count occurrences
    occupation_counts = high_earners_india['occupation'].value_counts()
    # Find the most popular occupation
    top_IN_occupation = occupation_counts.idxmax()
    

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
