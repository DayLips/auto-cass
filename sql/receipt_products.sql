-- public.receipt_products определение

-- Drop table

-- DROP TABLE receipt_products;

CREATE TABLE receipt_products (
	id serial4 NOT NULL,
	receipt_id int4 NOT NULL,
	product_id int4 NOT NULL,
	amount int4 NOT NULL,
	price numeric NOT NULL,
	discount numeric NOT NULL,
	CONSTRAINT receipt_products_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_receipt_products_id ON public.receipt_products USING btree (id);


-- public.receipt_products внешние включи

ALTER TABLE public.receipt_products ADD CONSTRAINT receipt_products_product_id_fkey FOREIGN KEY (product_id) REFERENCES products(id);
ALTER TABLE public.receipt_products ADD CONSTRAINT receipt_products_receipt_id_fkey FOREIGN KEY (receipt_id) REFERENCES receipts(id);