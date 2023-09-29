"""Config file for the script filter_clinical_data.py"""

from pathlib import Path

# Directories
SEG_DIR = Path(
    "/mnt/kannlab_rfa/JuanCarlos/mri-classification-sequences/"
    "curated_no_ops_60_cohort_reviewed/output/seg_predictions"
)
OUTPUT_DIR = Path(
    "/mnt/kannlab_rfa/JuanCarlos/mri-classification-sequences/"
    "curated_no_ops_60_cohort_reviewed/output"
)
PLOTS_DIR = OUTPUT_DIR / "volume_plots"
CSV_DIR = OUTPUT_DIR / "time_series_csv"

# Individual files
REDCAP_FILE = Path(
    "/home/jc053/GIT/mri_longitudinal_analysis/data/redcap/redcap_full_89_cohort.csv"
)
FEW_SCANS_FILE = OUTPUT_DIR / "patients_with_few_scans.txt"
ZERO_VOLUME_FILE = OUTPUT_DIR / "zero_volume_segmentations.txt"
NUMBER_TOTAL_PATIENTS = 89

# Options for creating the plots
LIMIT_LOADING = None

RAW = True
FILTERED = True
POLY_SMOOTHING = True
KERNEL_SMOOTHING = True
WINDOW_SMOOTHING = True
BANDWIDTH = 200
PLOT_COMPARISON = True

# If test data is being used or not
TEST_DATA = False
