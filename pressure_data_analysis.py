import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense

# Load dataset
data = pd.read_csv('engine_pressure_data.csv')

# Check and handle missing values
print("Missing values in dataset:")
print(data.isnull().sum())
data.fillna(data.mean(), inplace=True)

# Features and target variable
X = data[['temperature', 'rpm', 'load']]
y = data['pressure']

# Scale features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build the model
model = Sequential()
model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=10, validation_data=(X_test, y_test))

# Evaluate the model
loss = model.evaluate(X_test, y_test)
print(f"Model Loss: {loss}")

# Predict
y_pred = model.predict(X_test)
print("Predicted values:", y_pred)
