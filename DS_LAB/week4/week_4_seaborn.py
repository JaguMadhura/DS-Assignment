import seaborn as sns
iris = sns.load_dataset("iris")
print(iris.head())

objective = "Classdification: Survived (Yes/No)"
success_criteria = "Accuracy > 80%"
constraints = "Limited features, missing values, imbalance classes"
print("Objective:", objective)
print("Success Critria", success_criteria)
print("Constraints:", constraints)
