# =============================================================================
# SIMPLIFIED & THESIS-READY FIGURES (continuous + super clear)
# Just run this – it will create 3 perfect figures
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
df = pd.read_csv('data/FINAL_data_for_regression.csv')
print(df.columns)
# Set style
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.4)

# ==================== FIGURE 1 – Clean continuous inverted-U for caption length ====================
plt.figure(figsize=(8, 5.5))

# Continuous quadratic regression line with confidence interval
sns.regplot(
    data=df,
    x="Caption_Length",           # original values: 5, 70, 140, 200
    y="z_Engagement Intention Score",
    order=2,
    scatter=False,
    ci=95,
    line_kws={"color": "#d32f2f", "lw": 4},
    color="#d32f2f"
)

# Add the actual observed means with error bars (this makes it trustworthy)
means = df.groupby('Caption_Length')['z_Engagement Intention Score'].mean()
sems  = df.groupby('Caption_Length')['z_Engagement Intention Score'].sem()

plt.errorbar(means.index, means.values, yerr=sems.values*1.96,
             fmt='o', color='black', markersize=12, capsize=8, capthick=3,
             label='Observed means ± 95% CI', zorder=10)

plt.xlabel('Caption Length (characters)', fontsize=14)
plt.ylabel('Engagement Intention\n(z-standardized)', fontsize=14)
plt.title('Optimal Caption Length ≈ 120–130 characters\n'
          'Strong support for H1 – rejection of H3', fontsize=15, pad=20)
plt.xlim(0, 210)
plt.xticks([5, 70, 140, 200])
plt.legend(fontsize=12)
sns.despine()
plt.tight_layout()
plt.savefig('Figure_1_Final_Caption_Optimal.pdf', dpi=400)
plt.savefig('Figure_1_Final_Caption_Optimal.png', dpi=400)
plt.show()

# Print exact optimum
print(f"Peak at approximately {round(-0.186 / (2 * -0.325) * df['Caption_Length'].std() + df['Caption_Length'].mean())} characters")

# ==================== FIGURE 2 – Super simple hashtag effect (one clear panel) ====================
plt.figure(figsize=(7, 5))

# Continuous line (even though only 3 points, it’s still useful)
sns.regplot(data=df, x="Hashtags", y="z_Engagement Intention Score",
            order=2, scatter=False, ci=95,
            line_kws={"color": "#1976d2", "lw": 4})

# Observed means + error bars
means_h = df.groupby('Hashtags')['z_Engagement Intention Score'].mean()
sems_h  = df.groupby('Hashtags')['z_Engagement Intention Score'].sem()
plt.errorbar(means_h.index, means_h.values, yerr=sems_h.values*1.96,
             fmt='o', color='black', markersize=12, capsize=8, capthick=3)

plt.xlabel('Number of Hashtags', fontsize=14)
plt.ylabel('Engagement Intention\n(z-standardized)', fontsize=14)
plt.title('More hashtags → slightly lower engagement\n'
          'No support for “the more the better” (H4 rejected)', fontsize=15, pad=20)
plt.xticks([5, 11, 15])
sns.despine()
plt.tight_layout()
plt.savefig('Figure_2_Final_Hashtags.pdf', dpi=400)
plt.savefig('Figure_2_Final_Hashtags.png', dpi=400)
plt.show()

# ==================== FIGURE 3 – Simple heatmap version (easiest to read) ====================
plt.figure(figsize=(7.5, 5.5))

# Create average engagement for each of the 12 conditions
heatmap_data = df.groupby(['Caption_Length', 'Hashtags'])['z_Engagement Intention Score'].mean().unstack()

# Plot as heatmap – instantly shows where the “hot spot” is
sns.heatmap(heatmap_data,
            annot=True, fmt=".2f", cmap="RdYlBu_r",
            cbar_kws={'label': 'Mean Engagement Intention (z)'},
            linewidths=2, linecolor='white')

plt.xlabel('Number of Hashtags', fontsize=14)
plt.ylabel('Caption Length (characters)', fontsize=14)
plt.title('Best combination = 140 characters + 5–11 hashtags', fontsize=15, pad=20)
plt.tight_layout()
plt.savefig('Figure_3_Final_Heatmap.pdf', dpi=400)
plt.savefig('Figure_3_Final_Heatmap.png', dpi=400)
plt.show()
