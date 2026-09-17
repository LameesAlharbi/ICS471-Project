# ICS 471 - Project Proposal
# Loading EuroSAT and getting the stuff I need for the proposal (samples, class counts, plots)

# installing the datasets library first
!pip install datasets -q

from datasets import load_dataset
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# loading eurosat from hugging face
dataset = load_dataset("Honaker/eurosat_dataset")
print(dataset)

# the 10 classes, in order (0-9)
class_names = [
    "AnnualCrop", "Forest", "HerbaceousVegetation", "Highway",
    "Industrial", "Pasture", "PermanentCrop", "Residential",
    "River", "SeaLake"
]

train_data = dataset["train"]

# just checking the sizes of everything and what one sample looks like
print("Train size:", len(dataset["train"]))
print("Validation size:", len(dataset["validation"]))
print("Test size:", len(dataset["test"]))
print("Example item:", train_data[0])
print("Image size:", train_data[0]["image"].size)  # should be 64x64

# counting how many images are in each class so i can check the balance
labels = train_data["label"]
counts = Counter(labels)
print("\nClass counts (train split):")
for i, name in enumerate(class_names):
    print(f"{name}: {counts[i]}")

# grabbing one image from each class to show as samples
fig, axes = plt.subplots(2, 5, figsize=(15, 6))
seen_classes = {}
for item in train_data:
    label = item["label"]
    if label not in seen_classes:
        seen_classes[label] = item["image"]
    if len(seen_classes) == 10:
        break  # got one of each, no need to keep looping

for i, ax in enumerate(axes.flat):
    ax.imshow(seen_classes[i])
    ax.set_title(class_names[i])
    ax.axis("off")

plt.suptitle("EuroSAT: One Sample per Class", fontsize=14)
plt.tight_layout()
plt.savefig("sample_images.png", dpi=150)
plt.show()

# bar chart for the class distribution
plt.figure(figsize=(10, 5))
counts_ordered = [counts[i] for i in range(10)]
plt.bar(class_names, counts_ordered, color="steelblue")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Number of images")
plt.title("EuroSAT Class Distribution (Train Split)")
plt.tight_layout()
plt.savefig("class_distribution.png", dpi=150)
plt.show()

# double checking all images are actually 64x64 like they're supposed to be
# (just checking a sample of 200, going through all 21600 would take forever)
sizes = set()
for item in train_data.select(range(200)):
    sizes.add(item["image"].size)
print("\nUnique image sizes found (sample of 200):", sizes)
