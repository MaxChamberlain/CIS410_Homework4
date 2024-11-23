import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def loadFile(path):
    data = pd.read_csv(path)
    return data

def printHead(data):
    print(data.head())

def printDataFrameInfo(data):
    print(data.info())

def printScoreColumns(data):
    print(data[['math score', 'reading score', 'writing score']].describe())
    
def groupByRaceAndCalcMean(data):
    print(data.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean())

def printColumnAsDataFrame(data, column):
    print(data[[column]])

def printColumnAsSeriesBracketNotation(data, column):
    print(data[column])

def printColumnAsSeriesDotNotation(data):
    print(data.lunch)

def printFemaleGT90(data):
    print(data[(data['gender'] == 'female') & (data['math score'] >= 90)])

def boxPlot(data, columns):
    data.boxplot(columns).plot(kind='box', figsize=(10, 10))
    plt.show()

def groupByGenderAndCalcMean(data):
    gender_means = data.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
    gender_means.plot(kind='bar', figsize=(10, 6))
    plt.title('Average Scores by Gender')
    plt.ylabel('Average Score')
    plt.show()

def plotCatplot(data):
    sns.catplot(x='race/ethnicity', kind='count', data=data, height=5, aspect=2)
    plt.title('Count of Students by Race/Ethnicity')
    plt.xticks(rotation=45)  # step 12
    plt.show()

def scatterPlotWithHue(data):
    sns.scatterplot(data=data, x='writing score', y='reading score', hue='test preparation course', palette='Set2')
    plt.title('Writing vs Reading Scores by Test Preparation Course (with hue)')
    plt.show()

def generalScatterPlot(data):
    data.plot.scatter(x='writing score', y='reading score', c=data['test preparation course'].map({'none': 'red', 'completed': 'blue'}))
    plt.title('Writing vs Reading Scores by Test Preparation Course (general)')
    plt.show()

def resizedScatterPlot(data):
    data.plot.scatter(x='writing score', y='reading score', c=data['test preparation course'].map({'none': 'red', 'completed': 'blue'}), figsize=(16, 4))
    plt.title('Writing vs Reading Scores by Test Preparation Course (Adjusted Size)')
    plt.show()

def main():
    data = loadFile('hw4_exams.csv')
    print('= OPERATIONS =')
    print('1. Print the first 5 rows of the data')
    print('2. Print the information of the data')
    print('3. Print the summary statistics of the math, reading, and writing scores')
    print('4. Group the data by race/ethnicity and display the mean of the math, reading, and writing scores')
    print('5. Print the lunch column as a DataFrame')
    print('6. Print the lunch column as a Series using bracket notation')
    print('7. Print the lunch column as a Series using dot notation')
    print('8. Print only rows where the gender is female and the math score is greater than or equal to 90')
    print('9. Create a box plot of the math, reading, and writing scores')
    print('10. Group the data by the gender column and calculate the average scores. Then create a bar plot.')
    print('11. Create a count plot of the number of students by race, with 45 degree labels')
    print('12. Create a count plot of the number of students by race, with 45 degree labels')
    print('13. Create a scatter plot of writing vs reading scores, with test preparation course as the hue')
    print('14. Create a general scatter plot of writing vs reading scores, with test preparation course as the color')
    print('15. Create a scatter plot of writing vs reading scores, with test preparation course as the color and adjusted size')
    print('0. Exit')
    operation = int(input('Enter the operation number: '))
    match operation:
        case 1:
            printHead(data)
        case 2:
            printDataFrameInfo(data)
        case 3:
            printScoreColumns(data)
        case 4:
            groupByRaceAndCalcMean(data)
        case 5:
            printColumnAsDataFrame(data, 'lunch')
        case 6:
            printColumnAsSeriesBracketNotation(data, 'lunch')
        case 7:
            printColumnAsSeriesDotNotation(data)
        case 8:
            printFemaleGT90(data)
        case 9:
            boxPlot(data, ['math score', 'reading score', 'writing score'])
        case 10:
            groupByGenderAndCalcMean(data)
        case 11:
            plotCatplot(data)
        case 12:
            plotCatplot(data)
        case 13:
            scatterPlotWithHue(data)
        case 14:
            generalScatterPlot(data)
        case 15:
            resizedScatterPlot(data)
        case 0:
            exit()
        case _:
            print('Invalid operation')
    input('Press any key to continue...')


if __name__ == '__main__':
    while True:
        main()