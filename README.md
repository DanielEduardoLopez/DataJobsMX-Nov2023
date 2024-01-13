<p align="center">
	<img src="Figures/Header.png?raw=true" width=80% height=80%>
</p>

# Data Jobs Salaries in Mexico in November 2023
#### Daniel Eduardo López

<font size="-1"><a href="https://www.linkedin.com/in/daniel-eduardo-lopez">LinkedIn</a> | <a href="https://github.com/DanielEduardoLopez">GitHub </a></font>

**14 Ene 2024**

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
With the emergence of the big data, new jobs have appeared demanding new sets of skills and expertise for extracting value from data (Axis Talent, 2020; ai-jobs.net, 2023):

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
The **Data Architect** position has the highest salary in the Mexican labor market in November 2023 according to the OCC website.
____
### **5. Abridged Methodology** <a class="anchor" id="methodology"></a>
The methodology of the present study is based on Rollin’s Foundational Methodology for Data Science (Rollins, 2015).

1) **Analytical approach**: Descriptive and inferential statistics.
2) **Data requirements**: Data about job positions such as job name, salary, employer and location.
3) **Data collection**: Data was collected from the OCC Website (Mexico) on 26 November 2023, through web scraping with Python 3 and its libraries Selenium, BeautifulSoup, and Regex.
4) **Data exploration**: Data was explored with Python 3 and its libraries Matplotlib and Seaborn.
5) **Data preparation**:  Data then was cleaned with Python 3 and its libraries Pandas and Numpy.
6) **Data analysis**: Data was analyzed with Python 3 and its libraries Pandas, Scipy and Statsmodels and visualized with Matplotlib, Seaborn, Folium and Plotly. 
7) **Statistical analysis**: The D'Agostino-Pearson normality test was used to assess the normality of the data jobs salary distribution. Then, both parametric (ANOVA, Tukey-Kramer and one-sample and two-sample T-tests with unequal variance) and non-parametric (Kruskal-Wallis H, Dunn and Mann-Whitney U) tests were carried out to assess the significance of the obtained results. Furthermore, an effect size analysis was carried out by computing the absolute mean salary differences, the Cohen’s d, and the bootstrap confidence intervals for the mean for each data job category. This, in order to assess whether the salary differences were significant from a practical point of view.
8) **Implementation**:  A <a href="https://data-jobs-mx-2023.onrender.com"><b>dashboard</b></a> was built with Plotly and Dash and it was deployed on Render.

Furthermore:

9) A <a href="https://github.com/DanielEduardoLopez/DataJobs-Nov2023-MX/blob/main/Report.pdf"><b>final report</b></a> was written with the complete results obtained from the data.
10) Some <a href="https://github.com/DanielEduardoLopez/DataJobs-Nov2023-MX/blob/main/Slides.pdf"><b>slides</b></a> were prepared with the **most important insights** from the report.

___
### **6. Main Results** <a class="anchor" id="results"></a>

From the sample of 563 data jobs retrieved, the most demanded data job category was **Data Analyst**, with 33% of the total demand of data jobs in Mexico at the time of this study. On the contrary, **ML Engineer** positions are the less demanded, with about 1% out of the total.

<p align="center">
	<img src="Figures/Fig1_DemandOfDataJobsPerCategory2.png?raw=true" width=60% height=60%>
</p>

On the other hand, the data jobs demand is highly concentrated in Mexico City (“**Ciudad de México**”, in Spanish) with about the 57% of the total national demand of data jobs. Then, **Jalisco** and **Nuevo León** represented a distant second place with about the 9% of the demand. Finally, Remote positions and Estado de México accounted for about the 8% and 4% of the demand, respectively; whereas the rest of the country is lagging in terms of data jobs creation. 

<p align="center">
	<img src="Figures/Fig2_DemandOfDataJobsPerMexicanState.png?raw=true" width=60% height=60%>
</p>

Regarding the data jobs demand per location, **Data Analyst** position is the one most demanded across the Mexican States; whereas **Data Architect** and **ML Engineer** are the less demanded, as they are mostly concentrated in Mexico City and Jalisco.

<p align="center">
	<img src="Figures/Fig4_DemandPerLocationAndDataJobCategory2.png?raw=true" width=60% height=60%>
</p>

Moreover, **Bairesdev** is nowadays the biggest seeker of data skills in the Mexican labor market, along with **Banamex**, **Pesico** and **Softek**. 

<p align="center">
	<img src="Figures/Fig5_TopCompaniesDemandingDataJobs.png?raw=true" width=60% height=60%>
</p>

Furthermore, **Data Analyst** and **Data Engineer** positions are more demanded across different organizations. On the contrary, **Data Scientist**, **Data Architect** and, certainly, **ML Engineers** vacancies are demanded in more specific organizations like tech consulting companies and banks.

<p align="center">
	<img src="Figures/Fig6_DemandPerCompanyAndDataJobCategory.png?raw=true" width=60% height=60%>
</p>

As expectable, most of the companies are located in **Ciudad de México** as the large majority of the vacancies are offered there. However, the heatmap shows that there are some organizations that are spread across several Mexican states such as Bairesdev or Pepsico. Futhermore, there are few well-known companies whose data jobs demand is not located in the capital region, such as Jonhson Controls which is located in Nuevo León.

<p align="center">
	<img src="Figures/Fig7_DemandPerCompanyAndLocationTop30_2.png?raw=true" width=60% height=60%>
</p>

Overall, from a sample of **197** vacancies with disclosed salary, the average salary of the data jobs in Mexico in November 2023 was **$32,163 MXN (SD = 19,417)** per month. 

<p align="center">
	<img src="Figures/Fig15_DataJobsSalaryDistribution2.png?raw=true" width=60% height=60%>
</p>

A normality assumption could not be hold as the D'Agostino-Pearson normality test indicated that the null hypothesis that the sample comes from a normal distribution must be rejected at a signification level of $\alpha$ = 0.05 (*p*-value < 0.001).

Notwithstanding with the above, for the purposes of the present study, both parametric (ANOVA, Tukey-Kramer, and one-sample and two-sample T-test with unequal variance) and non-parametric (Kruskal-Wallis H, Dunn, and Mann-Whitney U) tests were carried out to assess the significance of the obtained results.

___
### **7. Dashboard** <a class="anchor" id="dashboard"></a>

Pending.


___
### **8. Conclusions** <a class="anchor" id="conclusions"></a>

Pending.


___
### **9. Partial Bibliography** <a class="anchor" id="bibliography"></a>

- **ai-jobs.net (2023).** *Machine Learning Engineer vs. Business Intelligence Data Analyst*. https://ai-jobs.net/insights/machine-learning-engineer-vs-business-intelligence-data-analyst/
- **Axis Talent. (2020).** *The Ecosystem of Data Jobs - Making sense of the Data Job Market*. https://www.axistalent.io/blog/the-ecosystem-of-data-jobs-making-sense-of-the-data-job-market
- **Rollins, J. B. (2015).** *Metodología Fundamental para la Ciencia de Datos*. Somers: IBM Corporation. https://www.ibm.com/downloads/cas/WKK9DX51

___
### **10. Description of Files in Repository** <a class="anchor" id="files"></a>

File | Description
:--- | :---
1_DataJobsMX_Nov2023_DataCollection.ipynb | Jupyter notebook for collecting the data through the web scraping.
2_DataJobsMX_Nov2023_DataAnalysis.ipynb | Jupyter Notebook for performing the data exploration, preparation, visualization and statistical analysis.
Dataset_processed.csv | CSV file with the cleaned dataset.
Dataset_raw.csv | CSV file with the raw data collected from web scraping.


