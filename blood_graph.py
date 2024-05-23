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
fig, ax1 = plt.subplots(figsize=(14, 8))

# 스타일 및 마커 설정
styles = ['-', '--', '-.', ':']
markers = ['o', 's', 'D', '*']
colors = ['b', 'r', 'g', 'm']

# 첫 번째 y축 (hb)
ax1.plot(data['index'], data['hb'], linestyle=styles[0], marker=markers[0], color=colors[0], label='HB', linewidth=2, markersize=8)
ax1.set_xlabel('Index')
ax1.set_ylabel('HB', color=colors[0])
ax1.tick_params(axis='y', labelcolor=colors[0])

# 두 번째 y축 (wbc)
ax2 = ax1.twinx()
ax2.plot(data['index'], data['wbc'], linestyle=styles[1], marker=markers[1], color=colors[1], label='WBC', linewidth=2, markersize=8)
ax2.set_ylabel('WBC', color=colors[1])
ax2.tick_params(axis='y', labelcolor=colors[1])

# 세 번째 y축 (anc)
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # y축을 오른쪽으로 약간 이동
ax3.plot(data['index'], data['anc'], linestyle=styles[2], marker=markers[2], color=colors[2], label='ANC', linewidth=2, markersize=8)
ax3.set_ylabel('ANC', color=colors[2])
ax3.tick_params(axis='y', labelcolor=colors[2])

# 네 번째 y축 (plt)
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))  # y축을 오른쪽으로 더 이동
ax4.plot(data['index'], data['plt'], linestyle=styles[3], marker=markers[3], color=colors[3], label='PLT', linewidth=2, markersize=10)
ax4.set_ylabel('PLT', color=colors[3])
ax4.tick_params(axis='y', labelcolor=colors[3])

# x축 레이블을 날짜로 변경
ax1.set_xticks(data['index'])
ax1.set_xticklabels(data['date'].dt.strftime('%Y-%m-%d'), rotation=45)

# 그래프 꾸미기
fig.suptitle('Line Plot of HB, WBC, ANC, and PLT over Time')
fig.tight_layout()

# 범례 추가
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()

ax1.legend(lines + lines2 + lines3 + lines4, labels + labels2 + labels3 + labels4, loc='upper left', fontsize='large')

# 그래프 보여주기
plt.show()
