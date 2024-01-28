<p align="center">
	<img src="Figures/Header.png?raw=true" width=80% height=80%>
</p>

# Data Jobs Salaries in Mexico in November 2023
#### Daniel Eduardo López

<font size="-1"><a href="https://www.linkedin.com/in/daniel-eduardo-lopez">LinkedIn</a> | <a href="https://github.com/DanielEduardoLopez">GitHub </a></font>

**14 January 2024**

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
7) **Statistical analysis**: The D'Agostino-Pearson normality test was used to assess the normality of the data jobs salary distribution. Then, both parametric (ANOVA, Tukey-Kramer, one-sample and two-sample T-tests) and non-parametric (Kruskal-Wallis H, Dunn, Wilcoxon signed-rank, and Mann-Whitney U) tests were carried out to assess the significance of the obtained results. Furthermore, an effect size analysis was carried out by computing the absolute mean salary differences, the Cohen’s d, and the bootstrap confidence intervals for the mean for each data job category. This, in order to assess whether the salary differences were significant from a practical point of view.
8) **Implementation**:  A <a href="https://data-jobs-mx-nov2023.onrender.com"><b>dashboard</b></a> was built with Plotly and Dash and it was deployed on Render.

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
	<img src="Figures/Fig17_DataJobsSalaryDistribution2.png?raw=true" width=60% height=60%>
</p>

A normality assumption could not be hold as the D'Agostino-Pearson normality test indicated that the null hypothesis that the sample comes from a normal distribution must be rejected at a signification level of $\alpha$ = 0.05 (*p*-value < 0.001).

Notwithstanding with the above, for the purposes of the present study, both parametric (ANOVA, Tukey-Kramer, one-sample T-test, and two-sample T-test with unequal variance) and non-parametric (Kruskal-Wallis H, Dunn, Wilcoxon signed-rank, and Mann-Whitney U) tests were carried out to assess the significance of the obtained results.

The salaries for each data job category are shown in the following box plot:

<p align="center">
	<img src="Figures/Fig11_SalaryPerDataJobCategory2.png?raw=true" width=60% height=60%>
</p>

The figure above suggests that, the average and median salaries for the different data jobs categories are:

<p align="center">
	<img src="Figures/Fig12_MeanMedianSalaryPerDataJob2.png?raw=true" width=60% height=60%>
</p>

Thus, in view of the figure above, the mean and median monthly salaries are consistent for each data job category. And, it is noteworthy that the salary figures for **ML Engineers** and **Data Architect** positions were the highest ones. 

A one-way analysis of variance (ANOVA) procedure and a Kruskal-Wallis H test confirmed that the salary differences among the data jobs categories were statistically significant at a signification level of $\alpha$ = 0.05 (*p*-value < 0.001 in both tests).

