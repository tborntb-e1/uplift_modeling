# Uplift Modeling with Meta-Learners: Estimating Heterogeneous Treatment Effects

## Project Overview

This project aims to estimate the **Conditional Average Treatment Effect (CATE)** to evaluate the impact of an email marketing campaign on customer spending. Unlike traditional methods that estimate an overall average treatment effect, this approach leverages **uplift modeling** to uncover how different customer segments respond to the campaign, enabling more personalized marketing strategies. By utilizing **meta-learners** (including T-Learner, S-Learner, and X-Learner), I capture heterogeneous effects and compare their performance using robust evaluation metrics.

## Objective

The primary objectives are:
- Estimate the **CATE** of an email campaign on customer spending.
- Utilize **meta-learners** to uncover variations in treatment effects across different customer segments.
- Benchmark results using traditional regression models and evaluate the performance of each meta-learner.
- Conduct robustness checks and sensitivity analyses to estimate the business impact. 

You can read more about each meta-learner approach in my [Medium article](https://medium.com/@LillyH/part-2-1-conditional-treatment-heterogenous-effect-estimation-cate-w-7a25916bc6e7).


## Tech Stack
- **Languages**: Python
- **Libraries**:
  - Data Manipulation: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - Modeling: `scikit-learn`, `EconML`, `xgboost`, `lightgbm`
  - Evaluation: `uplift`, `scipy`, `statsmodels`
