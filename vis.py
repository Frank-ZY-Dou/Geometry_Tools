import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# 假设 quaternions 是一个 (N, 4) 形状的数组，N 表示四元数的数量
quaternions = np.random.randn(10000, 4)  # 随机生成一些四元数作为示例

# 设置一个初始四元数作为参考原点
origin_quaternion = np.array([1, 0, 0, 0])

# 归一化所有四元数
norms = np.linalg.norm(quaternions, axis=1).reshape(-1, 1)
quaternions_normalized = quaternions / norms

# 归一化初始四元数
origin_norm = np.linalg.norm(origin_quaternion)
origin_normalized = origin_quaternion / origin_norm

# 计算每个四元数与原点四元数的角度差
dot_products = np.dot(quaternions_normalized, origin_normalized)
angles = np.arccos(np.clip(dot_products, -1.0, 1.0))  # 使用clip防止浮点误差导致的问题

# 使用 PCA 降维到 2D
tsne_200 = TSNE(n_components=2, random_state=0, learning_rate='auto', init='random')
quaternions_2d = tsne_200.fit_transform(quaternions_normalized)


# pca = PCA(n_components=2)
# quaternions_2d = pca.fit_transform(quaternions_normalized)
# quaternions_2d = quaternions_normalized[:,:2]
# 绘制结果
plt.figure(figsize=(10, 8))
scatter = plt.scatter(quaternions_2d[:, 0], quaternions_2d[:, 1], c=angles, cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Angle to Origin Quaternion (radians)')
plt.title('2D Visualization of Quaternions Reduced by t-SNE')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
