# Uplift Modeling with Meta-Learners: Estimating Heterogeneous Treatment Effects

## Project Overview

This project aims to estimate the **Conditional Average Treatment Effect (CATE)** to evaluate the impact of an email marketing campaign on customer spending. Unlike traditional methods that estimate an overall average treatment effect, this approach leverages **uplift modeling** to uncover how different customer segments respond to the campaign, enabling more personalized marketing strategies. By utilizing **meta-learners** (including T-Learner, S-Learner, and X-Learner), I capture heterogeneous effects and compare their performance using robust evaluation metrics.

## Objective

The primary objectives are:
- Estimate the **CATE** of an email campaign on customer spending.
- Utilize **meta-learners** to uncover variations in treatment effects across different customer segments.
- Benchmark results using traditional regression models and evaluate the performance of each meta-learner.
- Conduct robustness checks and sensitivity analyses to estimate the business impact. 

## Data Description

The dataset consists of information on 64,000 customers who participated in an email campaign test, provided by Kevin Hillstrom [Source](https://blog.minethatdata.com/). Key features include demographic details, purchase history, and campaign engagement metrics.

![Data Overview](https://github.com/user-attachments/assets/92e3f8b2-ff03-43e7-8f9c-7d6e00f61568)

## Approach

### Check Randomization Assumption

### Methodology: Meta-Learners
Meta-learners were used to estimate **CATE** across different customer segments:
- You can read more about each meta-learner approach in my [Medium article](https://medium.com/@LillyH/part-2-1-conditional-treatment-heterogenous-effect-estimation-cate-w-7a25916bc6e7).

### 3. Evaluation
- **Uplift Metrics**: Performance was evaluated using **uplift scores**, which measure how effectively each model ranks differential responses to the email campaign.

## Results
- Identified customer segments more likely to increase spending when exposed to the email campaign.
- Compared the performance of different meta-learners, highlighting models that effectively captured treatment heterogeneity.
- Demonstrated the incremental impact of the email campaign, suggesting optimal customer targeting strategies.

## Tech Stack
- **Languages**: Python
- **Libraries**:
  - Data Manipulation: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - Modeling: `scikit-learn`, `EconML`, `xgboost`, `lightgbm`
  - Evaluation: `uplift`, `scipy`, `statsmodels`
