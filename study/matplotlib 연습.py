import numpy as np
Score = np.random.randint(100, size=(10, 4)) # 국 영 수 과

# x축은 영어, y축은 국어로 흩뿌리기
import matplotlib.pyplot as plt
x = Score[:, 1:2]
y = Score[:, :1]
plt.scatter(x, y)

# 스타일 ggplot
# x=0~100까지 100 나누기
# y=3x+7을 plot그래프 짧은 점선 초록색
plt.style.use('ggplot')
x = np.linspace(0, 100, 100)
y = 3*x + 7
plt.plot(x, y, linestyle='--', color='green')