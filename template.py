import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 해커뉴스 점수 계산 함수
def calculate_hn_score(views, hours_since_posted, gravity):
    return (views - 1) / pow((hours_since_posted + 2), gravity)

# 조회수 값
view_counts = [30, 60, 100]  # 기존 아이템들

# 중력 가속도 값
gravity_value = 0.8

# 점수 계산을 위한 DataFrame 생성 (0시간부터 48시간까지, 4시간 간격)
score_data = pd.DataFrame(index=np.arange(0, 49, 4))  # 0시간부터 48시간까지, 4시간 간격

# 기존 아이템들의 점수 계산
for views in view_counts:
    score_data[f'Views={views} with Algorithm'] = calculate_hn_score(views, score_data.index, gravity_value)
    score_data[f'Views={views} without Algorithm'] = views

# 새 아이템 조회수 및 점수 계산 (12시간 이후부터 시작)
new_item_views = 40
for time in score_data.index:
    if time >= 12:
        hours_since_new_item_posted = time - 12
        score_data.loc[time, f'New Item (Views={new_item_views}) after 12 hours'] = calculate_hn_score(new_item_views, hours_since_new_item_posted, gravity_value)
    else:
        score_data.loc[time, f'New Item (Views={new_item_views}) after 12 hours'] = np.nan

# 그래프 그리기
plt.figure(figsize=(15, 8))

# 기존 아이템들의 그래프
for views in view_counts:
    plt.plot(score_data.index, score_data[f'Views={views} with Algorithm'], label=f'Views={views} with Algorithm', linewidth=2)
    plt.plot(score_data.index, score_data[f'Views={views} without Algorithm'], label=f'Views={views} without Algorithm', linestyle='--', linewidth=2)

# 새 아이템의 그래프
plt.plot(score_data.index, score_data[f'New Item (Views={new_item_views}) after 12 hours'], label=f'New Item (Views={new_item_views}) after 12 hours', linewidth=2, linestyle=':', color='red')

# x, y 레이블과 제목 설정
plt.xticks(np.arange(0, 49, 4))
plt.xlabel('Hours Since Submission')
plt.ylabel('Score')
plt.title('Comparison of Item Exposure With and Without Hacker News Algorithm (0-48 Hours Interval)')
plt.legend()
plt.grid(True)
plt.show()
