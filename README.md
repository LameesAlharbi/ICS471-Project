# ICS 471 Project Proposal: EuroSAT Land-Use Classification

**Author:** Lamees Alharbi
**Course:** ICS 471 (Deep Learning)

## Overview
This repository contains the supporting code for the project proposal on land-use and land-cover classification using the EuroSAT satellite image dataset. The code loads the dataset, inspects its structure and class balance, and generates the two required figures used in the proposal PDF.

## Dataset
- **Source:** [`Honaker/eurosat_dataset`](https://huggingface.co/datasets/Honaker/eurosat_dataset) on Hugging Face (MIT license, redistributed from the [original EuroSAT repository](https://github.com/phelber/EuroSAT))
- **Size:** 27,000 labeled 64×64 RGB satellite images, 10 classes
- **Split:** 21,600 train / 2,700 validation / 2,700 test (predefined by the dataset)

## Files
- `eurosat_proposal.ipynb` (and `eurosat_proposal.py`): loads the dataset, prints dataset statistics and class counts, and generates both required figures
- `sample_images.png`: one representative image per class (Figure 1 in the proposal)
- `class_distribution.png`: class frequency bar chart (Figure 2 in the proposal)

## How to run
This code is designed to run in Google Colab (or any environment with internet access):

```bash
pip install datasets
python eurosat_proposal.py
```

## Reference
Helber, P., Bischke, B., Dengel, A., & Borth, D. (2019). EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification. *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, 12(7), 2217 to 2226.
