import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd
from constants import display_data_dictionary

df = pd.read_csv("preprocessed_gym.csv")

st.title("Data Analysis for below provided Dataframe:")
with st.expander("View Dataframe"):
    st.dataframe(df)



st.write("---")

with st.expander("📚 Data Dictionary - Complete Categorical Mappings"):
    display_data_dictionary()




st.write("---")
with st.expander("Line Chart"):
    with st.form("Select the required axis"):
        x = st.selectbox("X axis:",['Age','Weight (kg)','Height (m)','BMI','Session_Duration (hours)','Daily_Calorie_Intake (kcal)','Calorie_Balance (kcal)','Fat_Percentage'])
        y = st.selectbox("Y axis:",['Age','Weight (kg)','Height (m)','BMI','Session_Duration (hours)','Daily_Calorie_Intake (kcal)','Calorie_Balance (kcal)','Fat_Percentage'])
        if st.form_submit_button("Draw Graph"):
            if x == y:
                st.warning("Choose different columns for X and Y axes.")
            else:
                df_plot = df[[x, y]]
                if df_plot[x].duplicated().any():
                    st.info("Duplicate X values detected. Aggregating Y values by mean for each X.")
                    df_plot = df_plot.groupby(x, as_index=False)[y].mean()
                else:
                    df_plot = df_plot.sort_values(x)
                fig, ax = plt.subplots()
                ax.plot(df_plot[x], df_plot[y], marker='o')
                ax.set_xlabel(x)
                ax.set_ylabel(y)
                ax.set_title(f"{y} vs {x}")
                st.pyplot(fig)

numeric_columns = df.select_dtypes(include=['int64','float64']).columns.tolist()
categorical_columns = [col for col in df.columns if df[col].dtype == 'object' or df[col].nunique() <= 10]
recommended_pairs = [
    ("Age", "BMI"),
    ("Weight (kg)", "Fat_Percentage"),
    ("Session_Duration (hours)", "Calories_Burned"),
    ("Daily_Calorie_Intake (kcal)", "Calorie_Balance (kcal)"),
]


with st.expander("Scatter Plots"):
    st.write("Use numeric columns for scatter plots. Recommended pairs are selected from the dataset.")
    with st.form("Select the required axis scatter"):
        use_recommended = st.checkbox("Use recommended pair", value=True)
        if use_recommended:
            pair_label = [f"{a} vs {b}" for a, b in recommended_pairs]
            choice = st.selectbox("Recommended pairs", pair_label)
            x, y = recommended_pairs[pair_label.index(choice)]
        else:
            x = st.selectbox("X axis:", numeric_columns, key='scatter_x')
            y = st.selectbox("Y axis:", numeric_columns, key='scatter_y')
        color = st.color_picker("Point color", '#1f77b4')
        size = st.slider("Point size", min_value=5, max_value=100, value=35)
        if st.form_submit_button("Draw Scatter"):
            if x == y:
                st.warning("Choose different columns for X and Y axes for a scatter plot.")
            else:
                df_plot = df[[x, y]].dropna()
                fig, ax = plt.subplots()
                ax.scatter(df_plot[x], df_plot[y], c=color, s=size, alpha=0.7)
                ax.set_xlabel(x)
                ax.set_ylabel(y)
                ax.set_title(f"{y} vs {x} (Scatter)")
                st.pyplot(fig)

with st.expander("Histogram"):
    with st.form("Histogram options"):
        hist_col = st.selectbox("Numeric column:", numeric_columns, key='hist_col')
        bins = st.slider("Bins", min_value=5, max_value=80, value=20, key='hist_bins')
        if st.form_submit_button("Draw Histogram"):
            data = df[hist_col].dropna()
            fig, ax = plt.subplots()
            ax.hist(data, bins=bins, color='#4c78a8', edgecolor='black')
            ax.set_xlabel(hist_col)
            ax.set_ylabel('Count')
            ax.set_title(f'Histogram of {hist_col}')
            st.pyplot(fig)

with st.expander("Bar Chart"):
    with st.form("Bar chart options"):
        bar_col = st.selectbox("Categorical column:", categorical_columns, key='bar_col')
        max_categories = max(1, min(20, df[bar_col].nunique()))
        top_n = st.slider("Top categories", min_value=1, max_value=max_categories, value=min(10, max_categories), key='bar_top_n')
        if st.form_submit_button("Draw Bar Chart"):
            counts = df[bar_col].astype(str).value_counts().nlargest(top_n)
            fig, ax = plt.subplots()
            ax.bar(counts.index, counts.values, color='#ff7f0e')
            ax.set_xlabel(bar_col)
            ax.set_ylabel('Count')
            ax.set_title(f'Bar chart of {bar_col}')
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)

with st.expander("Box Plot"):
    with st.form("Box plot options"):
        box_y = st.selectbox("Numeric column:", numeric_columns, key='box_y')
        box_group = st.selectbox("Group by (optional):", [None] + categorical_columns, key='box_group')
        if st.form_submit_button("Draw Box Plot"):
            fig, ax = plt.subplots()
            if box_group:
                df_box = df[[box_group, box_y]].dropna()
                groups = [group[box_y].values for _, group in df_box.groupby(box_group)]
                labels = [str(name) for name, _ in df_box.groupby(box_group)]
                ax.boxplot(groups, labels=labels, patch_artist=True)
                ax.set_xlabel(box_group)
                ax.set_ylabel(box_y)
                ax.set_title(f'{box_y} by {box_group}')
                plt.xticks(rotation=45, ha='right')
            else:
                ax.boxplot(df[box_y].dropna(), patch_artist=True)
                ax.set_ylabel(box_y)
                ax.set_title(f'Box plot of {box_y}')
            st.pyplot(fig)



