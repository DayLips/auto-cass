-- public.categories определение

-- Drop table

-- DROP TABLE categories;

CREATE TABLE categories (
	id serial4 NOT NULL,
	"name" varchar(20) NOT NULL,
	description text NULL,
	CONSTRAINT categories_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_categories_id ON public.categories USING btree (id);
CREATE UNIQUE INDEX ix_categories_name ON public.categories USING btree (name);