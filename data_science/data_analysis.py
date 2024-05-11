import pandas as pd
import scipy.stats as stats


def analyze_data(data):
    # Analyze data using Pandas or SciPy
    # For example, calculate summary statistics, perform statistical tests, or fit distributions

    # Calculate summary statistics
    summary_stats = data.describe()

    # Perform statistical tests
    t_stat, p_val = stats.ttest_1samp(data["feature"], 0)
    print(f"T-statistic: {t_stat:.3f}, p-value: {p_val:.3f}")

    # Fit distributions
    param_estimates = stats.norm.fit(data["feature"])
    print(f"Estimated parameters: {param_estimates}")
