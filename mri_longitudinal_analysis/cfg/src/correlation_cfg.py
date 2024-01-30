"""Config file for the correlation analysis script."""
from pathlib import Path

CLINICAL_CSV = Path(
    "/home/jc053/GIT/mri_longitudinal_analysis/data/input/clinical/bch_filtered_88.csv"
)

VOLUMES_CSV = Path(
    "/mnt/93E8-0534/JuanCarlos/mri-classification-sequences/bch_longitudinal_dataset/new_review/output/time_series_csv_kernel_smoothed"
)

OUTPUT_DIR = Path("/home/jc053/GIT/mri_longitudinal_analysis/data/output")
OUTPUT_DIR_CORRELATIONS = OUTPUT_DIR / "correlation_plots_bch"
OUTPUT_DIR_STATS = OUTPUT_DIR / "correlation_stats_bch"


COHORT = "BCH"  # "BCH" or "CBTN"

# Step 1
SENSITIVITY = False
SENSITIVITY_THRESHOLD = 2

# Step 2
PROPENSITY = False
CALIPER = 0.1  # usually between 0.05 and 0.2

# Step 3
ANALYSIS_PRE_TREATMENT = True

ANGLE = False
PROGRESSION_THRESHOLD = 10  # angle value that defines progression
HIGH_RISK_THRESHOLD = 25  # angle value that defines high increase
STABILITY_THRESHOLD = 2  # angle value that defines stability

SAMPLE_SIZE = 79  # for plotting growth trajectories, usually number of patients in cohort

VOLUME_WEIGHT = 0.25
GROWTH_WEIGHT = 0.75
CHANGE_THRESHOLD = 25  # % volume change threshold for stability index


# Step 4
CORRECTION = False
CORRECTION_ALPHA = 0.05

# Step 5
FEATURE_ENG = True


#### DICTIONARIES

BCH_SYMPTOMS = {
    "incidental": "No symptoms (incident finding)",
    "headache": "Headaches",
    "migraine": "Headaches",
    "seizure": "Seizures",
    "staring": "Seizures",
    "syncopal": "Neurological deficits",
    "vertigo": "Neurological deficits",
    "scoliosis": "Neurological deficits",
    "curve": "Neurological deficits",
    "foot": "Neurological deficits",
    "developmental": "Developmental delay",
    "macrocephaly": "Developmental delay",
    "hydrocephalus": "Developmental delay",
    "circumference": "Developmental delay",
    "motor": "Developmental delay",
    "craniosynostosis": "Developmental delay",
    "visual": "Visual deficits",
    "diplopia": "Visual deficits",
    "neurofibromatosis": "Visual deficits",
    "eye": "Visual deficits",
    "optic": "Visual deficits",
    "nystagmus": "Visual deficits",
    "proptosis": "Visual deficits",
    "vision": "Visual deficits",
    "ADHD": "Other",
    "vomitting": "Other",
    "vomited": "Other",
    "obesity": "Other",
    "sinusitis": "Other",
    "numbness": "Other",
}

CBTN_SYMPTOMS = {
    "None": "No symptoms (incident finding)",
    "Unavailable": "No symptoms (incident finding)",
    "headaches": "Headaches",
    "seizure": "Seizures",
    "neurological": "Neurological deficits",
    "developmental": "Developmental delay",
    "visual": "Visual deficits",
    "behavior": "Other",
    "endocrinopathy": "Other",
    "hydrocephalus": "Other",
    "other": "Other",
}

BCH_LOCATION = {
    "posterior fossa": "Cerebellum",
    "cerebel": "Cerebellum",
    "vermis": "Cerebellum",
    "temporal": "Cortical",
    "frontal": "Cortical",
    "parietal": "Cortical",
    "sylvian": "Cortical",
    "suprasellar": "Meninges / Suprasellar",
    "thalamic": "Basal Ganglia / Thalamus",
    "thalamus": "Basal Ganglia / Thalamus",
    "basal": "Basal Ganglia / Thalamus",
    "midbrain": "Brainstem",
    "centrum": "Brainstem",
    "tectum": "Brainstem",
    "tectal": "Brainstem",
    "cervicomedullary": "Brainstem",
    "stem": "Brainstem",
    "optic": "Optic Pathway",
    "spinal": "Other",
    "ventricle": "Ventricles",
    "ventricular": "Ventricles",
    "midline": "Other",
    "pineal": "Other",
}

CBTN_LOCATION = {
    "Basal": "Basal Ganglia / Thalamus",
    "Thalamus": "Basal Ganglia / Thalamus",
    "Stem": "Brainstem",
    "Cerebellum": "Cerebellum",
    "Parietal Lobe": "Cortical",
    "Frontal Lobe": "Cortical",
    "Temporal Lobe": "Cortical",
    "Occipital Lobe": "Cortical",
    "Meninges": "Meninges / Suprasellar",
    "Suprasellar": "Meninges / Suprasellar",
    "Optic": "Optic Pathway",
    "Spinal": "Other",
    "Ventricles": "Ventricles",
    "Other": "Other",
}


BCH_GLIOMA_TYPES = {
    "astro": "Astrocytoma",
    "JPA": "Astrocytoma",
    "gang": "Ganglioglioma",
    "glio": "Glial-neuronal glioma",
    "glial": "Glial-neuronal glioma",
    "neuro": "Glial-neuronal glioma",
    "DNET": "Glial-neuronal glioma",
    "neo": "Glial-neuronal glioma",
    "pseudo": "Other",
    "oligodendroglioma": "Other",
    "low": "Plain Low Grade Glioma",
    "tectal": "Plain Low Grade Glioma",
}

CBTN_GLIOMA_TYPES = {
    "gang": "Ganglioglioma",
    "astro": "Astrocytoma",
    "glial": "Glial-neuronal",
}


# Mapping of BCH and CBTN columns
BCH_DTYPE_MAPPING = {
    "BCH MRN": "string",
    "Location": "category",
    "Symptoms": "category",
    "Sex": "category",
    "BRAF Status": "category",
    "Treatment Type": "category",
    "Tumor Progression": "category",
    "Received Treatment": "category",
    "Follow-up Time": "int",
    "Time to Treatment": "int",
    "Histology": "category",
}

BCH_DATETIME_COLUMNS = [
    "Age at First Diagnosis",
    "Age at First Treatment",
    "Age at First Progression",
    "Age at Last Clinical Follow-Up",
]
