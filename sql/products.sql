-- public.products определение

-- Drop table

-- DROP TABLE products;

CREATE TABLE products (
	id serial4 NOT NULL,
	"name" varchar(50) NOT NULL,
	description text NULL,
	category_id int4 NOT NULL,
	CONSTRAINT products_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_products_id ON public.products USING btree (id);
CREATE INDEX ix_products_name ON public.products USING btree (name);


-- public.products внешние включи

ALTER TABLE public.products ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES categories(id);