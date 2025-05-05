
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn import metrics
import pandas as pd
csv1=pd.read_csv("Battery_Data.csv")
#print(csv1)
X=scale(csv1[["Battery Age (Years)","Charge Cycle/24hrs"]])
X=pd.DataFrame(X,columns=["Battery Age (Years)","Charge Cycle/24hrs"])
y=csv1["Battery Wear Level (%)"]
#creating model
knn=neighbors.KNeighborsRegressor(n_neighbors=7,weights='uniform') 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
knn.fit(X_train,y_train)
prediction=knn.predict(X_test)
aslist=prediction.tolist()
#accuracy
mse=metrics.mean_squared_error(y_test,prediction)
print("Prediction is: ",aslist)
print(f"mse is: {mse:.2f}")
print("/////////////////////")
a=float(input("enter the battery age: "))
b=float(input("enter the charge cycle: "))
inputdata=pd.DataFrame({"Battery Age (Years)":[a],"Charge Cycle/24hrs":[b]})
pdtest=knn.predict(inputdata)
print(f"the battery wear level is: {pdtest[0]:.2f}%")




