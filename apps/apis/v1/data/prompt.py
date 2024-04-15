GENERATION_PROMPT = """
Please generate {num_rows} rows of realistic-looking data that follow the same pattern, data types, and value ranges as the example provided. The data should be similar in nature to the example, but not identical, containing a variety of plausible values for each field.

When generating the synthetic data, please keep the following in mind:

1. Maintain the same number of columns and column names as the example.
2. Infer the data types (e.g., string, integer, float, date) for each column based on the example data and ensure the generated data matches those types.
3. For columns containing categorical data, generate values that are similar to the example categories.
4. For columns with numerical data, generate values within a reasonable range based on the example.
5. If there are any dependencies or correlations between columns in the example, try to maintain similar relationships in the generated data.
6. Ensure that the generated data does not contain any duplicate rows.
7. For columns containing unique identifiers, make sure that each generated value is unique across the entire dataset.
8. For columns with textual data that should be unique, generate a diverse set of values to minimize repetition.
9. If necessary, you can append numbers or other identifiers to generated text values to ensure uniqueness while maintaining a realistic appearance.

Please provide only the resulting synthetic dataset in a tabular format CSV, without any additional conversational text or explanations.
"""

TIMESERIES_PROMPT = """
Please generate {num_rows} rows of realistic-looking time-series data that follow the same pattern, data types, and value ranges as the example provided. The data should be similar in nature to the example, but not identical, containing a variety of plausible values for each field.

When generating the synthetic time-series data, please keep the following in mind:

1. Maintain the same number of columns and column names as the example.
2. Infer the data types (e.g., string, integer, float, date) for each column based on the example data and ensure the generated data matches those types.
3. For the timestamp column, generate timestamps in chronological order with realistic intervals based on the example data.
4. For columns with numerical data, generate values that follow a similar trend and seasonality as the example data, taking into account any patterns or fluctuations.
5. Ensure that the generated data does not contain any duplicate timestamps.
6. If there are any dependencies or correlations between columns in the example, try to maintain similar relationships in the generated data.
7. Add realistic noise or variations to the generated values to mimic real-world time-series data.
8. If necessary, you can interpolate or extrapolate values to fill in any gaps or extend the time-series based on the patterns observed in the example data.

Please provide only the resulting synthetic time-series dataset in a tabular format CSV, without any additional conversational text or explanations.
"""