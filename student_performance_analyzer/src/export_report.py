import pandas as pd

def export_summary(input_file, output_file="final_report.csv"):
    try:
        df = pd.read_csv(input_file)

        # Calculate average per student
        avg_df = df.groupby("student_name")["marks"].mean().reset_index()
        avg_df.rename(columns={"marks": "average_marks"}, inplace=True)

        # Rank students
        avg_df["rank"] = avg_df["average_marks"].rank(ascending=False, method="dense")

        avg_df.sort_values("rank", inplace=True)

        avg_df.to_csv(output_file, index=False)

        print(f"Report exported successfully as {output_file}")

    except FileNotFoundError:
        print("Input CSV file not found")
