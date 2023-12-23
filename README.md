<p align="center">
	<img src="Images/Header.png?raw=true" width=80% height=80%>
</p>

# Data Jobs Salaries in Mexico in November 2023
#### Daniel Eduardo López

<font size="-1"><a href="https://www.linkedin.com/in/daniel-eduardo-lopez">LinkedIn</a> | <a href="https://github.com/DanielEduardoLopez">GitHub </a></font>

**23 Dec 2023**

____
### **Contents**

1. [Introduction](#intro)<br>
2. [General Objective](#objective)<br>
3. [Research Question](#question)<br>
4. [Hypothesis](#hypothesis)<br>
5. [Abridged Methodology](#methodology)<br>
6. [Main Results](#results)<br>
7. [Dashboard](#dashboard)<br>
8. [Conclusions](#conclusions)<br>
9. [Partial Bibliography](#bibliography)<br>
10. [Description of Files in Repository](#files)<br>

____
### **1. Introduction** <a class="anchor" id="intro"></a>
With the emergence of the big data, new jobs have appeared demanding new sets of skills and expertise for extracting value from data (Axis Talent, 2020):

- Business Analysts (BA)
- Business Intelligence Analysts (BI)
- Data Analysts (DA)
- Data Architects (DR) 
- Data Engineers (DE) 
- Data Scientists (DS)
- Machine Learning Engineers (ML)

Which one is the most valued in the Mexican labor market currently?

____
### **2. General Objective** <a class="anchor" id="objective"></a>
To identify which data job category has the highest salary in the Mexican labor market in November 2023 according to the OCC website.
____
### **3. Research Question** <a class="anchor" id="question"></a>
Which data job category has the highest salary in the Mexican labor market in November 2023 according to the OCC website?
____
### **4. Hypothesis** <a class="anchor" id="hypothesis"></a>
The **Data Scientist** position has the highest salary in the Mexican labor market in November 2023 according to the OCC website.
____
### **5. Abridged Methodology** <a class="anchor" id="methodology"></a>
The methodology of the present study is based on Rollin’s Foundational Methodology for Data Science (Rollins, 2015).

1) **Analytical approach**: Descriptive and inferential statistics.
2) **Data requirements**: Data about job positions such as job name, salary, employer and location.
3) **Data collection**: Data was collected from the OCC Website (Mexico) on 26 November 2023, through web scraping with Python 3 and its libraries Selenium, BeautifulSoup, and Regex.
4) **Data exploration**: Data was explored with Python 3 and its libraries Matplotlib and Seaborn.
5) **Data preparation**:  Data then was cleaned with Python 3 and its libraries Pandas and Numpy.
6) **Data analysis**: Data was analyzed with Python 3 and its libraries Pandas, Scipy and Statsmodels and visualized with Matplotlib, Seaborn, Folium and Plotly. 
7) **Statistical analysis**: The D'Agostino-Pearson normality test was used to assess the normality of the data jobs salary distribution. Then, both parametric (ANOVA and t-test with unequal variance) and non-parametric (Mann-Whitney U and Kruskal-Wallis H) tests were carried out to assess the significance of the obtained results. Furthermore, an effect size analysis was carried out by computing the absolute mean salary differences, the Cohen’s d, and the bootstrap confidence intervals for the mean for each data job category. This, in order to assess whether the salary differences were significant from a practical point of view.
8) **Implementation**:  A <a href="https://data-jobs-mx-2023.onrender.com"><b>dashboard</b></a> was built with Plotly and Dash and it was deployed on Render.

Furthermore:

9) A <a href="https://github.com/DanielEduardoLopez/DataJobs-Nov2023-MX/blob/main/Report.pdf"><b>final report</b></a> was written with the complete results obtained from the data.
10) Some <a href="https://github.com/DanielEduardoLopez/DataJobs-Nov2023-MX/blob/main/Slides.pdf"><b>slides</b></a> were prepared with the **most important insights** from the report.

___
### **6. Main Results** <a class="anchor" id="results"></a>

Pending.

