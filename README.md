# Instagram Survey Data Processing Pipeline

This repository processes survey data from an Instagram-related study, performing preprocessing, statistics, standardization, and visualizations. It's structured for sequential execution and is beginner-friendly with detailed comments.

## Directory Structure
- **data/**: Place input files here (e.g., original.xlsx). Outputs like CSVs will be saved here.
- **src/**: Python scripts to run in sequence.
- **figures/**: Generated plots from visualizations.py.

## Setup Instructions
1. Clone the repo: `git clone https://github.com/kami1712/Caption-Hashtag-Impact.git`
2. Navigate to the repo: `cd Caption-Hashtag-Impact.git`
3. Install dependencies: `pip install -r requirements.txt`
4. Place input files in /data/:
   - original.xlsx: The original survey Excel file.
5. Run scripts in sequence from the root directory:
   - `python src/preprocessing.py` (Generates processed CSVs in /data/)
   - `python src/compute_statistics.py` (Prints stats; uses original.xlsx)
   - `python src/standardization.py` (Generates FINAL_data_for_regression.csv in /data/)
   - `python src/data_exploration.py` (Generates plots in /figures/)
   - `python src/result_visualisation.py` (Generate result related plots in /figures/
6. View outputs: CSVs in /data/, plots in /figures/, and console prints for stats.

## Script Sequence and Expectations
- **preprocessing.py**: 
  - Input: data/original.xlsx
  - Output: Multiple CSVs in /data/ (e.g., IG_only.csv, merged_data_with_all_columns.csv)
  - Purpose: Cleans, filters, adds derived columns, merges data.
- **statistics.py**: 
  - Input: data/original.xlsx
  - Output: Console prints (stats for thesis Section 4.4)
  - Purpose: Computes descriptive stats.
- **standardization.py**: 
  - Input: data/merged_data_with_all_columns.csv (from preprocessing)
  - Output: data/FINAL_data_for_regression.csv
  - Purpose: Standardizes data for regression.
- **data_exploration.py**: 
  - Input: Various CSVs from prior steps (e.g., complete_data.csv, dataset.csv)
  - Output: PNG/PDF plots in /figures/
  - Purpose: Generates graphs for analysis of the raw data.
- **result_visualisation.py**: 
  - Input: Various CSVs from the final regression file 
  - Output: PNG/PDF plots in /figures/
  - Purpose: Generates graphs for interpretation of the results.
