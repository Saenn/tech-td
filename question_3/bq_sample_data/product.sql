CREATE TABLE IF NOT EXISTS my_dataset.Product (
  product_id INT64,
  product_name STRING,
  retail_price INT64,
  product_class_id INT64
);

INSERT INTO my_dataset.Product (product_id, product_name, retail_price, product_class_id)
VALUES
  (1, aa, 10, 1),
  (2, bb, 20, 1),
  (3, cc, 30, 2);
