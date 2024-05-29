import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Seaborn 스타일 설정
sns.set(style="whitegrid")

# CSV 파일 읽어오기
file_path = 'blood.csv'  # CSV 파일 경로를 지정하세요
data = pd.read_csv(file_path)

# 날짜 열을 datetime 형식으로 변환
data['date'] = pd.to_datetime(data['date'])

# 데이터 인덱스 재설정
data['index'] = range(len(data))

# 그래프 생성
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 스타일 및 마커 설정
styles = ['-', '--', '-.', ':']
markers = ['o', 's', 'D', '*']
colors = ['b', 'r', 'g', 'm']
marker_sizes = [6, 6, 6, 8]  # 마커 사이즈 설정 (별은 그대로 8로 설정)

def add_annotations(ax, x_data, y_data, color):
    for i in range(len(x_data)):
        ax.annotate(f'{y_data[i]}', (x_data[i], y_data[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color=color)

# 첫 번째 그래프 (hb)
ax1 = axes[0, 0]
ax1.plot(data['index'], data['hb'], linestyle=styles[0], marker=markers[0], color=colors[0], label='HB', linewidth=2, markersize=marker_sizes[0])
ax1.set_xlabel('Index')
ax1.set_ylabel('HB', color=colors[0])
ax1.tick_params(axis='y', labelcolor=colors[0])
ax1.set_title('HB over Time')
ax1.set_xticks(data['index'])
ax1.set_xticklabels(data['date'].dt.strftime('%Y-%m-%d'), rotation=45)
add_annotations(ax1, data['index'], data['hb'], colors[0])

# 두 번째 그래프 (wbc)
ax2 = axes[0, 1]
ax2.plot(data['index'], data['wbc'], linestyle=styles[1], marker=markers[1], color=colors[1], label='WBC', linewidth=2, markersize=marker_sizes[1])
ax2.set_xlabel('Index')
ax2.set_ylabel('WBC', color=colors[1])
ax2.tick_params(axis='y', labelcolor=colors[1])
ax2.set_title('WBC over Time')
ax2.set_xticks(data['index'])
ax2.set_xticklabels(data['date'].dt.strftime('%Y-%m-%d'), rotation=45)
add_annotations(ax2, data['index'], data['wbc'], colors[1])

# 세 번째 그래프 (anc)
ax3 = axes[1, 0]
ax3.plot(data['index'], data['anc'], linestyle=styles[2], marker=markers[2], color=colors[2], label='ANC', linewidth=2, markersize=marker_sizes[2])
ax3.set_xlabel('Index')
ax3.set_ylabel('ANC', color=colors[2])
ax3.tick_params(axis='y', labelcolor=colors[2])
ax3.set_title('ANC over Time')
ax3.set_xticks(data['index'])
ax3.set_xticklabels(data['date'].dt.strftime('%Y-%m-%d'), rotation=45)
add_annotations(ax3, data['index'], data['anc'], colors[2])

# 네 번째 그래프 (plt)
ax4 = axes[1, 1]
ax4.plot(data['index'], data['plt'], linestyle=styles[3], marker=markers[3], color=colors[3], label='PLT', linewidth=2, markersize=marker_sizes[3])
ax4.set_xlabel('Index')
ax4.set_ylabel('PLT', color=colors[3])
ax4.tick_params(axis='y', labelcolor=colors[3])
ax4.set_title('PLT over Time')
ax4.set_xticks(data['index'])
ax4.set_xticklabels(data['date'].dt.strftime('%Y-%m-%d'), rotation=45)
add_annotations(ax4, data['index'], data['plt'], colors[3])

# 그래프 꾸미기
fig.suptitle('Line Plots of HB, WBC, ANC, and PLT over Time')
fig.tight_layout(rect=[0, 0, 1, 0.96])  # 제목과 겹치지 않게 여백 조정

# 그래프 보여주기
plt.show()
