from toolz import curry 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@curry
def effect(data, y, t):
    # calculate th difference in mean outcome for treatment and control group
    ate = data[data[t]==1][y].mean() - data[data[t]==0][y].mean()
    return ate

# function to calculate the effect by quantile
def effect_by_quantile(df, pred, y, t, q=10):
    # sort the df by predicted uplift
    df = df.sort_values(by=pred, ascending=True).reset_index(drop=True)

    # make quantile partitions
    groups = np.round(pd.IntervalIndex(pd.qcut(df[pred], q=q)).mid, 2)

    return (
        df
        .assign(**{f"{pred}_quantile": groups})
        .groupby(f"{pred}_quantile")
        # estiamte the effect on each quantile
        .apply(effect(y=y, t=t))
    )

def cumulative_effect_curve(dataset, prediction, y, t, ascending=False, steps=100):
    size = len(dataset)
    ordered_df = (
        dataset
        .sort_values(by=prediction, ascending=ascending)
        .reset_index(drop=True)
    )
    steps = np.linspace(size/steps, size, steps).round(0)
    return np.array([effect(ordered_df.query(f"index<={row}"), t=t, y=y) for row in steps])

def cumulative_gain_curve(df, prediction, y, t,
                          ascending=False, normalize=False, steps=100):
    
    effect_fn = effect(t=t, y=y)
    normalizer = effect_fn(df) if normalize else 0
    
    size = len(df)
    ordered_df = (df
                  .sort_values(prediction, ascending=ascending)
                  .reset_index(drop=True))
    
    steps = np.linspace(size/steps, size, steps).round(0)
    effects = [(effect_fn(ordered_df.query(f"index<={row}"))
                -normalizer)*(row/size) 
               for row in steps]

    return np.array([0] + effects)

def plot_uplift_curve(df, spend_col, treatment_col, models, normalized=False, steps=100, figsize=(10, 5)):
    # Set up the figure and axis
    fig, ax = plt.subplots(1, 1, figsize=figsize)

    # Loop through each model and plot its cumulative gain curve
    for m in models:
        # Compute the cumulative gain curve for the model
        cumu_gain = cumulative_gain_curve(df, m, spend_col, treatment_col, steps=steps, normalize=normalized)
        x = np.array(range(len(cumu_gain)))  # X-axis for top percentages
        ax.plot(100 * (x / x.max()), cumu_gain, label=m)

    # Add a horizontal line for a random model as the baseline
    ax.hlines(0, 0, 100, linestyle="--", label="Random Model", color="black")

    # Set axis labels and the title, updating the title based on normalization
    ax.set_xlabel("Top %")
    ax.set_ylabel("Cumulative Gain")
    ax.set_title("Cumulative Gain Curve (Normalized)" if normalized else "Cumulative Gain Curve (Unnormalized)")
    
    # Show legend and display the plot
    ax.legend()
    plt.show()



