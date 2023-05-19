-- transaction with class id and class name
with sales_with_class as (
    select
        p2.product_class_name,
        p1.product_name,
        SUM(t1.quantity*p1.retail_price) as sales_value,
        SUM(t1.quantity) as quantity
    from Sales_Transaction t1
    left join Product p1 on t1.product_id = p1.product_id
    left join Product_Class p2 on p1.product_class_id = p2.product_class_id
    GROUP BY p2.product_class_name, p1.product_name
),
-- top_sales with rank
top_sales as (
    select
        product_class_name,
        row_number() over (
            partition by product_class_name
            order by sales_value DESC, quantity ASC 
        ) as rank,
        product_name,
        sales_value
    from sales_with_class
)
-- main clause
select
    product_class_name,
    rank,
    product_name,
    sales_value
from top_sales
where rank <= 2
order by product_class_name;
