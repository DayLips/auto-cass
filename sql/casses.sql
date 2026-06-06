-- public.casses определение

-- Drop table

-- DROP TABLE casses;

CREATE TABLE casses (
	id serial4 NOT NULL,
	num_cass int4 NOT NULL,
	total_money numeric NOT NULL,
	available bool NOT NULL,
	shop_id int4 NOT NULL,
	CONSTRAINT casses_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_casses_id ON public.casses USING btree (id);


-- public.casses внешние включи

ALTER TABLE public.casses ADD CONSTRAINT casses_shop_id_fkey FOREIGN KEY (shop_id) REFERENCES shops(id);