from easyDataverse import Dataset

# Initialize EasyDataverse dataset
dataset = Dataset.connect(url="http://localhost:8080")

print("Connected to DV instance ...")

for metadatablock in dataset.metadatablocks.values():
    metadatablock.info()

print("Creating a simple dataset ...")

# Fill Citation metadatablock
dataset.citation.title = "Test"
dataset.citation.add_ds_description(value="This is a test")
dataset.citation.add_author(name="John Doe", affiliation="Doe University")
dataset.citation.add_dataset_contact(name="John Doe", email="jonhdoe@doetastic.com")
dataset.citation.subject = ["Earth and Environmental Sciences"]

print(dataset.dataverse_json())