Later, the Tukey-Kramer and Dunn post hoc tests were performed to identify to detect which salary differences among the data jobs were statistically significant, finding some significant differences that were further tested with a series of pairwise two-sample t-tests with unequal variance (Welch's test) and Mann-Whitney U tests. However, as only one salary observation was retrieved for ML Engineer positions, said value was compared to the salary mean of other data jobs by means of a one-sample t-test and the Wilcoxon signed-rank test.

In this sense, it was found that the mean salary for Data Architect positions was not significantly lower than that for a ML Engineer. On the other hand, at a signification level of $\alpha$ = 0.05 (*p*-value < 0.05), Data Engineers and Data Scientists mean salaries were significantly lower than that for ML Engineer. Indeed, from the effect size analysis, the mean salary difference between ML Engineer and Data Engineer positions was, not only statistically significant, but also practically significant as a difference of $19,612 MXN per month and a percentage difference of about 35.53% is non-neglectable in the Mexican labor market.

On the other hand, the mean salary differences between **ML Engineer-Business Analyst**, **ML Engineer-BI Analyst**, **ML Engineer-Data Analyst**, **Data Architect-Business Analyst**, **Data Architect-BI Analyst**, **Data Architect-Data Analyst**, **Data Engineer-Business Analyst**, **Data Engineer-BI Analyst**, **Data Engineer-Data Analyst**, **Data Scientist-BI Analyst**,  **Data Scientist-Data Analyst**, **Business Analyst-Data Analyst**, and **BI Analyst-Data Analyst** positions were statistically significant at the same signification level; whereas the mean salary differences between **Data Architect-Data Engineer**, **Data Engineer-Data Scientist**, **Data Scientist-Business Analyst**, and **Business Analyst-BI Analyst** were not statistically significant at the same signification level.

Thus, according to the results from the present statistical analysis, average salaries for ML Engineers and Data Architects are the highest ones in the current Mexican labor market. However, this conclusion must be taken with caution as only one salary observation was retrieved for ML Engineer positions.

Furthermore, the highest salaries can be found in Ciudad de México, Nuevo León, Jalisco, Estado de México, and in remote.

<p align="center">
	<img src="Figures/Fig13_SalaryPerLocationAndDataJobCategory2.png?raw=true" width=60% height=60%>
</p>

Moreover, the companies offering the highest salaries are **Ecosistemex**, **Caspex Corp**, **Addon Technologies**, **Enterprise Solutions**, and **Softek**, which correspond to recruiting agencies and tech consulting firms.

<p align="center">
	<img src="Figures/Fig14_Top20SalaryPerCompany2.png?raw=true" width=60% height=60%>
</p>

Finally, for **BI Analyst** positions, the company offering higher salaries are *Randstad* and *Ids Comercial*. For **Business Analyst** positions, the organizations offering higher salaries are *Manpower* and *Totaltech*. For **Data Analyst** positions, the organizations offering higher salaries are *Caspex* and *Santander*. For **Data Architect** positions, the organizations offering higher salaries are *Softtek* and *Everis*. For **Data Engineer** positions, the organizations offering higher salaries are *Manpower*, and *Addon Technologies*. For **Data Scientist** positions, the organizations offering higher salaries are *Ecosistemex* and *Enterprises Solutions*. And, at last, for **ML Engineer** positions, the only company with a disclosed salary is *Enterprise Solutions*.

<p align="center">
	<img src="Figures/Fig15_SalaryPerCompanyAndDataJobCategory2.png?raw=true" width=60% height=60%>
</p>

Please refer to the **[Complete Report](https://github.com/DanielEduardoLopez/DataJobsMX-Nov2023/blob/main/Report.pdf)** for the full results and discussion.

___
### **7. Dashboard** <a class="anchor" id="dashboard"></a>

To view and play with the **interactive dashboard**, please visit this **[link](https://data-jobs-mx-nov2023.onrender.com)**.

<p align="center">
	<img src="Figures/Dashboard.png?raw=true" width=65% height=65%>
</p>

Or, if you prefer to deploy the app locally, please download the **[app](https://github.com/DanielEduardoLopez/DataJobsMX-Nov2023/blob/main/3_DataJobsMX_Nov2023_Dashboard.py)** into a directory of your choice. Then, run the app using the following command in Windows:
```bash
python 3_DataJobsMX_Nov2023_Dashboard.py
```
And visit http://127.0.0.1:8050/ in your web browser.

Please note that Python 3 and its libraries Numpy, Pandas, Plotly and Dash are required for properly running the dashboard.

___
### **8. Conclusions** <a class="anchor" id="conclusions"></a>

**ML Engineer** and **Data Architect** are the data job categories with **the highest salary** in the Mexican labor market in November 2023 according to the OCC website. However, this result must be taken with caution as only one salary observation could be retrieved for the former position.

On the contrary, **Data Analyst** is the data job category **more demanded** in the current Mexican labor market and across the different Mexican states, even though it was also the one with **the lowest salary**.

**Ciudad de México** is the place where it is possible to find the highest jobs demand and the highest salaries, even though high salaries can also be found in remote positions.

**ML Engineer** , and **Data Architect** positions are concentrated in Ciudad de México, Nuevo León, and Jalisco, and are most likely to be found in tech consulting firms and banks.

**Data Analyst**, **Business Scientist**, and **Data Engineer** positions are more demanded across different type of organizations and locations.

**Bairesdev**, **Banamex**, **Pepsico** and **Softek** exhibited the highest demand of data jobs positions; while **Ecosistemex**, **Caspex Corp**, **Addon Technologies**, **Enterprise Solutions**, and **Softek**, offered the highest salaries.

This study had **limitations**: 
- Only used OCC as source of information during a very short period of time (just 26 November 2023). 
- Very few salary observations were retrieved for ML Engineer, Data Architect and Data Scientist positions.
- Collected data mostly correspond to Ciudad de México, Nuevo León, Jalisco, and Estado de México.
- No distinction was made among entry level, middle and senior positions. 

**Future perspectives**:
- Gather data from more job websites.
- Retrieve information for a longer time span.
- Collect more salary observations for Data Architect and Data Scientist positions.
- Collect more salary data for other Mexican states.
- Make a distinction among entry level, middle and senior positions.


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
1_DataJobsMX_Nov2023_DataCollection.html | HTML version of the Jupyter notebook for collecting the data through the web scraping.
2_DataJobsMX_Nov2023_DataAnalysis.ipynb | Jupyter Notebook for performing the data exploration, preparation, visualization and statistical analysis.
2_DataJobsMX_Nov2023_DataAnalysis.html |  HTML version of the Jupyter Notebook for performing the data exploration, preparation, visualization and statistical analysis.
3_DataJobsMX_Nov2023_Dashboard.py | Python script for the interactive dashboard.
Dataset_processed.csv | CSV file with the cleaned dataset.
Dataset_raw.csv | CSV file with the raw data collected from web scraping.
requirements.txt | Python requirements file
Slides.pdf | Slides with the most important insights from this project.

