CREATE TABLE IF NOT EXISTS my_dataset.Sales_Transaction (
  transaction_id INT64,
  product_id INT64,
  quantity INT64
);

INSERT INTO my_dataset.Sales_Transaction (transaction_id, product_id, quantity)
VALUES
  (1, 1, 5),
  (1, 2, 7),
  (2, 3, 1),
  (3, 2, 3);