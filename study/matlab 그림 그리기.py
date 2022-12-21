# subplot으로 그리기
# matlab 또는 figure 상관 없이 아무거나 사용하기

import numpy as np
import matplotlib.pyplot as plt


def main():
    Score = np.random.randint(100, size=(10, 4))  # 국영수과
    print('Score')
    print(Score)
    picture_one(Score)
    picture_two(Score)
    picture_three(Score)
    picture_four(Score)


# 문제 1 : scatter
def picture_one(Score):
    x = Score[:, 1]
    y = Score[:, 0]
    plt.scatter(x, y, marker='^', color='c')
    plt.xlabel('English')
    plt.ylabel('Korea');
    plt.show()


# 문제 2 : subplot, histogram
def picture_two(Score):
    plt.subplots_adjust(hspace=0.4, wspace=0.4)

    plt.subplot(2, 2, 1)
    plt.hist(Score[:, 0])
    plt.xlabel('Korea')
    plt.ylabel('Count')

    plt.subplot(2, 2, 2)
    plt.hist(Score[:, 1])
    plt.xlabel('English')
    plt.ylabel('Count')

    plt.subplot(2, 2, 3)
    plt.hist(Score[:, 2])
    plt.xlabel('Math')
    plt.ylabel('Count')

    plt.subplot(2, 2, 4)
    plt.hist(Score[:, 3])
    plt.xlabel('Science')
    plt.ylabel('Count')

    plt.show()


# 문제 3 : pie
def picture_three(Score):
    korea = Score[:, 0]

    # 다른 방법
    #     a = korea[korea>=90]
    #     b = korea[korea<90]
    #     b1 = b[b>=80]
    #     c = korea[korea<80]
    #     c1 = c[c>=70]
    #     d = korea[korea<70]

    a_count = (korea >= 90).sum()
    tmp1 = (korea[korea >= 80])  # 에러 주의! (따로 분리해서 부등호 사용하기)
    b_count = (tmp1 < 90).sum()
    tmp2 = korea[korea >= 70]
    c_count = (tmp2 < 80).sum()
    d_count = (korea < 70).sum()

    arrlist = [a_count, b_count, c_count, d_count]
    label = ['A', 'B', 'C', 'D']
    plt.pie(arrlist, labels=label)
    plt.show()


# 문제 4 : boxplot
def picture_four(Score):
    a = [np.max(Score[:, 0]), np.mean(Score[:, 0]), np.min(Score[:, 0])]
    b = [np.max(Score[:, 1]), np.mean(Score[:, 1]), np.min(Score[:, 1])]
    c = [np.max(Score[:, 2]), np.mean(Score[:, 2]), np.min(Score[:, 2])]
    d = [np.max(Score[:, 3]), np.mean(Score[:, 3]), np.min(Score[:, 3])]

    plt.boxplot([a, b, c, d])
    plt.xticks([1, 2, 3, 4], ['Kor', 'Eng', 'Math', 'Science'])
    plt.show()


main()