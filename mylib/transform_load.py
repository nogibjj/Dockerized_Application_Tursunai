from pyspark.sql.functions import col
from pyspark.sql import SparkSession


def transform(data_path, spark):
    """
    Transforms the dataset by cleaning column names.

    Args:
        data_path (str): Path to the dataset file.
        spark (SparkSession): Active Spark session.

    Returns:
        DataFrame: Transformed DataFrame with cleaned column names.
    """
    if spark is None:
        raise ValueError("A Spark session must be provided.")

    print(f"Loading data from {data_path}...")
    df = spark.read.csv(data_path, header=True, inferSchema=True)

    print("Cleaning column names...")
    transformed_df = df.select(
        [
            col(c).alias(
                c.replace("(", "")
                .replace(")", "")
                .replace(" ", "_")
                .replace("-", "_")
                .replace("/", "_")
            )
            for c in df.columns
        ]
    )

    print("Data transformation complete.")
    return transformed_df


def load(df, output_path, file_format="parquet"):
    """
    Loads the DataFrame into the specified file format.

    Args:
        df (DataFrame): DataFrame to save.
        output_path (str): Output path for the saved file.
        file_format (str): Format to save the data ('parquet', 'csv', or 'json').

    Returns:
        str: Success message with the output path and format.
    """
    print(f"Saving data to {output_path} in {file_format} format...")
    if file_format == "parquet":
        df.write.mode("overwrite").parquet(output_path)
    elif file_format == "csv":
        df.write.mode("overwrite").option("header", True).csv(output_path)
    elif file_format == "json":
        df.write.mode("overwrite").json(output_path)
    else:
        raise ValueError("Unsupported file format. Choose 'parquet', 'csv', or 'json'.")

    print(f"Data successfully saved to {output_path}")
    return f"Data saved to {output_path} in {file_format} format."


if __name__ == "__main__":
    # Initialize Spark session
    spark = SparkSession.builder.appName("TransformLoadUrbanizationData").getOrCreate()

    # Input and output paths
    input_path = "dbfs:/tmp/urbanization_census_tract.csv"
    output_path = "dbfs:/tmp/urbanization_census_tract_transformed.parquet"
    file_format = "parquet"  # Change to 'csv' or 'json' if needed

    # Transform and load
    try:
        transformed_df = transform(data_path=input_path, spark=spark)
        load(transformed_df, output_path=output_path, file_format=file_format)
    except Exception as e:
        print(f"An error occurred: {e}")
