CREATE TABLE IF NOT EXISTS my_dataset.Product_Class (
  product_class_id INT64,
  product_class_name STRING,
);

INSERT INTO my_dataset.Product_Class (product_class_id, product_class_name)
VALUES
  (1, 'Class A'),
  (2, 'Class B'),
  (3, 'Class C');
