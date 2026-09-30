from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

veri = load_breast_cancer()

X = veri.data
y = veri.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
tahminler = model.predict(X_test)

dogruluk = accuracy_score(y_test, tahminler)
print("Doğruluk (accuracy):",dogruluk)
print("Yüzde olarak: %",dogruluk * 100)

matris = confusion_matrix(y_test,tahminler)
print("\nConfusion Matrix:")
print(veri.target_names)
print(matris)
