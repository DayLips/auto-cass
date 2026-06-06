-- public.shops определение

-- Drop table

-- DROP TABLE shops;

CREATE TABLE shops (
	id serial4 NOT NULL,
	"name" varchar(50) NOT NULL,
	num_shop int4 NOT NULL,
	description text NULL,
	CONSTRAINT shops_name_key UNIQUE (name),
	CONSTRAINT shops_num_shop_key UNIQUE (num_shop),
	CONSTRAINT shops_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_shops_id ON public.shops USING btree (id);