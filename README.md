# Student Exam Analysis Tool

This project provides a Python-based tool to analyze a dataset of student exam scores. The tool uses pandas, matplotlib, and seaborn to perform various data analysis and visualization tasks.

## Features

The tool supports the following operations:

1. **Print the First 5 Rows**  
   Display the first five rows of the dataset for a quick overview.

2. **Print DataFrame Information**  
   Show basic information about the dataset, including column names, data types, and non-null values.

3. **Summary Statistics**  
   Calculate and display summary statistics for the math, reading, and writing scores.

4. **Group by Race/Ethnicity**  
   Group the data by `race/ethnicity` and calculate the mean scores for math, reading, and writing.

5. **Single Column as a DataFrame**  
   Extract and display a specified column as a DataFrame.

6. **Single Column as a Series (Bracket Notation)**  
   Extract and display a specified column as a Series using bracket notation.

7. **Single Column as a Series (Dot Notation)**  
   Extract and display a specified column as a Series using dot notation.

8. **Filter Rows**  
   Display rows where the gender is female and the math score is greater than or equal to 90.

9. **Box Plot**  
   Create a box plot for the math, reading, and writing scores.

10. **Bar Plot by Gender**  
    Group the data by gender, calculate the average scores, and display a bar plot.

11. **Count Plot by Race/Ethnicity**  
    Create a count plot to visualize the number of students in each `race/ethnicity` group.

12. **Scatter Plot (Specific Method)**  
    Create a scatter plot comparing writing and reading scores, with `test preparation course` as the hue.

13. **Scatter Plot (General Method)**  
    Create a general scatter plot comparing writing and reading scores, with `test preparation course` as the color.

14. **Resized Scatter Plot**  
    Create a scatter plot similar to the general method but with an adjusted size.

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn

## How to Use

1. Clone or download the repository.
2. Ensure that the dataset file (`hw4_exams.csv`) is in the same directory as the script.
3. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```
4. Run the script:
   ```bash
   python script_name.py
   ```
5. Follow the on-screen instructions to select an operation.

## Functions

- **`loadFile(path)`**: Loads the CSV file into a pandas DataFrame.
- **`printHead(data)`**: Displays the first five rows of the dataset.
- **`printDataFrameInfo(data)`**: Shows basic DataFrame information.
- **`printScoreColumns(data)`**: Displays summary statistics for math, reading, and writing scores.
- **`groupByRaceAndCalcMean(data)`**: Groups data by `race/ethnicity` and calculates mean scores.
- **`printColumnAsDataFrame(data, column)`**: Displays a specified column as a DataFrame.
- **`printColumnAsSeriesBracketNotation(data, column)`**: Displays a specified column as a Series using bracket notation.
- **`printColumnAsSeriesDotNotation(data)`**: Displays the `lunch` column as a Series using dot notation.
- **`printFemaleGT90(data)`**: Filters and displays rows for females with a math score >= 90.
- **`boxPlot(data, columns)`**: Creates a box plot for specified columns.
- **`groupByGenderAndCalcMean(data)`**: Groups data by `gender`, calculates mean scores, and creates a bar plot.
- **`plotCatplot(data)`**: Creates a count plot for `race/ethnicity`.
- **`scatterPlotWithHue(data)`**: Creates a scatter plot with `test preparation course` as the hue.
- **`generalScatterPlot(data)`**: Creates a general scatter plot with `test preparation course` as the color.
- **`resizedScatterPlot(data)`**: Creates a resized scatter plot.

## Menu System

The tool uses a menu-driven interface. The user selects operations by entering the corresponding operation number. The program will execute the chosen operation and prompt the user to continue or exit.

Example Menu:
```
= OPERATIONS =
1. Print the first 5 rows of the data
2. Print the information of the data
3. Print the summary statistics of the math, reading, and writing scores
...
15. Create a scatter plot of writing vs reading scores, with test preparation course as the color and adjusted size
0. Exit
Enter the operation number: 
```
---