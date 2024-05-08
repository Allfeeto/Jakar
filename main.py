import streamlit as st
import pandas as pd
import numpy as np

def jaccard_similarity(a, b, c):
    return c / (a + b - c)

st.title('Коэффициент Жаккара')

uploaded_file = st.file_uploader("Загрузите файл Excel", type=["xls", "xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, index_col=0)
    st.write(df)

    CountX, CountY = df.shape  # Поменяли местами, чтобы соответствовать ожидаемым размерностям

    jaccard_matrix = np.zeros((CountY, CountY))  # Исправлено на CountY, CountY

    for i in range(CountY):
        for j in range(i, CountY):  # Циклы для итерации по парам столбцов без повторений
            a = sum(df.iloc[:, i])
            b = sum(df.iloc[:, j])  # Исправлено на итерацию по столбцам
            c = sum(df.iloc[:, i] & df.iloc[:, j])  # Подсчет пересечения
            jaccard_matrix[i, j] = jaccard_similarity(a, b, c)
            jaccard_matrix[j, i] = jaccard_similarity(a, b, c)  # Симметричная матрица

    jaccard_df = pd.DataFrame(jaccard_matrix, columns=df.columns, index=df.columns)  # Исправлено на df.columns
    np.fill_diagonal(jaccard_matrix, 1)
    st.write(jaccard_df)
