import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# 假设df是你的DataFrame，'target_col'是你想要插补的列，其余列为特征
df = pd.DataFrame({
    'feature1': [1, 2, np.nan, 4, 5],
    'feature2': [np.nan, 3, 4, 5, 6],
    'target_col': [10, 20, np.nan, 40, np.nan]
})

# 处理缺失值，这里先简单填充为0，实际应用中可能需要更细致的处理
df.fillna(0, inplace=True)

# 分离特征和目标变量
X = df.drop('target_col', axis=1)
y = df['target_col']

# 数据预处理，例如标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 构建神经网络模型
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=X_train.shape[1]))  # 输入层
model.add(Dense(16, activation='relu'))  # 隐藏层
model.add(Dense(1))  # 输出层

# 编译模型
model.compile(optimizer=Adam(lr=0.001), loss='mse')

# 训练模型
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=0, validation_data=(X_test, y_test))

# 使用模型预测缺失值
predictions = model.predict(X_scaled)

# 将预测值插回到原DataFrame
df['predicted_target'] = predictions.flatten()
df['target_col'] = df[['target_col', 'predicted_target']].max(axis=1)  # 这里简单地用预测值替换缺失值，实际应用可能需要更复杂的逻辑

print(df)
